import QtQuick 2.12
import QtQuick.Controls 2.15

ApplicationWindow {
    visible: true
    width: 500
    height: 370
    title: "Interface Défilante"

    property int currentPage: 1

    SwipeView {
        id: swipeView
        width: parent.width
        height: parent.height - 40
        currentIndex: currentPage

        Item{
            Rectangle {
                width: swipeView.width
                height: swipeView.height
                color: "lightgray"

                MouseArea {
                    width: parent.width
                    height: parent.height
                    onClicked: backend.handleButtonPress("Select_interface Display Numeric keypad")
                    BoutonView {}
                }
            }
        }

         Item{
            Rectangle {
                width: swipeView.width
                height: swipeView.height

                MouseArea {
                    width: parent.width
                    height: parent.height
                    onClicked: backend.handleButtonPress("Select_interface Menu")
                    Rectangle {
                        width: parent.width
                        height: parent.height
                        color: "lightgray"
                    }
                }
            }
        }

        Item {
            Rectangle {
                width: swipeView.width
                height: swipeView.height

                MouseArea {
                    width: parent.width
                    height: parent.height
                    onClicked: backend.handleButtonPress("Select_interface Display Search Hab")
                    BoutonViewcopy {}
                }
            }
        }
    }
/*
Rectangle {
        width: parent.width
        height: 40
        color: "lightgray"

        Row {
            spacing: 10
            anchors.centerIn: parent

            MouseArea {
                width: 100
                height: 30
                onClicked: {
                    backend.handleButtonPress("Bouton cliqué Précédent")
                    currentPage = (currentPage - 1 + swipeView.count) % swipeView.count
                }
                Rectangle {
                    width: parent.width
                    height: parent.height
                    color: "transparent"
                    Text {
                        anchors.centerIn: parent
                        text: "Précédent"
                    }
                }
            }

            MouseArea {
                width: 100
                height: 30
                onClicked: {
                    backend.handleButtonPress("Bouton cliqué Suivant")
                    currentPage = (currentPage + 1) % swipeView.count
                }
                Rectangle {
                    width: parent.width
                    height: parent.height
                    color: "transparent"
                    Text {
                        anchors.centerIn: parent
                        text: "Suivant"
                    }
                }
            }
        }
    }*/
}