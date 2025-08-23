import gradio as gr
import asyncio
import re
import os
from datetime import datetime
from urllib.parse import urlparse, parse_qs
import openai
from youtube_transcript_api import (
    YouTubeTranscriptApi,
    TranscriptsDisabled,
    NoTranscriptFound,
    VideoUnavailable,
    CouldNotRetrieveTranscript,
)

# Instructions de l'agent
AGENT_INSTRUCTIONS = """Tu es un assistant expert en analyse de vidéos YouTube et en création de contenu.

RÈGLE ABSOLUE : Quand l'utilisateur te donne une URL YouTube, tu DOIS utiliser IMMÉDIATEMENT l'outil fetch_youtube_transcript pour récupérer la transcription.

Processus obligatoire :
1. Détecte l'URL YouTube dans le message
2. Utilise IMMÉDIATEMENT fetch_youtube_transcript(URL) 
3. Analyse la transcription récupérée
4. Réponds en te basant UNIQUEMENT sur cette transcription

Règle stricte anti-hallucination : 
- Si la transcription n'est pas disponible, n'émet AUCUNE supposition sur le contenu
- Informe l'utilisateur que la transcription est indisponible et propose des options concrètes :
  1) coller ici la transcription/les paroles ; 
  2) copier/coller le titre et la description de la vidéo ; 
  3) fournir ses points clés à traiter
- Attends sa réponse et ne produis aucun résumé/avis tant qu'aucun texte source n'a été fourni

Une fois la transcription disponible, tu peux :
1. Analyser le contenu en identifiant les messages clés, le ton employé, les intentions de l'auteur, les cibles et les points marquants
2. Répondre aux questions sur la vidéo
3. Générer des contenus pour les réseaux sociaux :
   - Un post LinkedIn (800 à 1200 caractères), structuré, professionnel, avec une bonne accroche et un appel à l'action
   - Un post Instagram (300 à 600 caractères), plus direct, percutant et adapté au ton de la plateforme

Adapte toujours le style et le ton à la plateforme cible. Si un message central fort ou un angle original se dégage, utilise-le comme fil conducteur."""


# ---------------------------------------------------------------------
# Outil pour récupérer les transcriptions YouTube (version corrigée)
# ---------------------------------------------------------------------
def fetch_youtube_transcript(url: str) -> str:
    """Récupère la transcription d'une vidéo YouTube avec timestamps (FR -> EN -> fallback)."""
    
    print(f"🎬 Début de fetch_youtube_transcript avec URL: {url}")

    def _extract_video_id(u: str):
        # ID direct (11 caractères)
        if re.fullmatch(r"[0-9A-Za-z_-]{11}", u):
            return u
        p = urlparse(u)
        # youtu.be/<id>
        if p.hostname in ("youtu.be",):
            vid = p.path.strip("/")
            return vid if re.fullmatch(r"[0-9A-Za-z_-]{11}", vid) else None
        # youtube.com/watch?v=..., /embed/<id>, /shorts/<id>
        if p.hostname and "youtube.com" in p.hostname:
            qs = parse_qs(p.query)
            if "v" in qs:
                return qs["v"][0]
            m = re.match(r"^/(embed|shorts)/([0-9A-Za-z_-]{11})", p.path)
            if m:
                return m.group(2)
        # Dernier recours
        m = re.search(r"([0-9A-Za-z_-]{11})", u)
        return m.group(1) if m else None

    video_id = _extract_video_id(url)
    if not video_id:
        print("❌ Impossible d'extraire l'ID vidéo")
        return "⚠️ URL YouTube invalide. Impossible d'extraire l'ID vidéo."

    print(f"🎥 Récupération de la transcription pour l'ID: {video_id}")

    try:
        # Créer une instance de l'API
        yt_api = YouTubeTranscriptApi()
        
        # Essayer d'abord de lister les transcriptions disponibles
        try:
            print("🔄 Recherche des transcriptions disponibles...")
            transcript_list = yt_api.list(video_id)
            print(f"📋 Transcripts disponibles: {[t.language_code for t in transcript_list]}")
            
            # Essayer de trouver une transcription en français d'abord
            try:
                transcript = transcript_list.find_transcript(["fr"])
                print(f"✅ Transcription française trouvée")
            except:
                try:
                    # Essayer les sous-titres générés automatiquement en français
                    transcript = transcript_list.find_generated_transcript(["fr"])
                    print(f"✅ Sous-titres générés français trouvés")
                except:
                    # Essayer n'importe quelle transcription disponible
                    transcript = next(iter(transcript_list))
                    print(f"✅ Utilisation de la transcription en {transcript.language_code}")
            
            # Récupérer la transcription
            segments = transcript.fetch()
            print(f"✅ Transcription récupérée en {transcript.language_code}")
            
        except Exception as e:
            print(f"❌ Erreur lors de la recherche de transcriptions: {e}")
            return f"❌ Aucune transcription trouvée pour cette vidéo. Erreur: {e}"

        if not segments:
            print("❌ Aucune donnée de transcription récupérée")
            return "❌ Aucune donnée de transcription récupérée."

        # Formatage [mm:ss] texte - les objets ont des attributs directs, pas de méthode .get()
        lines = []
        for s in segments:
            # Les objets ont des attributs directs : text, start, duration
            txt = getattr(s, 'text', '').strip()
            if not txt:
                continue
            start = float(getattr(s, 'start', 0.0))
            m, sec = divmod(int(start), 60)
            lines.append(f"[{m:02d}:{sec:02d}] {txt}")

        result = "\n".join(lines)
        print(f"✅ Transcription formatée: {len(lines)} fragments, {len(result)} caractères")
        return result if result else "❌ Transcription vide."

    except Exception as e:
        print(f"❌ Erreur inattendue: {e}")
        return f"❌ Erreur inattendue : {e}"

def test_transcription(url: str) -> str:
    """Fonction de test simple pour la transcription YouTube"""
    try:
        result = fetch_youtube_transcript(url)
        return result
    except Exception as e:
        return f"❌ Erreur lors du test : {str(e)}"


def process_youtube_url(url: str) -> str:
    """Traite une URL YouTube et retourne la transcription ou un message d'erreur"""
    if not detect_youtube_url(url):
        return "❌ Ce n'est pas une URL YouTube valide."
    
    print(f"🔍 Traitement de l'URL YouTube : {url}")
    transcription = fetch_youtube_transcript(url)
    
    if transcription.startswith("❌") or transcription.startswith("⚠️"):
        return transcription
    
    # Transcription réussie
    return f"✅ Transcription récupérée avec succès !\n\n{transcription[:500]}...\n\n(Transcription complète : {len(transcription)} caractères)"

# ---------------------------------------------------------------------
# Création de l'agent
# ---------------------------------------------------------------------

def create_openai_client():
    """Crée le client OpenAI"""
    try:
        client = openai.OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))
        return client
    except Exception as e:
        print(f"❌ Erreur lors de la création du client OpenAI : {e}")
        return None

# Variables globales pour l'état de l'application
class AppState:
    def __init__(self):
        self.openai_client = None
        self.api_key = None
        self.current_video = None
        self.conversation_history = []
        self.session_start = datetime.now()

app_state = AppState()


def setup_agent(api_key):
    """Configure le client OpenAI avec la clé API"""
    if not api_key or not api_key.strip():
        return "❌ Veuillez entrer une clé API", "🔴 Non configuré"

    if not api_key.startswith("sk-"):
        return "❌ Format invalide. La clé doit commencer par 'sk-'", "🔴 Erreur"

    try:
        os.environ["OPENAI_API_KEY"] = api_key.strip()
        app_state.api_key = api_key.strip()
        app_state.openai_client = create_openai_client()
        
        if app_state.openai_client:
            print(f"✅ Client OpenAI créé avec succès")
        else:
            print("⚠️ Client OpenAI non créé")
            
        app_state.session_start = datetime.now()
        return f"✅ Client OpenAI configuré avec la clé sk-...{api_key[-8:]}", "🟢 Configuré"
    except Exception as e:
        print(f"❌ Erreur lors de la création du client OpenAI : {e}")
        return f"❌ Erreur lors de la configuration : {str(e)}", "🔴 Erreur"


def detect_youtube_url(text):
    """Détecte si le texte contient une URL YouTube"""
    youtube_pattern = r"(https?://)?(www\.)?(youtube\.com/watch\?v=|youtu\.be/)[\w-]+"
    return bool(re.search(youtube_pattern, text))


def format_user_prompt(user_input):
    """Formate le prompt utilisateur avec des instructions contextuelles"""
    if detect_youtube_url(user_input):
        app_state.current_video = user_input
        return f"""Nouvelle vidéo YouTube à analyser : {user_input}

IMPORTANT : Utilise IMMÉDIATEMENT l'outil fetch_youtube_transcript avec cette URL pour récupérer la transcription.

Instructions spéciales :
1. Récupère d'abord la transcription avec l'outil fetch_youtube_transcript
2. Fais une analyse initiale rapide
3. Pose-moi 2-3 questions pertinentes pour approfondir
4. Sois proactif et engage la conversation !"""
    else:
        return user_input


async def chat_with_agent(message, history):
    """Fonction principale pour chatter avec l'IA OpenAI"""
    if not app_state.openai_client:
        error_msg = "❌ Veuillez d'abord configurer votre clé API dans l'onglet Configuration."
        history.append([message, error_msg])
        yield history, ""
        return

    if not message.strip():
        yield history, ""
        return

    # Ajouter le message utilisateur à l'historique
    history.append([message, ""]) 

    # Vérifier si c'est une URL YouTube
    if detect_youtube_url(message):
        # Récupérer la transcription
        status_msg = "🔍 Récupération de la transcription YouTube en cours..."
        history[-1][1] = status_msg
        yield history, ""
        
        transcription = fetch_youtube_transcript(message)
        
        if transcription.startswith("❌") or transcription.startswith("⚠️"):
            error_msg = (
                "❌ Aucune transcription disponible pour cette vidéo.\n\n"
                "Pour continuer, choisissez une option :\n"
                "1) Collez ici la transcription ou les paroles ;\n"
                "2) Copiez/collez le titre et la description de la vidéo ;\n"
                "3) Donnez-moi les points clés que vous souhaitez traiter.\n\n"
                "Je reprendrai à partir de ces éléments — sans supposer quoi que ce soit tant que je n'ai pas de texte source."
            )
            history[-1][1] = error_msg
            yield history, ""
            return
        
        # Transcription réussie, analyser avec OpenAI
        success_msg = f"✅ Transcription récupérée ! ({len(transcription)} caractères)\n\nAnalyse en cours..."
        history[-1][1] = success_msg
        yield history, ""
        
        # Préparer le prompt pour OpenAI
        prompt = f"""Analyse cette transcription YouTube et réponds de manière utile :

TRANSCRIPTION :
{transcription[:2000]}...

Instructions :
1. Fais une analyse rapide des points clés
2. Pose 2-3 questions pertinentes pour approfondir
3. Sois proactif et engage la conversation

Réponse :"""
        
        try:
            response = app_state.openai_client.chat.completions.create(
                model="gpt-4o",
                messages=[{"role": "user", "content": prompt}],
                max_tokens=1000,
                temperature=0.7
            )
            
            ai_response = response.choices[0].message.content
            history[-1][1] = ai_response
            yield history, ""
            
        except Exception as e:
            error_msg = f"❌ Erreur lors de l'analyse : {str(e)}"
            history[-1][1] = error_msg
            yield history, ""
            
    else:
        # Question normale, répondre avec OpenAI
        try:
            response = app_state.openai_client.chat.completions.create(
                model="gpt-4o",
                messages=[{"role": "user", "content": message}],
                max_tokens=500,
                temperature=0.7
            )
            
            ai_response = response.choices[0].message.content
            history[-1][1] = ai_response
            yield history, ""
            
        except Exception as e:
            error_msg = f"❌ Erreur lors de la génération de réponse : {str(e)}"
            history[-1][1] = error_msg
            yield history, ""


def clear_conversation():
    """Efface l'historique de conversation"""
    app_state.conversation_history = []
    return []


def get_session_stats():
    """Retourne les statistiques de session"""
    if not app_state.session_start:
        return "📊 Aucune session active"

    duration = datetime.now() - app_state.session_start
    video_count = 1 if app_state.current_video else 0

    stats = f"""📊 **Statistiques de Session**
⏱️ Durée : {duration}
🎥 Vidéos analysées : {video_count}
🤖 Client OpenAI : {'✅ Actif' if app_state.openai_client else '❌ Non configuré'}
🔑 API : {'✅ Configurée' if app_state.api_key else '❌ Non configuré'}
"""

    if app_state.current_video:
        stats += f"📹 Vidéo actuelle : {app_state.current_video[:50]}..."

    return stats


# ---------------------------------------------------------------------
# Interface Gradio
# ---------------------------------------------------------------------

def create_interface():
    with gr.Blocks(
        title="🎬 YouTube Transcript Agent",
        theme=gr.themes.Soft(),
        css="""
        .gradio-container { max-width: 1200px !important; }
        .header-text { text-align: center; margin-bottom: 20px; }
        .config-box { background: #f8f9fa; padding: 15px; border-radius: 10px; margin: 10px 0; }
        """
    ) as app:

        # En-tête
        gr.HTML(
            """
        <div class="header-text">
            <h1 style="color: #2c3e50; font-size: 2.5em;">🎬 YouTube Transcript Agent</h1>
            <p style="color: #7f8c8d; font-size: 1.2em;">Analysez et discutez du contenu de vidéos YouTube avec une IA conversationnelle</p>
        </div>
            """
        )

        with gr.Tabs():
            # Onglet principal - Chat
            with gr.Tab("💬 Chat avec l'IA"):
                with gr.Row():
                    with gr.Column(scale=3):
                        chatbot = gr.Chatbot(
                            label="🤖 Conversation avec l'Agent YouTube",
                            height=500,
                            show_copy_button=True,
                            bubble_full_width=False,
                            avatar_images=("🧑", "🤖"),
                        )

                        with gr.Row():
                            msg_input = gr.Textbox(
                                label="💭 Votre message",
                                placeholder="Collez une URL YouTube ou posez une question...",
                                scale=4,
                                lines=2,
                            )
                            send_btn = gr.Button("📤 Envoyer", variant="primary", scale=1)

                        with gr.Row():
                            clear_btn = gr.Button("🗑️ Effacer chat", variant="secondary")
                            stats_btn = gr.Button("📊 Statistiques", variant="secondary")

                    with gr.Column(scale=1):
                        status_display = gr.Textbox(
                            label="📊 Statut",
                            value="🔴 Agent non configuré",
                            interactive=False,
                            lines=3,
                        )

                        stats_display = gr.Markdown(
                            value="📊 Configurez d'abord votre clé API",
                            label="📈 Statistiques",
                        )

            # Onglet configuration
            with gr.Tab("🔧 Configuration"):
                with gr.Row():
                    with gr.Column():
                        gr.HTML(
                            """
                        <div class="config-box">
                            <h3>🔑 Configuration de la Clé API OpenAI</h3>
                            <p>Obtenez votre clé API sur <a href="https://platform.openai.com/api-keys" target="_blank">platform.openai.com</a></p>
                        </div>
                            """
                        )

                        api_key_input = gr.Textbox(
                            label="🔐 Clé API OpenAI",
                            placeholder="sk-...",
                            type="password",
                            lines=1,
                        )

                        config_btn = gr.Button("✅ Configurer Agent", variant="primary", size="lg")
                        config_status = gr.Textbox(
                            label="📋 Statut de Configuration",
                            interactive=False,
                            lines=2,
                        )

            # Onglet aide
            with gr.Tab("❓ Aide"):
                gr.Markdown(
                    """
                # 🎯 Guide d'Utilisation

                ## 📋 Étapes pour commencer :
                1. **🔧 Configuration** : Allez dans l'onglet Configuration et entrez votre clé API OpenAI
                2. **💬 Chat** : Retournez à l'onglet Chat pour commencer à discuter
                3. **🎥 Analyse** : Collez une URL YouTube ou posez des questions

                ## 🚀 Fonctionnalités :
                - **🎬 Analyse de vidéos** : Collez n'importe quelle URL YouTube
                - **💭 Chat interactif** : Posez des questions sur le contenu
                - **⚡ Réponses en temps réel** : Streaming des réponses de l'IA
                - **🧠 Mémoire conversationnelle** : L'IA se souvient de vos échanges
                - **📊 Statistiques** : Suivez votre session d'analyse

                ## 💡 Exemples d'interactions :
                - "Analyse cette vidéo : https://youtube.com/watch?v=..."
                - "Résume-moi les points clés"
                - "Qu'est-ce qui est dit vers la 5ème minute ?"
                - "L'auteur mentionne-t-il [sujet] ?"
                - "Quelles sont les conclusions principales ?"

                ## 🔒 Sécurité :
                - Votre clé API n'est jamais sauvegardée
                - Elle reste privée pendant votre session
                - Aucune donnée n'est stockée de manière permanente
                """
                )

            # Nouvel onglet de test de transcription
            with gr.Tab("🧪 Test Transcription"):
                gr.HTML(
                    """
                    <div class="config-box">
                        <h3>🧪 Test Direct de la Transcription YouTube</h3>
                        <p>Testez directement la fonction de récupération de transcription sans passer par l'IA</p>
                    </div>
                    """
                )
                
                with gr.Row():
                    test_url_input = gr.Textbox(
                        label="🎬 URL YouTube à tester",
                        placeholder="https://www.youtube.com/watch?v=...",
                        lines=2,
                        value="https://www.youtube.com/watch?v=S38RcE-fp5g&t=48s&ab_channel=LeCoinStat"
                    )
                    test_btn = gr.Button("🧪 Tester Transcription", variant="primary", size="lg")
                
                test_result = gr.Textbox(
                    label="📋 Résultat du Test",
                    interactive=False,
                    lines=15,
                    placeholder="Le résultat du test de transcription apparaîtra ici..."
                )
                
                # Événement pour le test
                test_btn.click(fn=process_youtube_url, inputs=[test_url_input], outputs=[test_result])

        # Événements
        config_btn.click(fn=setup_agent, inputs=[api_key_input], outputs=[config_status, status_display])

        send_btn.click(fn=chat_with_agent, inputs=[msg_input, chatbot], outputs=[chatbot, msg_input])

        msg_input.submit(fn=chat_with_agent, inputs=[msg_input, chatbot], outputs=[chatbot, msg_input])

        clear_btn.click(fn=clear_conversation, outputs=[chatbot])

        stats_btn.click(fn=get_session_stats, outputs=[stats_display])

        # Exemples
        gr.Examples(
            examples=[
                ["Salut ! Peux-tu analyser cette vidéo pour moi ?"],
                ["https://www.youtube.com/watch?v=dQw4w9WgXcQ"],
                ["Résume-moi les points clés de cette vidéo"],
                ["Qu'est-ce qui est dit vers la 3ème minute ?"],
                ["L'auteur mentionne-t-il des exemples concrets ?"],
            ],
            inputs=[msg_input],
            label="💡 Exemples d'interactions",
        )

    return app


if __name__ == "__main__":
    # Créer et lancer l'application
    app = create_interface()

    # Configuration de lancement
    app.queue(default_concurrency_limit=5)  # Support multi-utilisateurs
    app.launch(
        server_name="0.0.0.0",  # Accessible depuis le réseau
        server_port=7860,        # Port standard
        share=True,              # Lien public temporaire
        show_error=True,         # Afficher les erreurs
        show_api=False,          # Cacher l'API documentation
        favicon_path=None,       # Pas d'icône personnalisée
        ssl_verify=False,        # Pour éviter les problèmes SSL
    )

    print("🚀 Application lancée !")
    print("🌐 Interface accessible sur http://localhost:7860")
    print("🔗 Lien public généré automatiquement pour le partage")
