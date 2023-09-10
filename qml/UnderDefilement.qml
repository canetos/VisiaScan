import QtQuick 2.12
import QtQuick.Controls 2.15
import "Constants.js" as Constants

SwipeView {
    property int currentPage: 1
    property int limitewithshow: parent.width
    property int limiteheightshow: parent.height

    id: swipeView
    width: Math.min(limitewithshow,limitewithshow-1)
    height: Math.min(limiteheightshow,limiteheightshow-1)
    currentIndex: currentPage   
    Item{
        visible: currentIndex === 0
        Rectangle {
            id: rectangleUnderDefilement
            x: 0
            y: 0
            width: parent.width
            height: parent.height
            color: Constants.colorblanc 
            Rectangle {
                width: swipeView.width
                height: swipeView.height
                MouseArea {
                    width: parent.width
                    height: parent.height
                    onClicked: {
                        backend.handleButtonPress("Select_interface Display Numeric keypad")
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