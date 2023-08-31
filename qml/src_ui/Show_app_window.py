#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
import logging
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtQuick import *
from PyQt5.QtQml import *

MAIN_WINDOW_QML = "qml/app_window.qml"

def manager_data(self, eventData):
    buttonText = eventData

    #Lancement de la reconnaissance facial
    if buttonText == "reco_IA":
        logging.debug("Lancement du programme de reconnaissance faciale")
        # Ici, lancez votre programme de reconnaissance faciale

    elif buttonText in ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "*", "#"):
        self.stored_values.append(buttonText)
        if buttonText in ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "*", "#"):
            # Envoyer la valeur "*" au "pylibTextpavenum"
            self.transmit_textonQML("*", "pylibTextpavenum")

    elif buttonText == "V":
        expected_sequence = ["#", "8", "4", "3", "*", "#"]
        if self.stored_values == expected_sequence:
            logging.debug("Séquence correcte")
        else:
            logging.debug("Séquence incorrecte")
        self.stored_values = []

    elif buttonText == "C":
        logging.debug("Effacement de la liste de valeurs")
        self.stored_values = []

    elif buttonText in ("Précédent", "Suivant"):
        logging.debug(f"État enregistré : {buttonText}")

    if "<<<" in eventData:
        print("passez " + eventData)
        label_name = "pyLbSerach_Hab"
        # Va chercher le nom précédent = ""
        msg_name_hab = "Jean Luc"
        msg_number_app = "413"
        text_to_send = f" Contacte : {msg_name_hab} \nNum appartement :\n{msg_number_app} "
        self.transmit_textonQML(text_to_send, label_name)
            
    elif ">>>" in eventData:
        print("passez " + eventData)
        label_name = "pyLbSerach_Hab"
        # Va chercher le nom suivant = msg
        msg_name_hab = "Jeanne d'Arc"
        msg_number_app = "413"
        text_to_send = f" Contacte : \n   {msg_name_hab} \nNum appartement :\n   {msg_number_app} "
        self.transmit_textonQML(text_to_send, label_name)

    else:
        print("Not pass : " + eventData)



class Backend(QObject):
    """Classe Backend pour gérer les interactions entre QML et Python."""

    def __init__(self):
        super().__init__()
        self.stored_values = []

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

    logging.basicConfig(level=logging.DEBUG)

    backend = Backend()
    view = QQmlApplicationEngine()
    context = view.rootContext()
    context.setContextProperty("backend", backend)
    view.load(QUrl.fromLocalFile(MAIN_WINDOW_QML))
    
    # Vérifier si le chargement a réussi
    if not view.rootObjects():
        sys.exit(-1)

    label_name = "pyLbl1"  # Remplacez ceci par le nom du QLabel QML
    text_retour = backend.receive_textonPYTHON(label_name)
    print("Texte reçu sur Python:", text_retour)

    label_name = "pyLbl2"  # Remplacez ceci par le nom du QLabel QML
    for i in range(1, 11):
        text_to_send = f"Texte depuis Python {i}"
        backend.transmit_textonQML(text_to_send, label_name)   
    text_to_send = f"All send"
    backend.transmit_textonQML(text_to_send, label_name)

    sys.exit(app.exec_())