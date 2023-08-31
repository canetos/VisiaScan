#!/usr/bin/env python3
# coding: utf-8

import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtQuick import *
from PyQt5.QtQml import *

PICTURE_WINDOW_QML = "qml/picture_window.qml"

if __name__ == "__main__":
    app = QGuiApplication(sys.argv)
    view = QQmlApplicationEngine()
    view.load(QUrl.fromLocalFile(PICTURE_WINDOW_QML))
    sys.exit(app.exec_())