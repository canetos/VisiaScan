import QtQuick 2.12
import QtQuick.Controls 2.15

Rectangle {
    width: 500
    height: 370
    color: "lightgreen"

    signal onClicked()

    Button {
        width: 200
        height: 100
        anchors.centerIn: parent
        text: "Grand Bouton copie"
        onClicked: backend.sendEvent("Bouton cliqué copy")
    }
}