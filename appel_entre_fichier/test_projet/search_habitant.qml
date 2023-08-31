import QtQuick 2.12
import QtQuick.Controls 2.15
import "Constants.js" as Constants

Rectangle {
    width: 500
    height: 370
    color: "lightgreen"

    signal onClicked()

    Rectangle {
        id: rectanglemain1
        x: 10
        y: 11
        width: 482
        height: 337
        color: "#2b678f"
        radius: 5
        Rectangle {
            id: rectangle15
            x: 120
            y: 5
            width: parent.width / 2
            height: parent.height - 10
            color: "#007acc"
            radius: 5
            Rectangle {
                id: rectangle16
                x: 5
                y: 5
                width: parent.width - 10
                height: parent.height - 10
                color: "#000000"
                radius: 5
                Label {
                    width: parent.width
                    height: parent.height
                    color: "#ffffff"
                    text: "....."
                    font.pixelSize: 40
                    verticalAlignment: Text.Align
                    anchors.verticalCenterOffset: 0
                    anchors.horizontalCenterOffset: 0
                    anchors.centerIn: parent
                }
            }
        }

        Rectangle {
            id: rectangle13
            x: 8
            y: 72
            width: 100
            height: 190
            color: "#007acc"
            radius: 5

            Button {
                width: 200
                height: 100
                anchors.centerIn: parent
                text: "Grand Bouton copie"
                onClicked: backend.handleButtonPress("Bouton cliqué copy")
    }

            MouseArea {
                anchors.fill: parent
                //onPressed: parent.color = "#00558c" // Couleur plus foncée lors de l'appui
                //onReleased: parent.color = "#007acc" // Retour à la couleur standard lors du relâchement
            }

            Text {
                color: "#ffffff"
                text: "<<<"
                font.pixelSize: 40
                horizontalAlignment: Text.AlignHCenter
                verticalAlignment: Text.AlignVCenter
                anchors.centerIn: parent
            }
        }
        Rectangle {
            id: rectangle
            x: 374
            y: 72
            width: 100
            height: 190
            color: "#007acc"
            radius: 5

            MouseArea {
                anchors.fill: parent
                //onPressed: parent.color = "#00558c" // Couleur plus foncée lors de l'appui
                //onReleased: parent.color = "#007acc" // Retour à la couleur standard lors du relâchement
            }

            Text {
                color: "#ffffff"
                text: ">>>"
                font.pixelSize: 40
                horizontalAlignment: Text.AlignHCenter
                verticalAlignment: Text.AlignVCenter
                anchors.centerIn: parent
            }
        }
    }
}