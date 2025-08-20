import streamlit as st
import pandas as pd
import plotly.express as px
from streamlit_option_menu import option_menu
import json

# Configuration de la page
st.set_page_config(
    page_title="Data Reconversion Assistant - Demo",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Titre principal
st.title("🚀 Assistant de Reconversion Data - Version Démo")
st.markdown("**Transformez votre carrière avec l'intelligence artificielle et la data science**")

# Métiers data avec informations
METIERS_DATA = {
    "Data Analyst": {
        "description": "Analyse des données pour prendre des décisions business",
        "salaire_junior": "35k-45k€",
        "salaire_senior": "55k-75k€",
        "duree_formation": "3-6 mois",
        "niveau_difficulte": "Facile",
        "competences_requises": ["SQL", "Excel", "Python", "Tableau/PowerBI", "Statistiques"]
    },
    "Data Scientist": {
        "description": "Création de modèles prédictifs et d'algorithmes ML",
        "salaire_junior": "45k-60k€",
        "salaire_senior": "70k-100k€",
        "duree_formation": "6-12 mois",
        "niveau_difficulte": "Difficile",
        "competences_requises": ["Python", "Machine Learning", "Mathématiques", "SQL", "Deep Learning"]
    },
    "Data Engineer": {
        "description": "Construction et maintenance des infrastructures de données",
        "salaire_junior": "40k-55k€",
        "salaire_senior": "65k-90k€",
        "duree_formation": "6-9 mois",
        "niveau_difficulte": "Moyen",
        "competences_requises": ["Python", "SQL", "Cloud (AWS/Azure)", "Big Data", "DevOps"]
    },
    "Business Intelligence": {
        "description": "Création de tableaux de bord et rapports business",
        "salaire_junior": "35k-45k€",
        "salaire_senior": "55k-75k€",
        "duree_formation": "4-7 mois",
        "niveau_difficulte": "Facile",
        "competences_requises": ["SQL", "PowerBI/Tableau", "Excel", "Business", "SQL Server"]
    },
    "Machine Learning Engineer": {
        "description": "Déploiement et productionisation de modèles ML",
        "salaire_junior": "50k-65k€",
        "salaire_senior": "75k-110k€",
        "duree_formation": "8-12 mois",
        "niveau_difficulte": "Très difficile",
        "competences_requises": ["Python", "ML/DL", "DevOps", "Cloud", "Docker/Kubernetes"]
    }
}

# Navigation
selected = option_menu(
    menu_title=None,
    options=["🏠 Accueil", "🎯 Analyse Personnalisée", "📚 Ressources", "📊 Comparatif Métiers"],
    icons=["house", "target", "book", "graph-up"],
    orientation="horizontal",
)

if selected == "🏠 Accueil":
    st.header("Bienvenue dans votre parcours de reconversion Data !")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("""
        ### 🎯 **Pourquoi se reconvertir dans la Data ?**
        
        - **Croissance exponentielle** : Le marché de la data explose avec +40% de croissance annuelle
        - **Salaires attractifs** : Des rémunérations parmi les plus élevées du secteur tech
        - **Demande forte** : Plus de 200 000 postes à pourvoir en France d'ici 2025
        - **Évolution rapide** : Possibilité de progresser rapidement dans sa carrière
        
        ### 🚀 **Comment ça marche ?**
        
        1. **Renseignez votre profil** : Métier actuel et compétences
        2. **Recevez des recommandations** : Métiers data adaptés à votre profil
        3. **Obtenez un plan d'action** : Formation personnalisée et ressources
        4. **Suivez votre progression** : Objectifs et étapes claires
        """)
    
    with col2:
        st.info("""
        **💡 Conseil d'expert**
        
        Commencez par l'onglet "Analyse Personnalisée" pour recevoir vos recommandations personnalisées !
        """)
        
        st.metric("Métiers Data", "5", "disponibles")
        st.metric("Durée Formation", "3-12 mois", "selon le métier")
        st.metric("Salaire Moyen", "60k€", "+15% vs marché")

elif selected == "🎯 Analyse Personnalisée":
    st.header("🎯 Analyse Personnalisée de Votre Profil")
    
    # Formulaire de saisie
    with st.form("profile_form"):
        st.subheader("📝 Votre Profil Actuel")
        
        col1, col2 = st.columns(2)
        
        with col1:
            metier_actuel = st.text_input("Quel est votre métier actuel ?", placeholder="Ex: Commercial, Comptable, Enseignant...")
            secteur_actuel = st.selectbox("Dans quel secteur travaillez-vous ?", 
                                        ["Commerce/Retail", "Finance/Banque", "Santé", "Éducation", "Industrie", "Services", "Autre"])
        
        with col2:
            experience_annees = st.slider("Combien d'années d'expérience professionnelle ?", 0, 30, 5)
            niveau_etudes = st.selectbox("Niveau d'études", 
                                       ["Bac", "Bac+2", "Bac+3", "Bac+4", "Bac+5", "Doctorat"])
        
        st.subheader("🔧 Vos Compétences")
        
        competences_tech = st.multiselect(
            "Compétences techniques (si vous en avez)",
            ["Excel", "SQL", "Python", "R", "PowerBI", "Tableau", "JavaScript", "HTML/CSS", "Git", "Aucune"],
            default=["Aucune"]
        )
        
        competences_soft = st.multiselect(
            "Compétences transversales",
            ["Analyse", "Communication", "Gestion de projet", "Résolution de problèmes", "Travail en équipe", "Autonomie"],
            default=["Analyse", "Communication"]
        )
        
        motivation = st.selectbox(
            "Quelle est votre motivation principale ?",
            ["Changement de carrière", "Évolution dans mon domaine", "Intérêt pour la tech", "Salaire plus attractif", "Autre"]
        )
        
        temps_disponible = st.selectbox(
            "Temps disponible pour la formation",
            ["2-5h/semaine", "5-10h/semaine", "10-15h/semaine", "15h+/semaine"]
        )
        
        submitted = st.form_submit_button("🚀 Analyser Mon Profil")
    
    if submitted and metier_actuel:
        st.success("✅ Analyse terminée ! (Version démo)")
        
        # Analyse simulée basée sur les réponses
        st.subheader("🎯 Métiers Data Recommandés")
        
        # Logique simple de scoring
        scores = {}
        for metier, info in METIERS_DATA.items():
            score = 5  # Score de base
            
            # Bonus pour compétences techniques
            if "Python" in competences_tech:
                score += 2
            if "SQL" in competences_tech:
                score += 1
            if "Excel" in competences_tech:
                score += 1
            
            # Bonus pour compétences soft
            if "Analyse" in competences_soft:
                score += 1
            if "Communication" in competences_soft:
                score += 1
            
            # Bonus pour expérience
            if experience_annees > 5:
                score += 1
            
            # Bonus pour niveau d'études
            if "Bac+4" in niveau_etudes or "Bac+5" in niveau_etudes:
                score += 1
            
            scores[metier] = min(10, score)
        
        # Trier par score
        sorted_scores = sorted(scores.items(), key=lambda x: x[1], reverse=True)
        
        for metier, score in sorted_scores[:3]:
            with st.expander(f"{metier} - Score: {score}/10"):
                info = METIERS_DATA[metier]
                col1, col2, col3 = st.columns(3)
                
                with col1:
                    st.metric("Salaire Junior", info['salaire_junior'])
                    st.metric("Durée Formation", info['duree_formation'])
                
                with col2:
                    st.metric("Salaire Senior", info['salaire_senior'])
                    st.metric("Difficulté", info['niveau_difficulte'])
                
                with col3:
                    st.write("**Compétences requises :**")
                    for comp in info['competences_requises']:
                        st.write(f"• {comp}")
                
                st.write(f"**Description :** {info['description']}")
        
        # Analyse du profil
        st.subheader("📊 Analyse de Votre Profil")
        
        forces = []
        faiblesses = []
        
        if competences_tech and "Aucune" not in competences_tech:
            forces.append("Vous avez déjà des compétences techniques")
        else:
            faiblesses.append("Pas de compétences techniques préalables")
        
        if experience_annees > 3:
            forces.append(f"Expérience professionnelle solide ({experience_annees} ans)")
        else:
            faiblesses.append("Expérience professionnelle limitée")
        
        if "Analyse" in competences_soft:
            forces.append("Compétence d'analyse développée")
        
        if "Communication" in competences_soft:
            forces.append("Bonne communication")
        
        col1, col2 = st.columns(2)
        with col1:
            st.write("**✅ Vos Forces :**")
            for force in forces:
                st.write(f"• {force}")
        
        with col2:
            st.write("**⚠️ Points d'amélioration :**")
            for faiblesse in faiblesses:
                st.write(f"• {faiblesse}")
        
        # Plan de formation
        st.subheader("📚 Plan de Formation Personnalisé")
        
        if "Aucune" in competences_tech:
            st.write("**Phase 1 (Mois 1-2) :** Fondamentaux")
            st.write("• Apprentissage de Python de base")
            st.write("• Introduction à SQL")
            st.write("• Maîtrise d'Excel avancé")
        
        st.write("**Phase 2 (Mois 3-4) :** Spécialisation")
        st.write("• Formation spécifique au métier choisi")
        st.write("• Projets pratiques")
        st.write("• Outils de visualisation")
        
        st.write("**Phase 3 (Mois 5-6) :** Professionnalisation")
        st.write("• Portfolio de projets")
        st.write("• Préparation aux entretiens")
        st.write("• Networking et communauté")
        
        # Conseils
        st.subheader("💡 Conseils Personnalisés")
        
        if temps_disponible == "2-5h/semaine":
            st.write("• Privilégiez les formations en ligne flexibles")
            st.write("• Concentrez-vous sur un métier à la fois")
            st.write("• Prévoyez 6-12 mois pour la reconversion")
        
        elif temps_disponible == "15h+/semaine":
            st.write("• Vous pouvez accélérer votre formation")
            st.write("• Considérez des bootcamps intensifs")
            st.write("• Objectif : reconversion en 3-6 mois")
        
        st.write("• Créez un compte GitHub et partagez vos projets")
        st.write("• Rejoignez des communautés data sur LinkedIn")
        st.write("• Participez à des meetups et conférences")

elif selected == "📚 Ressources":
    st.header("📚 Ressources de Formation")
    
    tab1, tab2, tab3, tab4 = st.tabs(["🎓 Cours en Ligne", "📖 Documentation", "💻 Projets Pratiques", "🎯 Certifications"])
    
    with tab1:
        st.subheader("🎓 Plateformes de Cours en Ligne")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("""
            **🌐 Coursera**
            - Data Science Specialization (Johns Hopkins)
            - Machine Learning (Stanford)
            - Python for Everybody
            
            **📚 edX**
            - Data Science MicroMasters (UC San Diego)
            - Introduction to Python Programming
            - Data Analysis with Python
            """)
        
        with col2:
            st.markdown("""
            **🎯 Udemy**
            - Python for Data Science Bootcamp
            - SQL Bootcamp
            - Tableau A-Z
            
            **🚀 DataCamp**
            - Data Analyst with Python
            - Data Scientist with Python
            - Machine Learning Fundamentals
            """)
    
    with tab2:
        st.subheader("📖 Documentation et Références")
        
        st.markdown("""
        **🐍 Python**
        - [Documentation officielle Python](https://docs.python.org/)
        - [Pandas User Guide](https://pandas.pydata.org/docs/)
        - [NumPy Reference](https://numpy.org/doc/)
        
        **🗄️ SQL**
        - [SQL Tutorial](https://www.w3schools.com/sql/)
        - [PostgreSQL Documentation](https://www.postgresql.org/docs/)
        
        **📊 Visualisation**
        - [Matplotlib Tutorial](https://matplotlib.org/stable/tutorials/)
        - [Plotly Documentation](https://plotly.com/python/)
        - [Seaborn Guide](https://seaborn.pydata.org/tutorial.html)
        """)
    
    with tab3:
        st.subheader("💻 Projets Pratiques")
        
        st.markdown("""
        **🔍 Projets d'Analyse de Données**
        1. **Analyse des ventes e-commerce** : Utiliser des données de vente pour identifier les tendances
        2. **Prédiction de churn** : Analyser les données clients pour prédire le départ
        3. **Analyse de sentiment** : Classifier les avis clients avec NLP
        
        **📈 Projets de Machine Learning**
        1. **Prédiction de prix immobilier** : Régression linéaire sur des données immobilières
        2. **Classification d'images** : Reconnaissance de chiffres manuscrits (MNIST)
        3. **Recommandation de produits** : Système de recommandation collaboratif
        
        **🗄️ Projets de Data Engineering**
        1. **Pipeline ETL** : Extraction, transformation et chargement de données
        2. **Dashboard temps réel** : Visualisation de données en streaming
        3. **Data Lake** : Architecture de stockage de données
        """)
    
    with tab4:
        st.subheader("🎯 Certifications Reconnues")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("""
            **🔐 Microsoft**
            - Azure Data Scientist Associate
            - Azure Data Engineer Associate
            - Power BI Data Analyst
            
            **☁️ AWS**
            - AWS Certified Data Analytics
            - AWS Certified Machine Learning
            """)
        
        with col2:
            st.markdown("""
            **📊 Tableau**
            - Tableau Desktop Specialist
            - Tableau Desktop Certified Associate
            
            **🐍 Python Institute**
            - PCAP: Certified Associate in Python
            - PCPP: Certified Professional in Python
            """)

elif selected == "📊 Comparatif Métiers":
    st.header("📊 Comparatif des Métiers Data")
    
    # Création du DataFrame pour la visualisation
    df_metiers = pd.DataFrame([
        {
            "Métier": metier,
            "Salaire Junior (k€)": int(info["salaire_junior"].split("-")[0].replace("k", "")),
            "Salaire Senior (k€)": int(info["salaire_senior"].split("-")[0].replace("k", "")),
            "Durée Formation (mois)": int(info["duree_formation"].split("-")[0]),
            "Difficulté": info["niveau_difficulte"]
        }
        for metier, info in METIERS_DATA.items()
    ])
    
    # Graphiques comparatifs
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("💰 Comparaison des Salaires")
        fig_salaires = px.bar(
            df_metiers, 
            x="Métier", 
            y=["Salaire Junior (k€)", "Salaire Senior (k€)"],
            title="Évolution des Salaires par Métier",
            barmode="group"
        )
        fig_salaires.update_layout(height=400)
        st.plotly_chart(fig_salaires, use_container_width=True)
    
    with col2:
        st.subheader("⏱️ Durée de Formation")
        fig_formation = px.pie(
            df_metiers, 
            values="Durée Formation (mois)", 
            names="Métier",
            title="Répartition par Durée de Formation"
        )
        fig_formation.update_layout(height=400)
        st.plotly_chart(fig_formation, use_container_width=True)
    
    # Tableau détaillé
    st.subheader("📋 Détail des Métiers")
    
    for metier, info in METIERS_DATA.items():
        with st.expander(f"🔍 {metier}"):
            col1, col2, col3 = st.columns(3)
            
            with col1:
                st.metric("Salaire Junior", info['salaire_junior'])
                st.metric("Durée Formation", info['duree_formation'])
            
            with col2:
                st.metric("Salaire Senior", info['salaire_senior'])
                st.metric("Niveau Difficulté", info['niveau_difficulte'])
            
            with col3:
                st.write("**Compétences requises :**")
                for comp in info['competences_requises']:
                    st.write(f"• {comp}")
            
            st.write(f"**Description :** {info['description']}")

# Sidebar avec informations utiles
with st.sidebar:
    st.header("ℹ️ Informations Utiles")
    
    st.info("""
    **💡 Conseils de Reconversion**
    
    • Commencez par les bases (Python, SQL, Excel)
    • Pratiquez sur des projets concrets
    • Créez un portfolio GitHub
    • Rejoignez des communautés data
    • Restez à jour avec les tendances
    """)
    
    st.metric("💼 Postes Ouverts", "200k+", "en France")
    st.metric("📈 Croissance", "+40%", "par an")
    st.metric("💰 Salaire Moyen", "60k€", "secteur data")
    
    st.markdown("---")
    
    st.markdown("**🔗 Liens Utiles**")
    st.markdown("[LinkedIn Data Jobs](https://www.linkedin.com/jobs/data-science-jobs/)")
    st.markdown("[Meetup Data Science](https://www.meetup.com/fr-FR/topics/data-science/)")
    st.markdown("[Kaggle](https://www.kaggle.com/)")
    
    st.markdown("---")
    st.warning("⚠️ **Version Démo** - L'analyse IA n'est pas disponible. Utilisez la logique intégrée pour tester l'application.")

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #666;'>
    <p>🚀 <strong>Data Reconversion Assistant - Version Démo</strong> - Votre compagnon pour une carrière dans la data</p>
    <p>Développé avec Streamlit</p>
</div>
""", unsafe_allow_html=True)
