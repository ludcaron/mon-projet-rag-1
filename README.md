# Mon Projet RAG

## Description
Mon Projet RAG est une application qui utilise l'apprentissage automatique pour analyser des données textuelles et PDF. Le projet inclut des fonctionnalités pour traiter des fichiers PDF et une interface web pour interagir avec les utilisateurs.

## Structure du projet
```
mon-projet-rag
├── data
│   ├── exemple.txt        # Fichier texte utilisé pour l'analyse
│   └── sample.pdf         # Document PDF d'exemple à traiter
├── src
│   ├── main.py            # Point d'entrée de l'application
│   ├── pdf_processing.py   # Traitement des fichiers PDF
│   ├── web_interface.py    # Interface web de l'application
│   └── utils
│       └── helpers.py      # Fonctions utilitaires
├── requirements.txt        # Dépendances du projet
├── README.md               # Documentation du projet
└── templates
    └── index.html         # Modèle HTML pour l'interface web
```

## Installation
1. Clonez le dépôt :
   ```
   git clone <URL_DU_DEPOT>
   cd mon-projet-rag
   ```

2. Installez les dépendances :
   ```
   pip install -r requirements.txt
   ```

## Utilisation
Pour démarrer l'application, exécutez le fichier `main.py` :
```
python src/main.py
```

Accédez à l'interface web via votre navigateur à l'adresse `http://127.0.0.1:5000`.

## Fonctionnalités
- Traitement de fichiers PDF pour extraire du texte et des données.
- Interface web pour visualiser les résultats et interagir avec l'application.
- Utilisation de l'apprentissage automatique pour améliorer l'analyse des données.

## Contribuer
Les contributions sont les bienvenues ! Veuillez soumettre une demande de tirage pour toute amélioration ou correction.