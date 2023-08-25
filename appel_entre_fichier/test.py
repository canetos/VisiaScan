#!/usr/bin/env python3
# coding: utf-8

import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtQuick import *
from PyQt5.QtQml import *

# Chemin vers le fichier QML
qml_file = r'src_test_ui/main.qml'


class Backend(QObject):
    """Classe Backend pour gérer les interactions entre QML et Python."""

    # Signal pour indiquer qu'un événement s'est produit
    eventOccurred = pyqtSignal(str)

    @pyqtSlot(str)
    def sendEvent(self, eventData):
        """
        Méthode pour envoyer un événement depuis QML vers Python.

        Args:
            eventData (str): Les données de l'événement.
        """
        print(f"Événement reçu : {eventData}")
        self.eventOccurred.emit(eventData)

        # Mettre à jour les propriétés clickText dans les vues TexteView.qml et TexteViewcopy.qml
        context = view.rootContext()
        context.setContextProperty("clickText", eventData)

if __name__ == "__main__":
    app = QGuiApplication(sys.argv)

    backend = Backend()

    view = QQmlApplicationEngine()
    context = view.rootContext()
    context.setContextProperty("backend", backend)
    
    # Charger le fichier QML
    view.load(QUrl.fromLocalFile(qml_file))
    
    # Vérifier si le chargement a réussi
    if not view.rootObjects():
        sys.exit(-1)
      
    sys.exit(app.exec_())
