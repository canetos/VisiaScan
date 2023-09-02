import QtQuick 2.12
import QtQuick.Controls 2.15
import "Constants.js" as Constants

Rectangle {
    width: 500
    height: 370
    color: "transparent"

    signal onClicked()

    Rectangle {
        id: rectanglemain1
        x: 10
        y: 11
        width: 482
        height: 307
        color: "#2b678f"
        radius: 5
        Rectangle {
            id: rectangle15
            x: 120
            y: 5
            width: parent.width / 2
            height: parent.height - 10
            color: "#004aac"
            radius: 5             
            RoundButton {
                id: myRoundButtonAppeladmin
                x: 5
                y: 5
                width: 230
                height: 50
                Text {
                    text: "Open Admin"
                    color: "#ffffff"
                    font.pixelSize: 16
                    horizontalAlignment: Text.AlignHCenter
                    verticalAlignment: Text.AlignVCenter
                    anchors.centerIn: parent
                }
                background: Rectangle {
                    radius: myRoundButtonAppeladmin.radius = 5
                    color: "#007acc"
                }
                onClicked:{ 
                    backend.handleButtonPress("Open_Admin")
                    inactivityTimer.restart()
                }
            }
/*
            RoundButton {
            id: myRoundButtonsuivant
            x: 374
            y: 72
            width: 100
            height: 190
                Text {
                    text: ">>>"
                    color: "#ffffff"
                    font.pixelSize: 35
                    horizontalAlignment: Text.AlignHCenter
                    verticalAlignment: Text.AlignVCenter
                    anchors.centerIn: parent
                }
                background: Rectangle {
                    radius: myRoundButtonsuivant.radius = 5
                    color: "#007acc"
                }
                onClicked:{ 
                    backend.handleButtonPress(">>>")
                    inactivityTimer.restart()
                }
            }

            RoundButton {
                id: myRoundButtonprecedent
                x: 8
                y: 72
                width: 100
                height: 190
                Text {
                    text: "<<<"
                    color: "#ffffff"
                    font.pixelSize: 35
                    horizontalAlignment: Text.AlignHCenter
                    verticalAlignment: Text.AlignVCenter
                    anchors.centerIn: parent
                }
                background: Rectangle {
                    radius: myRoundButtonprecedent.radius = 5
                    color: "#007acc"
                }
                onClicked: {
                    backend.handleButtonPress("<<<")
                    inactivityTimer.restart()
                }
            }*/
        }
    }
}   