import QtQuick 2.12
import QtQuick.Controls 2.15

Rectangle {
    width: 500
    height: 370
    color: "lightgreen"

    signal onClicked()

    Rectangle {
        id: rectangle13
        x: 10
        y: 10
        width: 130
        height: 50
        radius: 5

        property bool btnPressed: false

        MouseArea {
            anchors.fill: parent
            onClicked: event.sendEvent("C")
        }

        Text {
            text: "C"
            font.pixelSize: 40
            horizontalAlignment: Text.AlignHCenter
            verticalAlignment: Text.AlignVCenter
            anchors.centerIn: parent
        }
    }
}
