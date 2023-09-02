#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
import logging
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtQuick import *
from PyQt5.QtQml import *

#from Open_Win_Admin import *

MAIN_WINDOW_QML = "qml/app_window.qml"

def Call_reco_Facial(self, eventData):
    logging.debug("Lancement du programme de reconnaissance faciale")
    # ICI l'appel de la fonctionnalité

def Manager_numeric_Keypad(self, eventData):
    if eventData in ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "*", "#"):
        self.stored_values.append(eventData)
        if eventData in ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "*", "#"):
            # Envoyer la valeur "*" au "pyLbNum_Keypad"
            num_stars = len(self.stored_values)
            stars_text = "*" * num_stars
            self.transmit_textonQML(stars_text, "pyLbNum_Keypad")

    elif eventData == "V":
        expected_sequence = ["1", "2", "3", "4", "*", "#"]
        if self.stored_values == expected_sequence:
            logging.debug("Séquence correcte")
            self.transmit_textonQML("The dor is open", "pyLbNum_Keypad")
        else:
            logging.debug("Séquence incorrecte")
            self.transmit_textonQML("", "pyLbNum_Keypad")
        self.stored_values = []

    elif eventData == "C":
        logging.debug("Effacement de la liste de valeurs")
        num_stars = len(self.stored_values)
        stars_text = "*" * num_stars
        self.transmit_textonQML(stars_text, "pyLbNum_Keypad")
        self.stored_values = []

    else : 
        print("Enter else : Manager_numeric_Keypad :" + eventData)

def manger_search_habitant(self, eventData):
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

    elif "Call the person" in eventData:
        print("passez " + eventData)
        label_name = "pyLbSerach_Hab"
        # Va chercher le nom suivant = msg
        msg_name_hab = "Jeanne d'Arc"
        msg_number_app = "413"
        text_to_send = f" Contacte : \n   {msg_name_hab} \nNum appartement :\n   {msg_number_app} "
        self.transmit_textonQML(text_to_send, label_name)

    else : 
        print("Enter else : manger_search_habitant :" + eventData)

def managerchangeswipeView(self, eventData):
    logging.debug(f"État enregistré : {eventData}")

    if "Button clicked Previous" in eventData:
        print("passez " + eventData)
        label_name = "pyLblnext"
        msg_name = "clicked Previous"
        text_to_send = f"{msg_name} "
        self.transmit_textonQML(text_to_send, label_name)

    elif "Button clicked Next" in eventData:
        print("passez " + eventData)
        label_name = "pyLblnext"
        msg_name = "clicked Next"
        text_to_send = f"{msg_name} "
        self.transmit_textonQML(text_to_send, label_name)

    else : 
        print("Enter else : managerchangeswipeView :" + eventData)

def Open_Win_Admin(self):
    pass #self.open_admin_page

def managerActivateAdmin(self, eventData):
    if "Open_Admin" in eventData:
            print("Receipt of: " + eventData)
            logging.debug("Lancement d'ouverture de la fenetre Admin")
            Open_Win_Admin(self)
    else : 
        print("Enter else : managerActivateAdmin :" + eventData)


def write_messages_to_file(word, file_path):
    if word and len(word.strip()) > 0:
        with open(file_path, "r") as file:
            lines = file.readlines()
            if word + "\n" not in lines:
                with open(file_path, "a") as append_file:
                    append_file.write(word + "\n")

def manager_data(self, eventData):

    # Utilisation d'un switch case pour gérer les différents cas
    switch = {
        "Reconnaissance_IA": Call_reco_Facial,
        "0": Manager_numeric_Keypad,
        "1": Manager_numeric_Keypad,
        "2": Manager_numeric_Keypad,
        "3": Manager_numeric_Keypad,
        "4": Manager_numeric_Keypad,
        "5": Manager_numeric_Keypad,
        "6": Manager_numeric_Keypad,
        "7": Manager_numeric_Keypad,
        "8": Manager_numeric_Keypad,
        "9": Manager_numeric_Keypad,
        "*": Manager_numeric_Keypad,
        "#": Manager_numeric_Keypad,
        "V": Manager_numeric_Keypad,
        "C": Manager_numeric_Keypad,
        "Call the person":manger_search_habitant,
        "<<<": manger_search_habitant,
        ">>>": manger_search_habitant,
        "Button clicked Previous": managerchangeswipeView,
        "Button clicked next": managerchangeswipeView,
        "Open_Admin" : managerActivateAdmin,
        #"Select_interface Menu":
        #"Select_interface Display Numeric keypad":
        #"Select_interface Display Search Hab":
    }

    # Vérifier si l'événement est présent dans le switch
    if eventData in switch:
        # Appeler la fonction associée à l'événement
        switch[eventData](self, eventData)
    else:
        print("Not pass : " + eventData)
        file_path = "Resultat_Test\Rendu_nom_bouton.txt"
        write_messages_to_file(eventData, file_path)


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