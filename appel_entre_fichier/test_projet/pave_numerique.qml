import QtQuick 2.12
import QtQuick.Controls 2.15
import "Constants.js" as Constants

Rectangle {
    width: parent.width //500
    height: parent.height //370
    color: "lightgreen"

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
                    width: parent.width
                    height: parent.height
                    color: "#ffffff"
                    text: "....."
                    font.pixelSize: 40
                    verticalAlignment: Text.AlignVCenter
                    anchors.verticalCenterOffset: 0
                    anchors.horizontalCenterOffset: 0
                    anchors.centerIn: parent
                }
            }
        }
        Rectangle {
            id: rectangleC
            x: 10
            y: 10
            width: 130
            height: 50
            color: "#ac0000"
            radius: 5

            MouseArea {
                anchors.fill: parent
                //onPressed: parent.color = "#900000" // Couleur plus foncée lors de l'appui
                //onReleased: parent.color
                            = "#ac0000" // Retour à la couleur standard lors du relâchement
            }

            Text {
                color: "#ff0000"
                text: "C"
                font.pixelSize: 40
                horizontalAlignment: Text.AlignHCenter
                verticalAlignment: Text.AlignVCenter
                anchors.centerIn: parent
            }
        }
        Rectangle {
            id: rectangleV
            x: 341
            y: 10
            width: 130
            height: 50
            color: "#00ac7a"
            radius: 5

            MouseArea {
                anchors.fill: parent
                //onPressed: parent.color = "#006400" // Couleur plus foncée lors de l'appui
                //onReleased: parent.color
                            = "#00ac7a" // Retour à la couleur standard lors du relâchement
            }

            Text {
                color: "#00FF00"
                text: "V"
                font.pixelSize: 40
                horizontalAlignment: Text.AlignHCenter
                verticalAlignment: Text.AlignVCenter
                anchors.centerIn: parent
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
        Rectangle {
            id: rectangle1
            x: 10
            y: 10
            width: 130
            height: 45
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
                text: "1"
                font.pixelSize: 40
                horizontalAlignment: Text.AlignHCenter
                verticalAlignment: Text.AlignVCenter
                anchors.centerIn: parent
            }
        }

        Rectangle {
            id: rectangle2
            x: 177
            y: 10
            width: 130
            height: 45
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
                text: "2"
                font.pixelSize: 40
                horizontalAlignment: Text.AlignHCenter
                verticalAlignment: Text.AlignVCenter
                anchors.centerIn: parent
            }
        }

        Rectangle {
            id: rectangle3
            x: 341
            y: 10
            width: 130
            height: 45
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
                text: "3"
                font.pixelSize: 40
                horizontalAlignment: Text.AlignHCenter
                verticalAlignment: Text.AlignVCenter
                anchors.centerIn: parent
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
        Rectangle {
            id: rectangle4
            x: 10
            y: 10
            width: 130
            height: 45
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
                text: "4"
                font.pixelSize: 40
                horizontalAlignment: Text.AlignHCenter
                verticalAlignment: Text.AlignVCenter
                anchors.centerIn: parent
            }
        }

        Rectangle {
            id: rectangle5
            x: 177
            y: 10
            width: 130
            height: 45
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
                text: "5"
                font.pixelSize: 40
                horizontalAlignment: Text.AlignHCenter
                verticalAlignment: Text.AlignVCenter
                anchors.centerIn: parent
            }
        }

        Rectangle {
            id: rectangle6
            x: 341
            y: 10
            width: 130
            height: 45
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
                text: "6"
                font.pixelSize: 40
                horizontalAlignment: Text.AlignHCenter
                verticalAlignment: Text.AlignVCenter
                anchors.centerIn: parent
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
        Rectangle {
            id: rectangle7
            x: 10
            y: 10
            width: 130
            height: 45
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
                text: "7"
                font.pixelSize: 40
                horizontalAlignment: Text.AlignHCenter
                verticalAlignment: Text.AlignVCenter
                anchors.centerIn: parent
            }
        }

        Rectangle {
            id: rectangle8
            x: 177
            y: 10
            width: 130
            height: 45
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
                text: "8"
                font.pixelSize: 40
                horizontalAlignment: Text.AlignHCenter
                verticalAlignment: Text.AlignVCenter
                anchors.centerIn: parent
            }
        }

        Rectangle {
            id: rectangle9
            x: 341
            y: 10
            width: 130
            height: 45
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
                text: "9"
                font.pixelSize: 40
                horizontalAlignment: Text.AlignHCenter
                verticalAlignment: Text.AlignVCenter
                anchors.centerIn: parent
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
        Rectangle {
            id: rectanglediez
            x: 10
            y: 10
            width: 130
            height: 45
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
                text: "#"
                font.pixelSize: 40
                horizontalAlignment: Text.AlignHCenter
                verticalAlignment: Text.AlignVCenter
                anchors.centerIn: parent
            }
        }

        Rectangle {
            id: rectangle0
            x: 177
            y: 10
            width: 130
            height: 45
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
                text: "0"
                font.pixelSize: 40
                horizontalAlignment: Text.AlignHCenter
                verticalAlignment: Text.AlignVCenter
                anchors.centerIn: parent
            }
        }

        Rectangle {
            id: rectangleetoile
            x: 341
            y: 10
            width: 130
            height: 45
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
                text: "*"
                font.pixelSize: 50
                horizontalAlignment: Text.AlignHCenter
                verticalAlignment: Text.AlignVCenter
                anchors.verticalCenterOffset: 5
                anchors.horizontalCenterOffset: 0
                anchors.centerIn: parent
            }
        }
    }
}