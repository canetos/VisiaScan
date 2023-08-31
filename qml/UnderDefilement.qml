import QtQuick 2.12
import QtQuick.Controls 2.15

SwipeView {
    
    Timer {
        id: inactivityTimer
        interval: 10000
        repeat: false
        onTriggered: {
            currentPage = 1
        }
    }

      onCurrentIndexChanged: {
        // Appeler la fonction de réinitialisation
        resetWindow();
    }

    function resetWindow() {
        if (currentIndex === 0) {
        // Réinitialiser les valeurs des champs et masquer les éléments pour le premier Item
        lbNum_Keypad.text = "Waiting for passwords";
        } 
    else if (currentIndex === 1) {
        // Réinitialiser les valeurs des champs et masquer les éléments pour le deuxième Item
        }

    else if (currentIndex === 2) {
        // Réinitialiser les valeurs des champs et masquer les éléments pour le troisième Item
        lbSerach_Hab.text = "Wait for your choice"
        }
    }

    property int currentPage: 1
    id: swipeView
    width: Math.min(500, 499)
    height: 370 - 40
    currentIndex: currentPage    

    Item{
        visible: currentIndex === 0
        Rectangle {
            width: swipeView.width
            height: swipeView.height
            
            MouseArea {
                width: parent.width
                height: parent.height
                onClicked: {
                    backend.handleButtonPress("Select_interface Display Numeric keypad")
                    inactivityTimer.restart()
                }
                UnderNumericKeypad {}
            }
        }
    }

    Item{
        visible: currentIndex === 1
        Rectangle {
            width: swipeView.width
            height: swipeView.height

            MouseArea {
                width: parent.width
                height: parent.height
                onClicked: {
                    backend.handleButtonPress("Select_interface Menu")
                    inactivityTimer.restart()
                }
                UnderMiddle {}
            }
        }
    }

    Item {
        visible: currentIndex === 2
        Rectangle {
            width: swipeView.width
            height: swipeView.height

            MouseArea {
                width: parent.width
                height: parent.height
                onClicked: {
                    backend.handleButtonPress("Select_interface Display Search Hab")
                    inactivityTimer.restart()
                }
                UnderSearchUInhabitant {}
            }
        }
    }
}

//Enleve les commentaire pour tester avec la sélection au clic
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
                inactivityTimer.restart()
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
                inactivityTimer.restart()
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
