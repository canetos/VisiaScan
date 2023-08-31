#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtQuick import *
from PyQt5.QtQml import *

qml_file_reserve = r'appel_entre_fichier/main.qml'
qml_file_test = r'appel_entre_fichier\test_projet\TEST_main_defilement.qml'
qml_file = qml_file_reserve


def manager_data(self, eventData):
    if "<<<" in eventData:
        print("passez " + eventData)
        label_name = "pyLbSerach_Hab"
        # Va chercher le nom précédent = ""
        msg_name_hab = "Jean Luc"
        msg_number_app = "413"
        text_to_send = f" Contacte : {msg_name_hab} \nNum appartement :\n{msg_number_app} "
        self.transmit_textonQML(text_to_send, label_name)
            
    if ">>>" in eventData:
        print("passez " + eventData)
        label_name = "pyLbSerach_Hab"
        # Va chercher le nom suivant = msg
        msg_name_hab = "Jeanne d'Arc"
        msg_number_app = "413"
        text_to_send = f" Contacte : \n   {msg_name_hab} \nNum appartement :\n   {msg_number_app} "
        self.transmit_textonQML(text_to_send, label_name)

    if "pressmehandle" in eventData:
            print("passez ?")
            label_name = "pyLbl2"
            for i in range(1, 11):
                text_to_send = f"Texte depuis Python {i}"
                self.transmit_textonQML(text_to_send, label_name)
            text_to_send = f"troisième All send"
            self.transmit_textonQML(text_to_send, label_name)

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
    view.load(QUrl.fromLocalFile(qml_file))
    
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