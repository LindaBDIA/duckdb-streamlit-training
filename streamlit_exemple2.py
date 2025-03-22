import streamlit as st
import pandas as pd
import plotly.express as px

# Titre de l'application
st.title("🛳️ Analyse des survivants - Dataset Titanic")

# Chargement du fichier CSV
uploaded_file = st.file_uploader("📂 Chargez votre fichier CSV", type="csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    st.markdown("✅ Données chargées avec succès !")

    # Nettoyage / préparation : suppression des âges manquants si besoin
    df = df.dropna(subset=['Age'])

    # ---------- Graphique 1 : Survivants par catégorie d’âge ----------
    st.subheader("📊 Survivants par tranche d’âge")

    # Créer des tranches d’âge
    bins = [0, 12, 18, 30, 45, 60, 100]
    labels = ['0-12', '13-18', '19-30', '31-45', '46-60', '60+']
    df['AgeGroup'] = pd.cut(df['Age'], bins=bins, labels=labels, right=False)

    # Grouper par AgeGroup et Survived
    age_survival = df.groupby(['AgeGroup', 'Survived']).size().reset_index(name='Count')
    age_survival['Survived'] = age_survival['Survived'].map({0: 'Non Survivants', 1: 'Survivants'})

    # Afficher le graphique
    fig_age = px.bar(
        age_survival,
        x='AgeGroup',
        y='Count',
        color='Survived',
        barmode='group',
        labels={'AgeGroup': 'Tranche d’âge', 'Count': 'Nombre de passagers'},
        title="🎂 Répartition des survivants selon l’âge"
    )
    st.plotly_chart(fig_age)

    # ---------- Graphique 2 : Survivants par sexe ----------
    st.subheader("📊 Survivants par sexe")

    sex_survival = df.groupby(['Sex', 'Survived']).size().reset_index(name='Count')
    sex_survival['Survived'] = sex_survival['Survived'].map({0: 'Non Survivants', 1: 'Survivants'})

    fig_sex = px.bar(
        sex_survival,
        x='Sex',
        y='Count',
        color='Survived',
        barmode='group',
        labels={'Sex': 'Sexe', 'Count': 'Nombre de passagers'},
        title="👥 Répartition des survivants selon le sexe"
    )
    st.plotly_chart(fig_sex)

else:
    st.info("📁 Veuillez charger un fichier CSV pour commencer l’analyse.")
