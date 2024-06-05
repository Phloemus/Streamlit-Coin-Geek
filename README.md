<p align="center">
    <a href="https://streamlit.io" target="_blank" rel="noopener">
        <img src="https://raw.githubusercontent.com/Phloemus/Streamlit-Coin-Geek/main/img/cover.png" alt="Streamlit - Créer des dashboards web en python" />
    </a>
</p>


<p align="center">
    <em>Une présentation proposée par <a href="https://pf-bird.univ-nantes.fr/bn/">le réseau Bioinfo Nantais</a></em>
</p>

## Objectifs

L'objectif de ce tutoriel est d'apprendre à utiliser Streamlit pour créer des petites démo (dashboard) web. 
L'avantage d'un dashboard c'est qu'il s'agit d'une interface simple que les biologistes peuvent utiliser sans aucun 
problème. 

Streamlit rend le traitement des données biologique plus transparant pour les biologistes humide. Par exemple un 
dashboard Streamlit est excellent pour montrer des résultats d'analyse à son responsable de thèse. 

Malgré tous les avantage qu'offre Streamlit, c'est un outil encore méconnu de la communauté bioinfo. Dans ce coin geek
on va y remédier et apprendre à créer des dashboard web pour montrer ses données !

## Requirements

Pour bien suivre le tutoriel, il y a certains programmes qui sont nécéssaire d'avoir installé sur son ordinateur. 

- git
- conda
- python3

De préférence, utilisez plutôt Linux pour suivre le tutoriel. Sous windows, les étapes devraient être identiques, 
mais des erreurs de packages python peuvent tout de même subsister :/ 

> [!NOTE]
> Si vous rencontrez des difficultés à installer certains d'entre eux, n'hésitez pas à demander de l'aide sur le 
> [serveur mattermost](https://mattermost.univ-nantes.fr/bioinfosnantais/channels/town-square) du réseau BN 
> (c'est un endroit pratique pour demander de l'aide en cas de bloquage !)

## Mise en place de l'environement

Une application streamlit repose sur plusieurs packages pythons qu'il est pertinent de mettre dans un même 
environement conda. La liste des packages nécéssaire pour créer l'application démo du tutoriel est dans
le fichier **src/environment.yaml**.

La méthode la plus simple pour suivre le tutoriel est de cloner le répertoire github puis de créer un environment
conda avec le fichier **environment.yaml**

Cloner le répertoire github

```
bash 
git clone https://github.com/Phloemus/Streamlit-Coin-Geek.git
```

Créer un environement conda avec les packages nécéssaire pour le tutoriels

```
bash
conda create --name streamlit-coin-geek
source activate streamlit-coin-geek
conda env export > src/environment.yaml
```

Et voilà, maintenant il y un environment conda avec streamlit et tous les packages pour déployer l'application du 
tutoriel !

## Tutoriel

## Documentation officielle

## Canaux de discussion 
