import QtQuick 2.12
import QtQuick.Controls 2.15

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
                    id: lbSerach_Hab
                    objectName: 'pyLbSerach_Hab'
                    width: parent.width
                    height: parent.height
                    color: "#ffffff"
                    text: "Wait for your choice"
                    font.pixelSize: 20
                    verticalAlignment: Text.AlignVCenter
                    anchors.verticalCenterOffset: 0
                    anchors.horizontalCenterOffset: 0
                    anchors.centerIn: parent
                }
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
        }

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
    }
}   