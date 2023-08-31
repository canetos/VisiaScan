
/*
This is a UI file (.ui.qml) that is intended to be edited in Qt Design Studio only.
It is supposed to be strictly declarative and only uses a subset of QML. If you edit
this file manually, you might introduce QML code that is not supported by Qt Design Studio.
Check out https://doc.qt.io/qtcreator/creator-quick-ui-forms.html for details on .ui.qml files.
*/
import QtQuick 6.5
import QtQuick.Controls 6.5
import QtQuick.Timeline 1.0
import IHM_Interphone

Rectangle {
    id: rectanglesous

    width: 500
    height: 370
    color: "Tansparent"

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
