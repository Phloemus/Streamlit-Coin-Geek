import streamlit as st
import datetime


## Set the configuration of the page 
st.set_page_config(
    page_title="Streamlit - Les bases",
    layout="centered",
    initial_sidebar_state="expanded"
)

st.title("Bienvenue au Coin Geek sur Streamlit !")

st.markdown("")

st.markdown(
        """
            ## Créer sa première application

            Pour créer une application streamlit, il suffit de créer un fichier python (ex: **app.py**)
            et importer le package **streamlit**. Ce package permet de faire de très nombreuses choses mais surtout 
            de pouvoir écrire sur la page web directement en utilisant des fonctions accessibles depuis l'objet 
            streamlit !
        """
)

st.markdown("")

st.info(
    """
        **app.py**

        Pour le tutoriel on va créer une application streamlit dans app.py que l'on modifiera au fur et à mesure que l'on avance dans le tutoriel
    """
)

st.code(
    """
        ## Créer app.py dans src
        cd src
        touch app.py
    """
)

st.markdown(
    """
        Importer le package Streamlit dans le fichier **app.py**
    """
)

st.code("import streamlit as st", language="python", line_numbers=False)

st.markdown("## Ajouter du contenu dans son application")

st.markdown(
        """
            ### Ecrire du texte

            Par exemple pour écrire du texte, il est possible d'utiliser la fonction **st.markdown** et d'y ajouter 
            une chaine de charactère en markdown dedans. 
        """
)

st.code(
        """
            import streamlit as st

            st.markdown("Bonjour, je suis du texte qui s'affiche sur le **dashboard**")
        """, 
    language="python", 
    line_numbers=False
)

st.markdown("""
                #### Résultat du code
            """
)

with st.expander("Résultat du code"):
    st.markdown("Bonjour, je suis du texte qui s'affiche sur le **dashboard**")

st.info(
        """
            En plus ce qui est pratique c'est que Streamlit interprête la chaine de caracètre comme du markdown ce qui veut dire
            qu'il est possible de mettre en *italique* ou en **gras**, d'ajouter des [liens](https://github.com/Phloemus/Streamlit-Coin-Geek) !
        """
)

st.markdown(
    """
        ## Partie 1 - Les composants interactifs

        Il y a plein de choses que l'on peut ajouter sur une application streamlit. 
        Des **bouttons**, des **champs à remplir**, des **checkbox**, etc..

        En voici un petit panel !
    """
)

colSelectors, colFields = st.columns(2)

with colSelectors:
    st.markdown("Les composants à cliquer")
    st.button("Click me !", type="primary")
    st.radio("Nom du gène",
    ["herg1", "aadA1", "aadA13"])
    st.select_slider(
    "Select a range of color wavelength",
    options=["red", "orange", "yellow", "green", "blue", "indigo", "violet"],
    value=("red", "blue"))

with colFields:
    st.markdown("Les composants à remplir")
    st.selectbox("Nom du gène",
    ("herg1", "aadA1", "aadA13"))
    st.text_input("Nom du gène", "aadA1")
    st.date_input("Date de l'analyse", datetime.date(2024, 7, 6))

with st.expander("Code des composants cliquables"):
    st.code(
        """
            ## Button        
            st.button("Click me !", type="primary")

            ## Boutton radio
            st.radio("Nom du gène",
            ["herg1", "aadA1", "aadA13"])

            ## Slider
            st.select_slider("Select a range of color wavelength",
                options=["red", "orange", "yellow", "green", "blue", "indigo", "violet"],
                value=("red", "blue"))
        """
    )


with st.expander("Code des composants à remplissables"):
    st.code(
        """
            ## Select box
            st.selectbox("Nom du gène", ("herg1", "aadA1", "aadA13"))

            ## Text input
            st.text_input("Nom du gène", "aadA1")

            ## Date input
            st.date_input("Date de l'analyse", datetime.date(2024, 7, 6))
        """
    )

st.info(
    """
        **Tous les composants de streamlit**

        Il y a une liste de tous les composants de streamlit dans la 
        [documentation](https://docs.streamlit.io/develop/api-reference)
    """
)

st.markdown(
        """
           ## Partie 2 - Les layouts

           Cette partie du tutoriel a pour but de comprendre comment positionner différents
           éléments sur un dashboard Streamlit. Le but est de manipuler les différents types de layouts 
           pour que le dashboard soit bien organisé
        """
)

st.markdown("")

st.markdown(
    """
        ### Changer la taille de la page

        De base, Streamlit affiche le contenu sur une petite partie de l'écran et centre le 
        contenu. C'est très joli pour écrire du texte ou de la documentation mais ça 
        représente une très grosse perte de place lorsqu'il s'agit de créer un dashboard :/

        Heureusement, il est possible de changer la taille prise par le contenu sur les pages
        en passant le paramètre **layout** à la fonction **set_page_config**
    """
)

st.code(
    """
        ## configuration de la page
        st.set_page_config(
            page_title="Streamlit - Les bases",
            layout="centered",
            initial_sidebar_state="expanded"
        )
    """
)

st.markdown(
        """
            ### Les colonnes

            La colonne est un layout qui permet de séparer son contenu en plusieurs
            parties distinctes côte à côte sur le dashboard.
        """
)

col1, col2 = st.columns(2)

with col1:
    st.markdown(
       """
            #### Colonne 1

            On peut imaginer que cette colonne puisse être utilisée pour y mettre
            des bouttons ou des champs à remplir 
       """
)

with col2:
    st.markdown(
       """
            #### Colonne 2

            Ici on pourrait y mettre un graphe ou une image par exemple
       """
)

with st.expander("Voir le code pour les colonnes"):
    st.code(
        """
            col1, col2 = st.columns(2)
            
            with col1:
                st.markdown(
                    '''#### Colonne 1
            
                        On peut imaginer que cette colonne puisse être utilisée pour y mettre
                        des bouttons ou des champs à remplir 
                   '''
            )
            
            with col2:
                st.markdown(
                   '''
                        #### Colonne 2
            
                        Ici on pourrait y mettre un graphe ou une image par exemple
                   '''
            )           
        """,
        language="python",
        line_numbers=False
    )

st.markdown(
    """
        Les colonnes peuvent avoir des tailles différentes en précisant la part de page 
        qui doit être utilisée par chaque colonne
    """
)

st.code(
    """
        ## la colonne du centre sera deux fois plus grande que les colonnes des extrémités
        col = st.columns((2, 4, 2), gap='medium')
    """
)

st.markdown(
        """
            ### Les tabs

            Les tabs permettent de d'afficher des éléments prenant tout l'écran en 
            fonction d'une catégorie sélectionnée. C'est pratique pour y naviguer
            facilement entre plusieurs informations. 

        """
)

tab1, tab2 = st.tabs(["tab 1", "code"])

with tab1:
    st.markdown(
       """
            #### Tab 1 

            Jusqu'à la fin du tutoriel je vais utiliser les tabs pour donner accès 
            au code pour chaque petite démo.

       """
)

with tab2:
    st.markdown("#### Code")
    st.code(
        """ 
            tab1, tab2 = st.tabs(["tab 1", "code"])
            
            with tab1:
                st.markdown(
                    '''
                        #### Tab 1 
            
                        Jusqu'à la fin du tutoriel je vais utiliser les tabs pour donner accès 
                        au code pour chaque petite démo.
            
                   '''
            )
            
            with tab2:
                st.code(
                    '''
                       code utilisé pour les tabs 
                    '''
            )           
        """
)

st.markdown(
    """
        ### Les popover

        Les popover sont des bouttons qui affichent une mini fenêtre avec laquelle 
        l'utilisateur peut interagir
    """
)

tabPopoverExample, tabPopoverCode = st.tabs(["Exemple popover", "Code popover"])

with tabPopoverExample:
    with st.popover("Click ici !"):
        st.markdown("Indiquer le nom d'un gène")
        genename = st.text_input("genename")

with tabPopoverCode:
   st.code(
        """
            with st.popover('Click ici !'):
                st.markdown('Indiquer le nom d'un gène')
                genename = st.text_input('genename')
        """
) 

st.markdown(
        """
            ### Sidebar

            Pour l'instant on a vu comment faire pour ajouter des éléments pour 
            créer des sous parties sur la page principale de l'application 
            streamlit. 

            La sidebar est la partie de l'interface ou que l'on peut ouvrir en 
            appuyant sur le boutton en haut à gauche de la page. 

            C'est possible de la customiser pour y ajouter les différentes pages
            de l'application. Pour un **dashboard** c'est un excellent endroit pour 
            ajouter des boutons et customiser la sidebar pour devenir le centre de
            contrôle de l'application. De cette façon toute la page peut afficher 
            des données, tableau et graphes tandis que la sidebar permet de gérer 
            ce qui est affiché sur la page.
        """
)

with st.sidebar:
    st.markdown("## Sidebar customisée")
    st.button("Click me")


with st.expander("Code de la sidebar"):
    st.code(
        """
            with st.sidebar:
                st.markdown("## Sidebar customisée")
                st.button("Click me")
        """,
        language="python"
    )

st.header("Partie manip - A vos clavier !")

st.markdown(
        """
            Ajouter du code python dans **app.py** pour 
            créer le layout d'un dashboard d'analyse de données avec 
            streamlit. Le résultat doit ressembler ressemblant à ceci:
        """
)

st.image("images/layout-manip.png", caption="manip-layout")

st.subheader("Tips")

st.markdown(
    """
        - Commencer par déterminer quel est le layout du dashboard
        - Utiliser les composants que l'on a vu dans cette page du tuto
    """
)

st.subheader("Code de la solution")

with st.expander("Proposition de correction"):
    st.code(
        """

# Import libraries
import streamlit as st
import pandas as pd

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

    with graphTabComparison:
        st.markdown("graphe comparaison")

with col[2]:
    st.header("Tableaux")
    st.markdown("Table content")


st.header("Description du dashboard")
st.markdown("")
st.markdown("Ce dashboard permet de suivre l'évolution de la population des départements français et de comparer leurs évolutions dans le temps")
       """,
        language="python",
        line_numbers=False
    )
