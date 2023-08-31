#!/usr/bin/env python3
# coding: utf-8

import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtQuick import *
from PyQt5.QtQml import *

PICTURE_WINDOW_QML = "qml/Picture_window.qml"
LUNCH_WINDOW_QML = "qml/lunch_window.qml"
MAIN_WINDOW_QML = "qml/mainWindow.qml"
qml_file_bouton_num = r'qml/Show_pave_numerique.qml'
qml_file_bouton_hab = r'qml/Show_search_habitant.qml'
qml_file_bouton_IA= r'qml/lunch_IA.qml'


if __name__ == "__main__":
    app = QGuiApplication(sys.argv)
    view = QQmlApplicationEngine()
#    view.load(QUrl.fromLocalFile(PICTURE_WINDOW_QML))
#    view.load(QUrl.fromLocalFile(LUNCH_WINDOW_QML))
#    view.load(QUrl.fromLocalFile(MAIN_WINDOW_QML))
    view.load(QUrl.fromLocalFile(qml_file_bouton_num))
    view.load(QUrl.fromLocalFile(qml_file_bouton_hab))

    sys.exit(app.exec_())