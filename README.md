# VisiaScan
 Partie du projet en lien à l'interface de l'interphone pour notre projet de fin d'année

## Pour visualiser la partie ui, lancer :
### les instruction pour réaliser l'installation du projet
- le fichier requirements: 
Il permet de faire une installation des dépendances necéssaire au bon fonctionnement du projet, c'est un fichier requirements.txt aquis avec l'utilisation de la commande : pip freeze > requirements.txt

## Étapes à réaliser pour faire son éxecution finale

1. Cloner via l'URL du repository GitHub : git clone https://github.com/canetos/VisiaScan.git
2. Créez un environnement virtuel : python -m venv Venv_VisIA-scan
3. Activez l'environnement : 
    - mon_env\Scripts\activate (sous Windows)
    - source mon_env/bin/activate (sous Linux/macOS)
4. Installez les dépendances : pip install -r requirements.txt

### les fichier .py
- qml\src_ui\Show_picture_window.py : Il servira d'apparition pour le logo encore non réaliser du soft
- qml\src_ui\Show_load_window.py : Il servira à de chargement des données lors du lancement démarrage de l'interphone pour l'intervenant devant faire l'installation
- qml\src_ui\Show_app_window.py : Il servira comme lancement de l'interface , il pourra être à même d'avoir des évolutions dans le futurs

### les fichiers .py pour le developpeur :
- qml\src_ui\Show_Test_Defilement_window.py : Il sert au developpeur pour tester la partie défilement et de test des blocs internes au défilement.
