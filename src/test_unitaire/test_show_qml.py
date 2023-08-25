#!/usr/bin/env python3
# coding: utf-8 / PEP 257

import sys
import asyncio
import time
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtQuick import *
from PyQt5.QtQml import *
import constants

class IHMManager(QObject):
    """Gère le chargement et la transition des IHM."""
    def __init__(self, view):
        super().__init__()
        self.view = view

    @pyqtSlot()
    def close_IHM(self):
        """Ferme la fenêtre IHM actuelle."""
        print("stop IHMmanager")
        self.view.rootObjects()[0].close()

    def close_current_window(self):
        """Ferme la fenêtre IHM actuelle."""
        if self.view.rootObjects():
            self.close_IHM()

    async def load_IHM(self):
        """Charge les IHM."""

        # Actuellement les fichiers sont executer en même temps
        await self.load_file(constants.PICTURE_WINDOW_QML,constants.Time_Show_Window.Time_Show_W1.value)  # Affichage immédiat
        await self.load_file(constants.LUNCH_WINDOW_QML,constants.Time_Show_Window.Time_Show_W2.value)  # Affichage immédiat
        await self.load_file(constants.MAIN_WINDOW_QML,constants.Time_Show_Window.Time_Show_W3.value)  # Affichage après 7 secondes


    async def load_file(self, file_path, delay_sec):
        """
        Charge un fichier QML avec un délai.
        :param file_path: Chemin vers le fichier QML.
        :param delay_sec: Délai en secondes avant de passer à la prochaine IHM.
        """
        if delay_sec > 0:
            time.sleep(delay_sec)
        print("Lancement : " + file_path,"Sleep : " + str(delay_sec))
        self.close_current_window()      
        await asyncio.to_thread(lambda: QMetaObject.invokeMethod(self.view, "load", Qt.QueuedConnection, Q_ARG(QUrl, QUrl.fromLocalFile(file_path))))

def launch_ihm(view):
    """
    Lance la partie IHM de l'application.
    :param view: La vue QQmlApplicationEngine.
    """
    loop = asyncio.get_event_loop()
    app_manager = IHMManager(view)
    loop.run_until_complete(app_manager.load_IHM())

def APP_main(view):
    """
    Fonction principale du programme.
    Initialise l'application PyQt et appelle la fonction pour lancer la partie IHM.
    """
    launch_ihm(view)
    #launch_backends()

def main():
    """
    Fonction principale du programme.
    Initialise l'application PyQt et appelle APP_main().
    """
    app = QGuiApplication(sys.argv)
    view = QQmlApplicationEngine()

    APP_main(view)  # Exécution de l'application

    sys.exit(app.exec_())

if __name__ == "__main__":
    asyncio.run(main())
