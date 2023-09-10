#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
import time
import subprocess
import logging
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtQuick import *
from PyQt5.QtQml import *

import json
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
from facereco import FaceRecognitionWithIndication
from Open_Win_Admin import *

face_recognition = FaceRecognitionWithIndication.FaceRecognition()

MAIN_WINDOW_QML = "qml/app_window.qml"

def Call_reco_Facial(self, eventData):
     logging.debug("Lancement du programme de reconnaissance faciale")
    if face_recognition.recognize_faces():
        print("personne connue")
    else:
        print("personne non connue")

def Manager_numeric_Keypad(self, eventData):
    if eventData in ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "*", "#"):
        self.stored_values.append(eventData)
        if eventData in ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "*", "#"):
            # Envoyer la valeur "*" au "pyLbNum_Keypad"
            num_stars = len(self.stored_values)
            stars_text = "*" * num_stars
            self.transmit_textonQML(stars_text, "pyLbNum_Keypad")

    elif eventData == "V":
        expected_sequence = ["1", "2", "3", "4", "*"]
        if self.stored_values == expected_sequence:
            logging.debug("Séquence correcte")
            self.transmit_textonQML("The door is open", "pyLbNum_Keypad")
            self.transmit_textonQML("Waiting code PIN", "pyLbNum_Keypad")

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

def update_name_display(self):
    registered_names = list(face_recognition.house_administrator_dict.keys())

    if not registered_names:
        name: str = "No names registered"
        return name
    current_name = registered_names[face_recognition.current_name_index]
    # Remove any digits at the end of the name (if any)
    current_name = ''.join(filter(lambda x: not x.isdigit(), current_name))
    # Replace underscores with spaces
    msg_name = current_name.replace("_", " ")
    msg_appt = msg_name.rsplit(' ', 1)[-1]
    msg_name_hab = msg_name.rsplit(' ', 1)[0]

    return msg_name_hab, msg_appt


def manger_search_habitant(self, eventData):
    if "<<<" in eventData:
        if face_recognition.current_name_index == 0:
            pass
        else:
            face_recognition.current_name_index += 1
        print("passez " + eventData)
        label_name = "pyLbSerach_Hab"
        # Va chercher le nom précédent = ""
        msg_name = update_name_display(self)
        msg_name_hab = msg_name[0]
        msg_number_app = msg_name[1]
        text_to_send = f" Contacte : {msg_name_hab} \nNum appartement :\n{msg_number_app} "
        self.transmit_textonQML(text_to_send, label_name)

    elif ">>>" in eventData:
        print("passez " + eventData)
        face_recognition.current_name_index += 1
        label_name = "pyLbSerach_Hab"
        # Va chercher le nom suivant = msg
        msg_name = update_name_display(self)
        msg_name_hab = msg_name[0]
        msg_number_app = msg_name[1]
        text_to_send = f" Contacte : \n   {msg_name_hab} \nNum appartement :\n   {msg_number_app} "
        self.transmit_textonQML(text_to_send, label_name)
        if face_recognition.current_name_index == len(list(face_recognition.house_administrator_dict.keys())):
            face_recognition.current_name_index = 0

    elif "Call the person" in eventData:
        print("passez " + eventData)
        label_name = "pyLbSerach_Hab"
        # Va chercher le nom suivant = msg
        msg_name = update_name_display(self)
        msg_name_hab = msg_name[0]
        msg_number_app = msg_name[1]
        text_to_send = f" Contacte : \n   {msg_name_hab} \nNum appartement :\n   {msg_number_app} "
        self.transmit_textonQML(text_to_send, label_name)

    else:
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
    try:
        # Spécifiez le chemin absolu ou relatif du script Win_Admin.py
        script_path = r'qml\src_ui\Win_Admin.py'

        # Exécutez le script avec l'environnement Python actuel
        print(f"Chemin complet : {script_path}")
        subprocess.Popen(["python", script_path])
    except Exception as e:
        print(f"Une erreur s'est produite : {e}")
    
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
    
    face_recognition = FaceRecognitionWithIndication.FaceRecognition()


    logging.basicConfig(level=logging.DEBUG)

    backend = Backend()
    view = QQmlApplicationEngine()
    context = view.rootContext()
    context.setContextProperty("backend", backend)
    view.load(QUrl.fromLocalFile(MAIN_WINDOW_QML))
    
    # Vérifier si le chargement a réussi
    if not view.rootObjects():
        sys.exit(-1)

    sys.exit(app.exec_())