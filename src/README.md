# Code de l'application streamlit 

## Lancer son dashboard en local

### Créer et activer l'environement python

Pour lancer une application Streamlit il faut avoir le package **streamlit** installé. Il peut être installé 
de façon globale mais le mieux est quand même de créer un environment **conda** avec les packages python que vous 
voulez utiliser en plus !

Pour aller plus vite, il est possible de créer un environment avec tous les packages utilisé pour créer le dashboard
du point geek en utilisant le fichier *environment.yaml*

```
bash
## Crée l'environement conda avec les packages utilisé pour le dashboard du tutoriel
conda env create --name <env-name> -f environment.yaml
```

### Lancer son dashboard 

```
bash
streamlit run app.py
```

Streamlit se lance par défaut sur le port **8051** - [Voir mon dashboard local](http://localhost:8051)

## Créer un layout pour son dashboard

## Ajouter de nouvelles pages

## Rendre son dashboard interactif

## Partager son dashboard avec d'autres personnes

### Déployer sur le service cloud de Streamlit

### Déployer sur une machine virtuelle
