# Import libraries
import streamlit as st
import pandas as pd


# Get the dataset
df = pd.read_csv("data/fr-population-1999-2024.csv")

## Dataset formating
df.drop(columns=df.columns[3], inplace=True)
df = df.iloc[1:].reset_index(drop=True)
new_header = ['Numéro département', 'Nom département', '2024', '2021', '2015', '2010', '1999']
df.columns = new_header
df = df[df['Nom département'] != 'France métropolitaine']
df = df[df['Nom département'] != 'France']

# Page configuration
st.set_page_config(
    page_title="Population par département",
    layout="wide",
    initial_sidebar_state="expanded")

# Content of the page
st.title("Mon premier dashboard Streamlit")

st.markdown("")
st.info("Ce dashboard est correspond à ce [tutoriel officiel](https://github.com/Phloemus/Streamlit-Coin-Geek)")
st.markdown("")

# Dashboard Main Panel
col = st.columns((2, 4, 2), gap='medium')

with col[0]:
    st.markdown("")
    st.header("Recherche")
    department = st.selectbox(
        "Département",
        ("44 - Loire atlantique", "Other")
    )
    dataset = st.selectbox(
        "Nom du dataset",
        ("Population", "Custom")
    )
    st.markdown("")
    yearStart, yearEnd = st.select_slider(
        "Selectionner une date",
        options=["1999", "2010", "2015", "2021", "2024"],
        value=("1999", "2015"))
    st.button("Sélectionner", type="primary")

with col[1]:
    st.header("Graphes")
    graphTabEvolution, graphTabComparison = st.tabs(["Evolution", "Comparaison"])
    
    with graphTabEvolution:
        st.markdown("graphe evolution")
        dfEvolution = df[df['Nom département'] == 'Ain'] ## Problem : this is an empty dataframe..
        dfEvolution = dfEvolution.iloc[2:].reset_index(drop=True)
        print(dfEvolution)
        st.line_chart(dfEvolution)

    with graphTabComparison:
        st.markdown("graphe comparaison")

with col[2]:
    st.header("Tableaux")
    st.dataframe(df)    

st.header("Description du dashboard")
st.markdown("")
st.markdown("Ce dashboard permet de suivre l'évolution de la population des départements français et de comparer leurs évolutions dans le temps")
