qml_file = 'src_test_ui/prog_fonctionnel/mainechange.qml'
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtQml import QQmlApplicationEngine
from PyQt5.QtCore import QObject, pyqtSlot, QVariant

class MainApp(QObject):

    def __init__(self, context, parent=None):
        super(MainApp, self).__init__(parent)
        self.win = parent
        self.ctx = context

    @pyqtSlot(QVariant)
    def foo(self, aword):
        print('Reception des caractères : (%s)' % aword)
        o = self.win.findChild(QObject, 'pyLbl1')

        print('Texte depuis le label:', o.property("text"))  
        o = self.win.findChild(QObject, 'pyLbl2')
        o.setProperty("text", "Texte depuis Python")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    engine = QQmlApplicationEngine()
    ctx = engine.rootContext()
    engine.load(qml_file)
    win = engine.rootObjects()[0]
    py_mainapp = MainApp(ctx, win)
    ctx.setContextProperty("py_mainapp", py_mainapp)
    win.show()
    sys.exit(app.exec_())