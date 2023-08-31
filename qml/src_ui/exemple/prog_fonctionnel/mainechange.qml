import QtQuick 2.12
import QtQuick.Controls 2.15

ApplicationWindow {
    title: "Test"
    width: 400
    height: 300

    Column {
        anchors.fill: parent
        spacing: 10

        Label {
            id: lbl1
            objectName: 'pyLbl1'
            text: "texte provenant du fichier qml"
        }

        Label {
            id: lbl2
            objectName: 'pyLbl2'
            text: "unset"
        }


        Button {
            text: 'pressme'
            onClicked: {
                py_mainapp.foo('Second texte provenant du fichier qml')
            }
        }
    }
}