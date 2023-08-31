import QtQuick 2.12
import QtQuick.Controls 2.15
import QtQuick.Timeline 1.0
import "Constants.js" as Constants

ApplicationWindow {
    visible: true
    title : Constants.textenameprojet
    width: Constants.fullscreenWidth
    height: Constants.fullscreenHeight
    color: Constants.colorgris

    flags: Qt.FramelessWindowHint | Qt.Window

    Image {
        id: imageFond_total
        x: 0
        y: 0
        width: Constants.fullscreenWidth
        height: Constants.fullscreenHeight
        source: Constants.picture_fondTotal
        anchors.horizontalCenter: parent.horizontalCenter

        Image {
            id: imageSousFond_V2
            x: 0
            y: 0
            width: Constants.fullscreenWidth
            height: Constants.fullscreenHeight
            source: Constants.picture_SousFond_V2

            Image {
                id: image
                x: 685
                y: 15
                width: 105
                height: 45
                source: Constants.picture_Ynov_Logo
                fillMode: Image.PreserveAspectFit
            }

// Au besoin de fermer l'UI, décommanté ce code
/* 
            Image {
                id: comptour_P_Logo_GVD
                x: -1
                y: -15
                width: 60
                height: 80
                source: "Images/Comptour_P_Logo_GvD.png"
                rotation: 90
                fillMode: Image.PreserveAspectFit
                Image {
                    id: poweron
                    x: 15
                    y: 10
                    width: 30
                    height: 60
                    rotation: 270
                    source: "Images/power-on.png"
                    fillMode: Image.PreserveAspectFit
                    MouseArea {
                                        anchors.fill: parent
                                        onPressed: parent.color =  Constants.colorbleufoncé // Couleur plus foncée lors de l'appui
                                        onReleased: parent.color = Constants.colorbleu // Retour à la couleur standard lors du relâchement
                    }
                }
            }
*/
            Image {
                id: image1
                x: 10
                y: 155
                width: 155
                height: 240
                anchors.verticalCenter: parent.verticalCenter
                anchors.left: parent.left
                source: Constants.picture_Comptour_P_Logo_GvD
                anchors.verticalCenterOffset: 0
                anchors.leftMargin: 0
                fillMode: Image.PreserveAspectFit

                Image {
                    id: image2
                    x: 40
                    y: 95
                    width: 80
                    height: 55
                    source: Constants.picture_Temp_Left_Pressed
                    fillMode: Image.PreserveAspectFit
                }
            }
            
            Image {
                id: image3
                x: 10
                y: 155
                width: 155
                height: 240
                anchors.verticalCenter: parent.verticalCenter
                anchors.left: parent.left
                source: Constants.picture_Comptour_P_Logo_DvG
                anchors.verticalCenterOffset: 0
                anchors.leftMargin: 655
                fillMode: Image.PreserveAspectFit

                Image {
                    id: image4
                    x: 40
                    y: 95
                    width: 80
                    height: 55
                    source: Constants.picture_Temp_Right_Pressed
                    fillMode: Image.PreserveAspectFit
                }
            }

            Rectangle {
                id: rectangle1
                x: 150
                y: 30
                width: 500
                height: 370
                color: Constants.colorblanc   
            }

            Rectangle {
                id: rectangle2
                x: 225
                y: 420
                width: 350
                height: 100
                radius: 45
                color: Constants.colorbleu // Couleur standard du bouton

                MouseArea {
                    anchors.fill: parent
                    onClicked: {
                        progressBar.visible = true // Afficher la ProgressBar
                        timelineAnimation.running = true // Démarrer l'animation de la ProgressBar
                    }
                    onPressed: parent.color =  Constants.colorbleufoncé // Couleur plus foncée lors de l'appui
                    onReleased: parent.color = Constants.colorbleu // Retour à la couleur standard lors du relâchement
                }

                Text {
                    anchors.centerIn: parent
                    text: "Reconnaissance_IA"
                    font.pixelSize: 15
                    color: "white"
                    horizontalAlignment: Text.AlignHCenter
                    verticalAlignment: Text.AlignVCenter
                }
            }
            ProgressBar {
                id: progressBar
                x: 245
                y: 450
                width: 310
                height: 80
                visible: false
                value: 0
            }

            Timeline {
            id: timeline
            animations: [
                TimelineAnimation {
                    id: timelineAnimation
                    running: false
                    loops: 1
                    duration: 3000
                    to: 3000
                    from: 0
                }
            ]
            startFrame: 0
            enabled: true
            endFrame: 3000

            KeyframeGroup {
                target: progressBar
                property: "value"
                Keyframe {
                    frame: 0
                    value: 0
                }

                Keyframe {
                    frame: 3000
                    value: 1
                    }
                }
            KeyframeGroup {
                target: progressBar
                property: "scale"
                Keyframe {
                    frame: 2999
                    value: 1
                }

                Keyframe {
                    frame: 3000
                    value: 0
                    }
                }
            }    
        }
    }
}