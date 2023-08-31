import QtQuick 2.12
import QtQuick.Controls 2.15

Rectangle {
    width: 500
    height: 370
    color: "lightgreen"

    signal onClicked()

    Column {
        anchors.centerIn: parent
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
            id : pressmehandle
            text: 'pressmehandle'
            property string text_all : text + ',Second texte provenant du fichier qml'
            onClicked : backend.handleButtonPress(text_all)
        }

        Button {
            id : pressmesend
            text: 'pressmesend'
            onClicked : backend.handleButtonPress('Second texte provenant du fichier qml')
        }
    }
}

/*
    property string clickText: "" // Propriété pour stocker le texte du clic

    Text {
        width: parent.width - 40
        height: parent.height - 40
        anchors.centerIn: parent
        font.pixelSize: 14
        text: clickText // Afficher le texte du clic
    }
}*/
