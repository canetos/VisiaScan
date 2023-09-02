import QtQuick 2.12
import QtQuick.Controls 2.15
import "Constants.js" as Constants

SwipeView {
    
    Timer {
        id: inactivityTimer
        interval: 10000
        repeat: false
        onTriggered: {
            currentPage = 1
        }
    }
/*
      onCurrentIndexChanged: {
        // Appeler la fonction de réinitialisation
        resetWindow();
    }

    function resetWindow() {
        if (currentIndex === 0) {
        // Réinitialiser les valeurs des champs et masquer les éléments pour le premier Item
        lbNum_Keypad.text = "Waiting code PIN";
        } 
    else if (currentIndex === 1) {
        // Réinitialiser les valeurs des champs et masquer les éléments pour le deuxième Item
        }

    else if (currentIndex === 2) {
        // Réinitialiser les valeurs des champs et masquer les éléments pour le troisième Item
        lbSerach_Hab.text = "Wait for your choice"
        }
    }
*/

    property int currentPage: 1
    id: swipeView
    width: Math.min(500, 499)
    height: 370 - 40
    currentIndex: currentPage    

    Item{
        visible: currentIndex === 0
        Rectangle {
            id: rectangleUnderDefilement
            x: 0
            y: 0
            width: 500
            height: 370
            color: Constants.colorblanc 
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
    }

    Item{
        visible: currentIndex === 1 
        Rectangle {
            width: swipeView.width
            height: swipeView.height
            color: "transparent"

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

    Item {
        visible: currentIndex === 3
        Rectangle {
                width: swipeView.width
                height: swipeView.height
                visible: true

                MouseArea {
                    width: parent.width
                    height: parent.height
                    onClicked: {
                        backend.handleButtonPress("Select_interface Display Admin")
                        inactivityTimer.restart()
                    }
                    UnderAdmin {}
                }
            }
        
    }
/*

    Item {
        visible: (text === "finishLoadAdminOK")
        Label {
            id: lbLoad_win
            objectName: 'pyLbLoad_win_Admin'
            text: ""
            visible : false

            Connections {
                target: pyLbLoad_win_Admin
                onTextChanged: {
                    if (text !== "finishState_Admin") {
                        if (text === "finishStateAdminOK") {
                            if (currentIndex === 3) {
                                backend.handleButtonPress("Open_Admin")
                            }
                        }
                        backend.handleButtonPress("Validate_Admin");    
                    }
                    text = ""; // Réinitialiser le texte après le traitement
                }
            }
            Rectangle {
                width: swipeView.width
                height: swipeView.height
                visible: true

                MouseArea {
                    width: parent.width
                    height: parent.height
                    onClicked: {
                        backend.handleButtonPress("Select_interface Display Admin")
                        inactivityTimer.restart()
                    }
                    UnderSearchUInhabitant {}
                }
            }
        }   
    }
    
    */

    

/*
    Rectangle {
        visible:false
        width: parent.width
        height: 40
        color: "transparent"

        Label {
            id: lblPrevious
            objectName: 'pyLblprevious'
            text: "unset"

            Connections {
                target: lblPrevious
                onTextChanged: {
                    if (lblPrevious.text === "clicked Previous") {
                        currentPage = (currentPage - 1 + swipeView.count) % swipeView.count;
                    }
                }
            }
        }

        Label {
            id: lblNext
            objectName: 'pyLblnext'
            text: "unset"

            Connections {
                target: lblNext
                onTextChanged: {
                    if (lblNexttext === "clicked Next") {
                        currentPage = (currentPage + 1) % swipeView.count;
                    }
                }
            }
        }
    }*/
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