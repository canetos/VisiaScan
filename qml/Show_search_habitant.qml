import QtQuick 2.12
import QtQuick.Controls 2.15
import "Constants.js" as Constants

ApplicationWindow {
    visible: true
    width: Constants.demiscreenWidth
    height: Constants.demiscreenHeight
    title: "Pavé Numérique"
    
    flags: Qt.FramelessWindowHint | Qt.Window

    Rectangle {
        id: rectanglesous
        width: parent.width //500
        height: parent.height //370
        color: Constants.transparent

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
                    Text {
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


            /*
            Rectangle {
                id: rectanglec
                x: 81
                y: -102
                width: 130
                height: 50
                //color: btnPressed ? "#00558c" : "#ac0000"
                radius: 5

                property bool btnPressed: false

                Button {
                    anchors.fill: parent
                    onClicked: btnPressed = !btnPressed; // Inversion de l'état du bouton
                }

                Text {
                    //color: btnPressed ? "#007acc" : "#ff0000"
                    text: "C"
                    font.pixelSize: 40
                    horizontalAlignment: Text.AlignHCenter
                    verticalAlignment: Text.AlignVCenter
                    anchors.centerIn: parent
                }
            }
            */
            Rectangle {
                id: rectangle13
                x: 8
                y: 72
                width: 100
                height: 190
                color: "#007acc"
                radius: 5

                MouseArea {
                    anchors.fill: parent
                    //onPressed: parent.color = "#00558c" // Couleur plus foncée lors de l'appui
                    //onReleased: parent.color
                                = "#007acc" // Retour à la couleur standard lors du relâchement
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
}