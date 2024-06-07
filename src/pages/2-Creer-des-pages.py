import streamlit as st


## Set the configuration of the page 
st.set_page_config(
    page_title="Streamlit - Multi pages",
    layout="centered",
    initial_sidebar_state="expanded"
)

st.title("Créer plusieurs pages différentes pour son dashboard")

st.markdown("")

st.markdown(
    """
        Streamlit est adapté pour créer de petites applications, donc c'est possible d'ajouter plusieurs pages 
        différentes dans la dashboard. Dans cette section on va apprendre à intégrer plusieurs pages dans une 
        application Streamlit
    """
)

st.header("Structure d'une application streamlit")

st.markdown(
    """
        Pour l'instant, la seule chose que l'on a faite était de coder dans le fichier principal de l'application. 
        Il s'agit de la page principale, utilisée pour lancer l'application Streamlit. 
    """
)

st.markdown(
    """
        Pour ajouter de nouvelles pages, il faut créer un dossier **pages** dans le même dossier que celui où se
        trouve la page principale de l'application
    """
)

tab1, tab2 = st.tabs(["Une seule page", "Plusieurs pages"])

with tab1:
    st.markdown(
        """
            - app.py
            - environment.yaml
        """
    )

with tab2:
    st.markdown(
        """
            - pages/
                - page1.py
                - page2.py
                - page3.py
            - app.py
            - environment.yaml
        """
    )

st.markdown(
    """
        Le nom des pages est le même que le nom des fichiers. Par exemple: page1.py s'affichera page1 dans 
        la barre de navigation. Aussi les pages s'affichent dans l'ordre alphabetique mais il est possible de
        contraindre l'ordre des pages en les nommant avec un chiffre au début. Par exemple, la page 1-Bases.py 
        s'affichera au dessus de la page 2-Avance.py dans la sidebar !
    """
)

st.markdown(
    """
        Pour le dashboard que l'on crée dans ce tutoriel, on ne va pas utiliser plusieurs pages. Par contre 
        l'application que vous êtes en train de consulter contient plusieurs pages, et même le dashboard que 
        l'on va créer à la fin du tutoriel !!
    """
)
