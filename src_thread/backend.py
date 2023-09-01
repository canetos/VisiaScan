
import logging
from PyQt5.QtCore import QObject, pyqtSignal, pyqtSlot
from constants import MAIN_WINDOW_QML

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

    def write_messages_to_file(self, word, file_path):
        if word and len(word.strip()) > 0:
            with open(file_path, "r") as file:
                lines = file.readlines()
                if word + "\n" not in lines:
                    with open(file_path, "a") as append_file:
                        append_file.write(word + "\n")

    def manager_data(self, eventData):
        switch = {
            "Reconnaissance_IA": self.Call_reco_Facial,
            "0": self.Manager_numeric_Keypad,
            "1": self.Manager_numeric_Keypad,
            "2": self.Manager_numeric_Keypad,
            "3": self.Manager_numeric_Keypad,
            "4": self.Manager_numeric_Keypad,
            "5": self.Manager_numeric_Keypad,
            "6": self.Manager_numeric_Keypad,
            "7": self.Manager_numeric_Keypad,
            "8": self.Manager_numeric_Keypad,
            "9": self.Manager_numeric_Keypad,
            "*": self.Manager_numeric_Keypad,
            "#": self.Manager_numeric_Keypad,
            "V": self.Manager_numeric_Keypad,
            "C": self.Manager_numeric_Keypad,
            "Call the person": self.manger_search_habitant,
            "<<<": self.manger_search_habitant,
            ">>>": self.manger_search_habitant,
            "Button clicked Previous": self.managerchangeswipeView,
            "Button clicked next": self.managerchangeswipeView,
        }

        if eventData in switch:
            switch[eventData](eventData)
        else:
            print("Not pass : " + eventData)
            file_path = "Resultat_Test\Rendu_nom_bouton.txt"
            self.write_messages_to_file(eventData, file_path)
