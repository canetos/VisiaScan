import QtQuick 2.12
import QtQuick.Controls 2.15

Rectangle {
    width: 500
    height: 370
    color: "lightgray"

    signal onClicked()

    Button {
        x: 40
        y: 20
        width: 200
        height: 100
        anchors.centerIn: parent
        text: "Grand Bouton"
        onClicked: backend.handleButtonPress("Bouton cliqué")
    }
}
