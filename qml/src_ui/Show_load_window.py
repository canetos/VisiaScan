#!/usr/bin/env python3
# coding: utf-8

import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtQuick import *
from PyQt5.QtQml import *


LUNCH_WINDOW_QML = "qml/load_window.qml"

def manager_data(self, eventData):
    if "finishState" in eventData:
        print("Receipt of: " + eventData)
        label_name = "pyLbLoad_win"
        msg_name_event = eventData
        msg_validate = "OK"
        text_to_send = f"Final status of the label, {label_name} : {msg_name_event}{msg_validate} "
        print(text_to_send)
        self.transmit_textonQML(text_to_send, label_name)
    elif "Validate" in eventData:
        print("Receipt of : " + eventData)
        self.transmit_textonQML("", "pyLbLoad_win")
        QCoreApplication.quit()
    else:
        print(f"Not pass : {eventData}")



class Backend(QObject):
    """Classe Backend pour gérer les interactions entre QML et Python."""

    # Signal pour indiquer qu'un événement s'est produit
    eventOccurred = pyqtSignal(str)
    
    @pyqtSlot(str)
    def handleButtonPress(self, eventData):
        """
        Méthode pour gérer l'événement transmis par les boutons dans QML.

        Args:
            eventData (str): Les données de l'événement.
        """
        print(f"Événement reçu : {eventData}")
        self.eventOccurred.emit(eventData)

        manager_data(self, eventData)
        
    @pyqtSlot(str, result=str)
    def receive_textonPYTHON(self, label_name):
        """
        Méthode pour recevoir du texte depuis QML.

        Args:
            label_name (str): Le nom du QLabel dans QML.

        Returns:
            str: Le texte reçu.
        """
        o = view.rootObjects()[0].findChild(QObject, label_name)
        if o is not None:
            text = o.property("text")
            print(f"Texte reçu depuis QML : {text}")
            return text
        return ""

    @pyqtSlot(str, str)
    def transmit_textonQML(self, text, label_name):
        """
        Méthode pour transmettre du texte depuis Python et l'afficher dans un QLabel QML.

        Args:
            text (str): Le texte à afficher.
            label_name (str): Le nom du QLabel dans QML.
        """
        o = view.rootObjects()[0].findChild(QObject, label_name)
        if o is not None:
            o.setProperty("text", text)
            print(f"Texte transmis vers QML : {text}")

if __name__ == "__main__":
    app = QGuiApplication(sys.argv)
    backend = Backend()
    view = QQmlApplicationEngine()
    context = view.rootContext()
    context.setContextProperty("backend", backend)
    view.load(QUrl.fromLocalFile(LUNCH_WINDOW_QML))
    
    # Vérifier si le chargement a réussi
    if not view.rootObjects():
        print("Closing the application: loading failed.")
        sys.exit(-1)

    sys.exit(app.exec_())