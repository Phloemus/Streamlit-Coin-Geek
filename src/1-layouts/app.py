import streamlit as st


st.title("Bienvenue au Coin Geek sur Streamlit !")

st.markdown("")

st.markdown(
        """
            ## Les bases

            Pour créer une application streamlit, il suffit de créer un fichier python (ex: **app.py**)
            et importer le package **streamlit**. Ce package permet de faire de très nombreuse choses mais surtout 
            de pouvoir écrire sur la page web directement en utilisant des fonctions accessibles depuis l'objet 
            streamlit !

            Admettons que l'on aie un fichier app.py et que l'on importe streamlit dedans

        """
)

st.code("import streamlit as st", language="python", line_numbers=False)

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

st.markdown("Bonjour, je suis du texte qui s'affiche sur le **dashboard**")

st.info(
        """
            En plus ce qui est pratique c'est que Streamlit interprête la chaine de caracètre comme du markdown ce qui veut dire
            qu'il est possible de mettre en *italique* et en **gras**, d'ajouter des [liens](https://github.com/Phloemus/Streamlit-Coin-Geek) !
        """
)

st.markdown(
        """
           ## Partie 1 - Les layouts

           Cette permière partie du tutoriel a pour but de comprendre comment positionner différents
           éléments sur un dashboard Streamlit. Le but est de manipuler les différents types de layouts 
           pour que le dashboard soit bien organisé
        """
)

st.markdown("")

st.info("Le code de ce dashboard et les tutoriels sont disponible sur la repo Github : https://github.com/Phloemus/Streamlit-Coin-Geek")


