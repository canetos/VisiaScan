import asyncio
from PyQt5.QtCore import QUrl
from PyQt5.QtQml import QQmlApplicationEngine
import constants

class MainApp:
    """
    Classe principale de l'application frontend.
    """
    def __init__(self, logger):
        self.engine = QQmlApplicationEngine()
        self.logger = logger
        self.visible_window  = None

    def load_window(self, qml_file):
        """
        Charger une fenêtre QML.

        Args:
            qml_file (str): Le chemin vers le fichier QML à charger.
        """
        
        # Fermer la fenêtre précédemment visible
        if self.visible_window :
            self.logger.debug("F - Window close")
            self.visible_window.close()  
        self.engine.load(QUrl(qml_file))
        self.logger.debug("F - Provenant du fichier : " + qml_file)
        self.visible_window  = self.engine.rootObjects()[0]
        self.visible_window .show()

class FrontEnd:
    """
    Classe pour la gestion de l'interface frontend.
    """
    def __init__(self, main_app):
        self.main_app = main_app
        self.logger = main_app.logger

    async def handle_ui_events(self):
        """
        Gérer les événements d'interface utilisateur de manière asynchrone.
        """
        self.logger.info("F - Process frontEnd")
        self.show_first_window()
        await self.wait_and_continue(1)
        self.show_second_window()
        await self.wait_and_continue(7)
        self.show_main_window()

    def show_first_window(self):
        """
        Afficher la première fenêtre d'interface utilisateur.
        """
        self.main_app.load_window(constants.PICTURE_WINDOW_QML)

    def show_second_window(self):
        """
        Afficher la seconde fenêtre d'interface utilisateur.
        """
        self.main_app.load_window(constants.LUNCH_WINDOW_QML)

    def show_main_window(self):
        """
        Afficher la fenêtre d'interface utilisateur principale.
        """
        self.main_app.load_window(constants.MAIN_WINDOW_QML)

    async def wait_and_continue(self, seconds):
        """
        Attendre un certain nombre de secondes et continuer.
        
        Args:
            seconds (int): Le nombre de secondes à attendre.
        """
        await asyncio.sleep(seconds)
        # Placeholder pour la validation de fin de chargement par le backend
        self.logger.debug("F - Process Sleep : " + str(seconds))
        await asyncio.sleep(0)  # Remplacer par le code réel de validation

async def frontEnd_process(logger):
    main_app = MainApp(logger)
    front = FrontEnd(main_app)
    await front.handle_ui_events()