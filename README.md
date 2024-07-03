
# API d'analyse de sentiments des avis clients

Cette application utilise FastAPI et Streamlit pour entraîner et utiliser un modèle d'analyse de sentiments des avis clients.

## Installation

1. Clonez le dépôt.
    ```sh
    git clone <URL_DU_DEPOT>
    cd <NOM_DU_DEPOT>
    ```

2. Installez les dépendances avec pipenv.
    ```sh
    pipenv install
    ```

## Utilisation

### Démarrage de l'API

Pour démarrer l'API, exécutez la commande suivante :
```sh
pipenv run uvicorn api:app --reload
```
ou
```sh
uvicorn api:app --reload
```

### Démarrage de l'application Streamlit

Pour démarrer l'application Streamlit, exécutez la commande suivante :
```sh
pipenv run streamlit run app.py
```
ou
```sh
streamlit run app.py
```

## Fonctionnalités

### Entraînement du modèle

1. Téléchargez un fichier CSV contenant les avis clients et leurs sentiments (colonnes `review` et `sentiment`).
2. Utilisez l'interface Streamlit pour télécharger le fichier CSV et entraîner le modèle.

### Prédiction des sentiments

1. Saisissez un avis client dans l'interface Streamlit.
2. Cliquez sur "Prédire" pour obtenir le sentiment prédit pour cet avis.

## Exemple de Fichier CSV

Le fichier CSV doit contenir deux colonnes : `review` et `sentiment`.

```csv
review,sentiment
"Le produit est génial !",positive
"Je n'aime pas ce produit",negative
"C'est un bon produit, mais il peut être amélioré.",neutral
"Le service client est très réactif et efficace.",positive
"Le produit est de mauvaise qualité et ne fonctionne pas.",negative
"Je suis très satisfait de mon achat.",positive
"C'est une perte de temps et d'argent.",negative
"Le design est élégant, mais la performance laisse à désirer.",neutral
"Excellent rapport qualité-prix.",positive
"Je ne recommande pas ce produit.",negative
```

## Dépendances

Ce projet utilise les dépendances suivantes :
- fastapi
- uvicorn
- streamlit
- pandas
- scikit-learn
- joblib
- nltk

Assurez-vous de les installer en utilisant `pipenv install` comme mentionné dans la section d'installation.

## Structure du Projet

```
.
├── api.py
├── app.py
├── functions.py
├── dataset.csv
├── Pipfile
├── Pipfile.lock
└── README.md
```

- `api.py` : Contient les endpoints de l'API pour entraîner le modèle et faire des prédictions.
- `app.py` : Contient l'application Streamlit pour l'interface utilisateur.
- `functions.py` : Contient les fonctions utilitaires, notamment pour le nettoyage des textes.
- `dataset.csv` : Exemple de fichier CSV contenant les avis clients.
- `Pipfile` et `Pipfile.lock` : Fichiers de gestion des dépendances.
- `README.md` : Ce fichier, décrivant le projet et son utilisation.

## Contributions

Les contributions sont les bienvenues ! Veuillez soumettre une pull request ou ouvrir une issue pour discuter de vos idées.

##

Ce projet est fait par les étudiants Marc-Antony NGOUARI, Franck Geoffroy SEKA et Melvin MARTINVALET.