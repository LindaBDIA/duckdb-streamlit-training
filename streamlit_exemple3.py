import streamlit as st
import pandas as pd
import duckdb
import matplotlib.pyplot as plt

st.set_page_config(page_title="Analyse Titanic", layout="wide")

# Titre
st.title("🚢 Analyse des survivants du Titanic")

# Étape 1 : Charger les données depuis GitHub
CSV_URL = "https://raw.githubusercontent.com/atifrani/mgt_opl_env_dev/main/data/titanic.csv"

@st.cache_data
def load_data():
    df = pd.read_csv(CSV_URL)
    return df

df = load_data()

# Étape 2 : Stocker dans DuckDB (en mémoire ici)
con = duckdb.connect(database=':memory:')
con.register('titanic_df', df)

# Étape 3 : Ajouter une colonne 'age_group' pour regrouper les âges
con.execute("""
    SELECT *,
        CASE
            WHEN Age < 10 THEN '0-9'
            WHEN Age < 20 THEN '10-19'
            WHEN Age < 30 THEN '20-29'
            WHEN Age < 40 THEN '30-39'
            WHEN Age < 50 THEN '40-49'
            WHEN Age < 60 THEN '50-59'
            WHEN Age < 70 THEN '60-69'
            ELSE '70+'
        END AS age_group
    FROM titanic_df
""")
df_grouped = con.df()

# Étape 4 : Histogramme des survivants par catégorie d’âge
st.subheader("📊 Survivants par catégorie d’âge")

survivors_by_age_group = df_grouped[df_grouped['Survived'] == 1].groupby('age_group').size().reindex(
    ['0-9', '10-19', '20-29', '30-39', '40-49', '50-59', '60-69', '70+'], fill_value=0)

fig1, ax1 = plt.subplots()
survivors_by_age_group.plot(kind='bar', ax=ax1)
ax1.set_title("Nombre de survivants par tranche d’âge")
ax1.set_xlabel("Tranche d’âge")
ax1.set_ylabel("Nombre de survivants")
st.pyplot(fig1)

# Étape 5 : Camembert des survivants par sexe
st.subheader("🥧 Survivants par sexe")

survivors_by_sex = df_grouped[df_grouped['Survived'] == 1]['Sex'].value_counts()

fig2, ax2 = plt.subplots()
ax2.pie(survivors_by_sex, labels=survivors_by_sex.index, autopct='%1.1f%%', startangle=90)
ax2.set_title("Répartition des survivants par sexe")
st.pyplot(fig2)
