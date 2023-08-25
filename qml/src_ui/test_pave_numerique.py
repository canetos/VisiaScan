import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtQml import *

class PaveNumerique(QObject):
    def __init__(self):
        super().__init__()
        self.password = ""

    @pyqtSlot(int)
    def addDigit(self, digit):
        self.password += str(digit)

    @pyqtSlot()
    def checkPassword(self):
        if self.password == "1111":
            print("Mot de passe correct !")
        else:
            print("Mot de passe incorrect !")
        self.password = ""

if __name__ == "__main__":
    app = QGuiApplication(sys.argv)
    engine = QQmlApplicationEngine()

    pave_numerique = PaveNumerique()
    engine.rootContext().setContextProperty("paveNumerique", pave_numerique)

    qml_file_pave_num = "qml/IHM_accueil.qml"
    engine.load(QUrl.fromLocalFile(qml_file_pave_num))

    sys.exit(app.exec_())
