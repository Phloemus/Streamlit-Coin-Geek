import streamlit as st
import pandas as pd


## Set the configuration of the page 
st.set_page_config(
    page_title="Streamlit - Interactions",
    layout="centered",
    initial_sidebar_state="expanded"
)

st.title("Pouvoir interagir avec le dashboard")

st.markdown("")

st.markdown(
    """
        Avoir un petit coté interactif est essentiel pour que le dashboard puisse être utilisé par les biologistes. 
        Heureusement, streamlit propose une solution en python pour le faire !
    """
)

st.header("Les variables d'états (aka states)")

st.markdown(
    """
        Avec streamlit certaines variables peuvent être marquées comme étant des **variables d'état**. Streamlit 
        regarde en permanence le contenu de ces variables puis réaffiche la page si la valeur de l'une d'entre elle 
        a changé.
    """
)

st.header("Créer un compteur de click")

st.markdown(
    """
        L'illustration parfaite du concept d'état est le compteur de click. Le but est d'avoir in boutton qui incrémente
        un compteur à chaque fois que le bouton est cliqué.
    """
)
    
if 'count' not in st.session_state:
    st.session_state['count'] = 0

tabDemo, tabCode = st.tabs(["Demo compteur", "Code compteur"])

with tabDemo:
    increment = st.button('Increment')
    if increment:
        st.session_state['count'] += 1

    st.write('Count = ', st.session_state['count'])

with tabCode:
    st.code(
        """
            ## Ajout de la variable d'état
            if 'count' not in st.session_state:
                st.session_state['count'] = 0
            
            increment = st.button('Increment')
            if increment:
                st.session_state['count'] += 1
            
            st.write('Count = ', st.session_state['count'])
       """
    )


st.markdown("")

st.markdown(
    """
        Dans cet exemple, on ajoute une variable d'état au programme. Toutes les variables d'états de streamlit sont 
        rassemblées dans le dictionnaire **st.session_state**. 
    """
)

st.markdown("")

with st.expander("Le contenu de **session_state**"):
    st.write(st.session_state)

st.markdown("")

st.markdown(
    """
        Lorsque l'on modifie une variable d'état 
        (correspondant à une certaine clé dans **st.session_state**), tous les composants de la page utilisant cette 
        variables seront ré-affichés sur la page avec la nouvelle valeur de la variable d'état

        C'est comme ça que le compteur fonctionne. lorsque le boutton est cliqué, la variables increment devient vrai 
        temporairement ce qui augmentate la valeur de **st.session_state['count']** de 1

        Puis comme cette variable est une variable d'état, Streamlit regénère tous les composants ou elle est utilisée
    """
)

st.info("Les variables d'états fonctionne comme les **States** dans ReactJS")

st.markdown("")

st.header("Combiner les variables d'états avec les callbacks")

st.markdown(
    """
        Un callback est une fonction qui se déclanche après une action précise en lien avec un composant streamlit. 

        Par exemple, un **st.button** accepte un call back lorsqu'il est cliqué, il suffit d'indiquer au boutton 
        quelle fonction doit s'exécuter lorsqu'il est cliqué.

        Concrètement le code correspond à ça:
    """
)

tabCode2, tabDemo2 = st.tabs(["Code compteur callback", "Démo compteur callback"])

with tabCode2:
    st.code(
        """
            if 'count' not in st.session_state:
                    st.session_state['count'] = 0
    
            def incrementCount:
                st.session_state['count'] += 1
    
            st.button("Click me", on_click=incrementCount) 

            st.write("count: ", count)
        """
    )

with tabDemo2:
    if 'count' not in st.session_state:
        st.session_state['count'] = 0
    
    def incrementCount():
        st.session_state['count'] += 1
    
    st.button("Click me", on_click=incrementCount) 
    st.write("count: ", st.session_state['count'])

st.markdown(
    """
        Cette technique est très pratique puisqu'elle élimine le besoin la variable increment que l'on utilisait
        tout à l'heure pour conditionner l'incrémentation du compteur.
    """
)

st.warning(
    """
        **Attention à toujours avoir une clé par variable d'état !**

        Ici par exemple, les deux compteurs utilisent et incrémentent la même variable. Une incrémentation sur le 
        compteur de la démo 1 va aussi augmenter la valeur du compteur dans la démo 2 !!
    """
)

st.header("Lier les états aux composants interactifs")

st.markdown(
    """
        Le plus grand défi est de lier les états aux composants interactifs pour traquer les valeurs données
        par l'utilisateur du dashboard et modifier les données en fonction de ça.
    """
)

st.markdown(
    """
        Pour se faire il est possible de lier un composant avec une variable d'état spécifique. Lorsque la valeur du 
        composant change, la valeur de l'état aussi ce qui fait qui provoque un réaffichage de la page avec la nouvelle
        valeur écrite dans le composant.
    """
)

if 'name' not in st.session_state:
    st.session_state['name'] = ""

st.text_input("Enter your name", key="name")
st.write(st.session_state['name'])

st.code(
    """
        st.text_input("Your name", key="name")

        st.write(st.session_state['name'])
    """
)

st.subheader("Changer des données en fonction d'une option")

st.markdown("Voici un autre petit exemple. Cette fois ci pour modifier l'affichage d'un tableau selon l'option selectionnée")

# Combined data in a single DataFrame
data = {
    'Option': ['Option 1', 'Option 1', 'Option 1', 
               'Option 2', 'Option 2', 'Option 2',
               'Option 3', 'Option 3', 'Option 3'],
    'Column A': [1, 2, 3, 4, 5, 6, 7, 8, 9],
    'Column B': ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']
}
df = pd.DataFrame(data)

# Callback function to update the filtered DataFrame
def update_table():
    st.session_state.filtered_df = df[df['Option'] == st.session_state.selected_option]

# Initialize session state for select box and filtered DataFrame
if 'selected_option' not in st.session_state:
    st.session_state.selected_option = 'Option 1'
    st.session_state.filtered_df = df[df['Option'] == 'Option 1']

# Select box to choose data option
selected_option = st.selectbox("Choose an option:", df['Option'].unique(), key='selected_option', on_change=update_table)

# Display the filtered table
st.table(st.session_state.filtered_df)

with st.expander("Code du tableau qui bouge"):
   st.code(
        """
            # Combined data in a single DataFrame
            data = {
                'Option': ['Option 1', 'Option 1', 'Option 1', 
                           'Option 2', 'Option 2', 'Option 2',
                           'Option 3', 'Option 3', 'Option 3'],
                'Column A': [1, 2, 3, 4, 5, 6, 7, 8, 9],
                'Column B': ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']
            }
            df = pd.DataFrame(data)
            
            # Callback function to update the filtered DataFrame
            def update_table():
                st.session_state.filtered_df = df[df['Option'] == st.session_state.selected_option]
            
            # Initialize session state for select box and filtered DataFrame
            if 'selected_option' not in st.session_state:
                st.session_state.selected_option = 'Option 1'
                st.session_state.filtered_df = df[df['Option'] == 'Option 1']
            
            # Streamlit app
            st.title("Dynamic Table Based on Select Box with Callback")
            
            # Select box to choose data option
            selected_option = st.selectbox("Choose an option:", df['Option'].unique(), key='selected_option', on_change=update_table)
            
            # Display the filtered table
            st.table(st.session_state.filtered_df)
        """
    ) 

st.markdown("")

st.header("Partie pratique")

st.markdown(
    """
        On va compléter le code du dashboard précédant pour le rendre plus interactif. 

        Le but est de changer le formatage du dataframe utilisé par le graph en fonction des valeurs indiquées dans 
        les champs par l'utilisateur.
    """
)

st.markdown(
    """
        ### Récupérer et traiter les données

        D'abord, il faut récupérer les données jouet que l'on va manipuler. Les données sont dans **data/fr-population-1999-2024.csv**. 
        On va les charger un dataframe pandas, retirer les lignes et les colonnes qui ne nous interessent pas. 

        Le code si dessous traite les données comme il faut, copie colle le dans le fichier de ton dashboard.
    """
)

st.code(
    """
        # Get the dataset
        df = pd.read_csv("data/fr-population-1999-2024.csv")
        
        ## Dataset formating
        df.drop(columns=df.columns[3], inplace=True)
        df = df.iloc[0:].reset_index(drop=True)
        new_header = ['Numéro département', 'Nom département', '2024', '2021', '2015', '2010', '1999']
        df.columns = new_header
        df = df[df['Nom département'] != 'France métropolitaine']
        df = df[df['Nom département'] != 'France']
    """
)


st.markdown("""
        ### Créer les variables d'états

        Créer les variables d'états suivantes

        - department
        - dfGraph
    """
)

st.code(
    """
        ## Exemple pour rajouter une variable d'état
        if 'key' not in st.session_state:
            st.session_state['key'] = 0
    """
)

st.markdown(
    """
        ### Créer une fonction de formatage des données utilisée pour le graphe

        Formater les données avec une fonction callback qui servira de filtre pour avoir qu'une partie du dataframe
        au lieu du dataframe entier.
    """
)

with st.expander("Code fonction de formatage des données"):
    st.code(
        """
            def filterByDepartment(): 
                dfEvolution = df.loc[df["Nom département"] == st.session_state.department]
                dfEvolution = dfEvolution.drop(columns=["Numéro département", "Nom département"])
                st.session_state.dfGraph = dfEvolution
        """
    )

st.markdown(
    """
        ### Mapper les champs aux données

        Dans la partie 'Recherche' du dashboard, les champs remplissables doivent être en lien avec les données 
        présentes dans le dataframe. 
       """
)

st.markdown("")

colSelectBox, colYearSelect, colButton = st.columns(3)

with colSelectBox:
    st.markdown("#### Select box")
    st.selectbox("Selectionner une option", ("Loire Atlantique", "Bretagne", "..."))
    st.markdown(
        """

            Les selectbox on un attribut **options** qui représente les différentes options de sélection. Cet
            attribut prend un dataframe

            Select box a aussi un attribut **on_change** qui se déclanche lorsque l'option selectionnée est changée
        """
    )

with colYearSelect:
    st.markdown("#### Slider")
    st.select_slider("Select a range of color wavelength", options=["1999", "2010", "2015", "2021", "2024"], value=("2010", "2015"))
    st.markdown(
        """
            Select slider a des options, et aussi l'attribut **on_change** qui accept une fonction callback
        """
    )

with colButton:
    st.markdown("#### Boutton")
    st.button("Click me", type="primary")
    st.markdown("Le composant boutton à un attribut **on_click** qui accepte une fonction callback")
