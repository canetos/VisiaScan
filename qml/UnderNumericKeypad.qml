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
        width: parent.width - 18 //482
        height: parent.height - 303 //67
        color: "#2b678f"
        radius: 5
        Rectangle {
            id: rectangle15
            x: 145
            y: 5
            width: parent.width / 2.5
            height: parent.height - 10
            color: "#007acc"
            radius: 5
            Rectangle {
                id: rectangleText
                x: 5
                y: 5
                width: parent.width - 10
                height: parent.height - 10
                color: "#000000"
                radius: 5
                Text {
                    id: lbNum_Keypad
                    objectName: 'pyLbNum_Keypad'
                    width: parent.width
                    height: parent.height
                    color: "#ffffff"
                    text: "Waiting code PIN"
                    font.pixelSize: 16
                    verticalAlignment: Text.AlignVCenter
                    anchors.verticalCenterOffset: 0
                    anchors.horizontalCenterOffset: 0
                    anchors.centerIn: parent
                }
            }
        }
        RoundButton {
            id: myRoundButtonC
            x: 10
            y: 10
            width: 130
            height: 50
            Text {
                text: "C"
                color: "#ff0000"
                font.pixelSize: 40
                horizontalAlignment: Text.AlignHCenter
                verticalAlignment: Text.AlignVCenter
                anchors.centerIn: parent
            }
            background: Rectangle {
                radius: myRoundButtonC.radius = 5
                color: "#ac0000"
            }
            onClicked: {
                backend.handleButtonPress("C")
                inactivityTimer.restart()
            }
        }
            
        RoundButton {
            id: myRoundButtonV
            x: 341
            y: 10
            width: 130
            height: 50
            Text {
                text: "V"
                color: "#00FF00"
                font.pixelSize: 40
                horizontalAlignment: Text.AlignHCenter
                verticalAlignment: Text.AlignVCenter
                anchors.centerIn: parent
            }
            background: Rectangle {
                radius: myRoundButtonC.radius = 5
                color: "#00ac7a"
            }
            onClicked: {
                backend.handleButtonPress("V")
                inactivityTimer.restart()
            }
        }
    }

    Rectangle {
        id: rectanglemain2
        x: 10
        y: 91
        width: 484
        height: 63
        color: "#2b678f"
        radius: 5

        RoundButton {
            id: myRoundButton1
            x: 10
            y: 10
            width: 130
            height: 45
            Text {
                text: "1"
                color: "#ffffff"
                font.pixelSize: 40
                horizontalAlignment: Text.AlignHCenter
                verticalAlignment: Text.AlignVCenter
                anchors.centerIn: parent
            }
            background: Rectangle {
                radius: myRoundButton1.radius = 5
                color: "#007acc"
            }
            onClicked: {
                backend.handleButtonPress("1")
                inactivityTimer.restart()
            }
        }

        RoundButton {
            id: myRoundButton2
            x: 177
            y: 10
            width: 130
            height: 45
            Text {
                text: "2"
                color: "#ffffff"
                font.pixelSize: 40
                horizontalAlignment: Text.AlignHCenter
                verticalAlignment: Text.AlignVCenter
                anchors.centerIn: parent
            }
            background: Rectangle {
                radius: myRoundButton2.radius = 5
                color: "#007acc"
            }
            onClicked: {
                backend.handleButtonPress("2")
                inactivityTimer.restart()
            }
        }

        RoundButton {
            id: myRoundButton3
            x: 341
            y: 10
            width: 130
            height: 45
            Text {
                text: "3"
                color: "#ffffff"
                font.pixelSize: 40
                horizontalAlignment: Text.AlignHCenter
                verticalAlignment: Text.AlignVCenter
                anchors.centerIn: parent
            }
            background: Rectangle {
                radius: myRoundButton3.radius = 5
                color: "#007acc"
            }
            onClicked: {
                backend.handleButtonPress("3")
                inactivityTimer.restart()
            }
        }
    }

    Rectangle {
        id: rectanglemain3
        x: 8
        y: 159
        width: 484
        height: 63
        color: "#2b678f"
        radius: 5
        RoundButton {
            id: myRoundButton4
            x: 10
            y: 10
            width: 130
            height: 45
            Text {
                text: "4"
                color: "#ffffff"
                font.pixelSize: 40
                horizontalAlignment: Text.AlignHCenter
                verticalAlignment: Text.AlignVCenter
                anchors.centerIn: parent
            }
            background: Rectangle {
                radius: myRoundButton4.radius = 5
                color: "#007acc"
            }
            onClicked: {
                backend.handleButtonPress("4")
                inactivityTimer.restart()
            }
        }

        RoundButton {
            id: myRoundButton5
            x: 177
            y: 10
            width: 130
            height: 45
            Text {
                text: "5"
                color: "#ffffff"
                font.pixelSize: 40
                horizontalAlignment: Text.AlignHCenter
                verticalAlignment: Text.AlignVCenter
                anchors.centerIn: parent
            }
            background: Rectangle {
                radius: myRoundButton5.radius = 5
                color: "#007acc"
            }
            onClicked: {
                backend.handleButtonPress("5")
                inactivityTimer.restart()
            }
        }

        RoundButton {
            id: myRoundButton6
            x: 341
            y: 10
            width: 130
            height: 45
            Text {
                text: "6"
                color: "#ffffff"
                font.pixelSize: 40
                horizontalAlignment: Text.AlignHCenter
                verticalAlignment: Text.AlignVCenter
                anchors.centerIn: parent
            }
            background: Rectangle {
                radius: myRoundButton6.radius = 5
                color: "#007acc"
            }
            onClicked: {
                backend.handleButtonPress("6")
                inactivityTimer.restart()
            }
        }
    }

    Rectangle {
        id: rectanglemain4
        x: 10
        y: 228
        width: 484
        height: 63
        color: "#2b678f"
        radius: 5

        RoundButton {
            id: myRoundButton7
            x: 10
            y: 10
            width: 130
            height: 45
            Text {
                text: "7"
                color: "#ffffff"
                font.pixelSize: 40
                horizontalAlignment: Text.AlignHCenter
                verticalAlignment: Text.AlignVCenter
                anchors.centerIn: parent
            }
            background: Rectangle {
                radius: myRoundButton7.radius = 5
                color: "#007acc"
            }
            onClicked: {
                backend.handleButtonPress("7")
                inactivityTimer.restart()
            }
        }

        RoundButton {
            id: myRoundButton8
            x: 177
            y: 10
            width: 130
            height: 45
            Text {
                text: "8"
                color: "#ffffff"
                font.pixelSize: 40
                horizontalAlignment: Text.AlignHCenter
                verticalAlignment: Text.AlignVCenter
                anchors.centerIn: parent
            }
            background: Rectangle {
                radius: myRoundButton8.radius = 5
                color: "#007acc"
            }
            onClicked: {
                backend.handleButtonPress("8")
                inactivityTimer.restart()
            }
        }

        RoundButton {
            id: myRoundButton9
            x: 341
            y: 10
            width: 130
            height: 45
            Text {
                text: "9"
                color: "#ffffff"
                font.pixelSize: 40
                horizontalAlignment: Text.AlignHCenter
                verticalAlignment: Text.AlignVCenter
                anchors.centerIn: parent
            }
            background: Rectangle {
                radius: myRoundButton9.radius = 5
                color: "#007acc"
            }
            onClicked: {
                backend.handleButtonPress("9")
                inactivityTimer.restart()
            }
        }   
    }

    Rectangle {
        id: rectanglemain5
        x: 10
        y: 297
        width: 484
        height: 63
        color: "#2b678f"
        radius: 5
        
        RoundButton {
            id: myRoundButtondiez
            x: 10
            y: 10
            width: 130
            height: 45
            Text {
                text: "#"
                color: "#ffffff"
                font.pixelSize: 40
                horizontalAlignment: Text.AlignHCenter
                verticalAlignment: Text.AlignVCenter
                anchors.centerIn: parent
            }
            background: Rectangle {
                radius: myRoundButtondiez.radius = 5
                color: "#007acc"
            }
            onClicked: {
                backend.handleButtonPress("#")
                inactivityTimer.restart()
            }
        }

        RoundButton {
            id: myRoundButton0
            x: 177
            y: 10
            width: 130
            height: 45
            Text {
                text: "0"
                color: "#ffffff"
                font.pixelSize: 40
                horizontalAlignment: Text.AlignHCenter
                verticalAlignment: Text.AlignVCenter
                anchors.centerIn: parent
            }
            background: Rectangle {
                radius: myRoundButton0.radius = 5
                color: "#007acc"
            }
            onClicked: {
                backend.handleButtonPress("0")
                inactivityTimer.restart()
            }
        }

        RoundButton {
            id: myRoundButtonetoile
            x: 341
            y: 10
            width: 130
            height: 45
            Text {
                text: "*"
                color: "#ffffff"
                font.pixelSize: 40
                horizontalAlignment: Text.AlignHCenter
                verticalAlignment: Text.AlignVCenter
                anchors.centerIn: parent
            }
            background: Rectangle {
                radius: myRoundButtonetoile.radius = 5
                color: "#007acc"
            }
            onClicked: {
                backend.handleButtonPress("*")
                inactivityTimer.restart()
            }
        }  
    }
}
