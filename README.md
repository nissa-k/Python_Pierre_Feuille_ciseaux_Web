#  Pierre - Feuille - Ciseaux - Version Web 

##  Description du Projet

Ce projet est une adaptation web du célèbre jeu **Pierre - Feuille - Ciseaux**, développé en **Python** avec le framework **Flask**. Affrontez l'ordinateur dans des parties palpitantes avec une interface moderne et intuitive !

##  Fonctionnalités

-  **Choix interactif** : Pierre, Feuille ou Ciseaux en un clic
-  **Adversaire IA** : L'ordinateur joue de façon aléatoire et intelligente
-  **Système de combat** :
  - Pierre bat Ciseaux
  - Feuille bat Pierre  
  - Ciseaux bat Feuille
-  **Parties en plusieurs manches** : Choisissez le nombre de manches 
-  **Suivi des scores** : Visualisation en temps réel des points
-  **Interface moderne** : Design responsive avec animations fluides
-  **Multi-plateforme** : Compatible desktop, tablette et mobile

##  Installation et Lancement

### Prérequis
- Python 3.7 ou supérieur
- Pip (gestionnaire de packages Python)

###  Installation

1. **Clonez le projet** :
```bash
git clone https://github.com/votre-repo/pierre-feuille-ciseaux-web.git

```

2. **Installez les dépendances** :
```bash
pip install flask
```

###  Lancement de l'Application

1. **Démarrez le serveur** :
modifier le lien avec votre chemain dossier : "C:/Users/karab/OneDrive/Desktop/ynov/Python_Pierre_Feuille_ciseaux_Web"
```bash
cd back
python server.py
```

2. **Accédez à l'application** :
Ouvrez votre navigateur et rendez-vous à l'adresse :
```
http://127.0.0.1:8080 (deja indiqué dans la console)
```

## 🎮 Comment Jouer ?

1. **Démarrage** : Cliquez sur "Jouer" depuis le menu principal
2. **Configuration** : 
   - Entrez votre nom
   - Choisissez le nombre de manches
3. **Jouez** : Sélectionnez Pierre, Feuille ou Ciseaux à chaque tour
4. **Suivi** : Observez les scores se mettre à jour en direct
5. **Résultat** : Découvrez le vainqueur à la fin de la partie !

##  Structure du Projet

python_pierre_feuille_ciseaux_web/
│
├python_pierre_feuille_ciseaux_web/
│
├── back/
│   └── src/
│       │
│       ├── game_utilities/
│       │   ├── __pycache__/
│       │   ├── __init__.py
│       │   ├── choice.py
│       │   └── score.py
│       │
│       ├── gaming/
│       │   ├── __pycache__/
│       │   ├── __init__.py
│       │   └── game.py
│       │
│       ├── info/
│       │   ├── __pycache__/
│       │   ├── __init__.py
│       │   └── info_bot.py
│       │
│       ├── rules/
│       │   ├── __pycache__/
│       │   ├── __init__.py
│       │   └── rules_game.py
│       │
│       └── server.py
│
├── static/
│   ├── infoBot.css
│   ├── jouer.css
│   ├── menu.css
│   └── rules.css
│
├── templates/
│   ├── infoBot.html
│   ├── jouer.html
│   ├── menu.html
│   └── rules.html
│
└── README.md


##  Design

- **Interface moderne** avec effets glassmorphism
- **Animations fluides** et interactives
- **Design responsive** s'adaptant à tous les écrans
- **Couleurs vibrantes** et visuellement attractives
- **Expérience utilisateur** optimisée

##  Technologies Utilisées

- **Backend** : Python, Flask
- **Frontend** : HTML5, CSS3 avec animations avancées
- **Stockage** : Sessions Flask pour la persistance des données
- **Responsive** : Media Queries CSS

##  Auteurs

karadag Nissa
Zemmar safaa


**Prêt à défier l'ordinateur ? **  
*Lancez le serveur et que le meilleur gagne !*
