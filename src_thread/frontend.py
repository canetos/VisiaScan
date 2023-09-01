import logging
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtQuick import *
from PyQt5.QtQml import *
from constants import MAIN_WINDOW_QML

class FrontEnd(QObject):
    def __init__(self, main_app):
        super().__init__()
        self.main_app = main_app
        self.logger = main_app.logger

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

    def handle_ui_events(self):
        app = self.main_app.app
        backend = self.main_app.backend

        view = QQmlApplicationEngine()

        context = view.rootContext()
        context.setContextProperty("backend", backend)
        
        view.load(QUrl.fromLocalFile(MAIN_WINDOW_QML))
    
        if not view.rootObjects():
            self.logger.error("Failed to load QML file.")
            app.quit()
        
        app.exec_()
