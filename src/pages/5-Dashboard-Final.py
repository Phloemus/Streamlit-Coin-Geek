# Import libraries
import streamlit as st
import pandas as pd


# Get the dataset
df = pd.read_csv("data/fr-population-1999-2024.csv")

## Dataset formating
df.drop(columns=df.columns[3], inplace=True)
df = df.iloc[0:].reset_index(drop=True)
new_header = ['Numéro département', 'Nom département', '2024', '2021', '2015', '2010', '1999']
df.columns = new_header
df = df[df['Nom département'] != 'France métropolitaine']
df = df[df['Nom département'] != 'France']


############ Callbacks
def filterByDepartment(): 
    dfEvolution = df.loc[df["Nom département"] == st.session_state.department]
    dfEvolution = dfEvolution.drop(columns=["Numéro département", "Nom département"])
    st.session_state.dfGraph = dfEvolution

def filterByDate():
    print(st.session_state['dateRange'])
    

############## States ##################################################################
if 'department' not in st.session_state:
    st.session_state['department'] = 'Ain'

## if 'dateRange' not in st.session_state:
##    st.session_state['dateRange'] = ['1999', '2010', '2015']

if 'dfGraph' not in st.session_state:
    dfEvolution = df.loc[df["Nom département"] == 'Ain']
    dfEvolution = dfEvolution.drop(columns=["Numéro département", "Nom département"])
    st.session_state['dfGraph'] = dfEvolution

############# Content of the page ######################################################


# Page configuration
st.set_page_config(
    page_title="Population par département",
    layout="wide",
    initial_sidebar_state="expanded")

st.title("Mon premier dashboard Streamlit")

st.markdown("")
st.info("Ce dashboard est correspond à ce [tutoriel officiel](https://github.com/Phloemus/Streamlit-Coin-Geek)")
st.markdown("")

# Dashboard Main Panel
col = st.columns((2, 4, 2), gap='medium')

with col[0]:
    st.markdown("")
    st.header("Recherche")
    st.selectbox(
        "Département",
        df[["Nom département"]],
        key="department",
        on_change=filterByDepartment
    )
    dataset = st.selectbox(
        "Nom du dataset",
        ("Population", "Custom")
    )
    st.markdown("")
   ## st.select_slider(
   ##     "Selectionner une date",
   ##     options=["1999", "2010", "2015", "2021", "2024"],
   ##     value=("1999", "2015"),
   ##     key="dateRange",
   ##     on_change=filterByDate
   ## )

with col[1]:
    st.header("Graphes")
    graphTabLinePlot, graphTabBarPlot = st.tabs(["Line Plot", "Bar Plot"])
    
    with graphTabLinePlot:
        st.line_chart(st.session_state.dfGraph.transpose())

    with graphTabBarPlot:
        st.bar_chart(st.session_state.dfGraph.transpose())

with col[2]:
    st.header("Tableaux")
    st.dataframe(st.session_state.dfGraph)    
    st.dataframe(df)    

st.header("Description du dashboard")
st.markdown("")
st.markdown("Ce dashboard permet de suivre l'évolution de la population des départements français et de comparer leurs évolutions dans le temps")
