import QtQuick 2.12
import QtQuick.Controls 2.15
import QtQuick.Timeline 1.0
import "Constants.js" as Constants

ApplicationWindow {
    visible: true
    title : Constants.titleExecutable
    width: Constants.fullscreenWidth
    height: Constants.fullscreenHeight
    color: Constants.colorgris

    flags: Qt.FramelessWindowHint | Qt.Window

    Image {
        id: imageFond_total
        width: parent.width
        height: parent.height
        source: Constants.picture_fondTotal
        anchors.centerIn: parent
        Image {
            id: imageSousFond
            width: parent.width
            height: parent.height
            source: Constants.picture_SousFond
            anchors.centerIn: parent

            Image {
                id: imageYnov_Logo
                x: 615
                y: 15
                width: 175 
                height: 71
                source: Constants.picture_Ynov_Logo
                fillMode: Image.PreserveAspectFit
            }

            Image {
                id: imageComptour_P_Logo
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
                    id: imageLogo_Maison
                    x: 40
                    y: 65
                    width: 80
                    height: 95
                    source: Constants.picture_Logo_Maison
                    fillMode: Image.PreserveAspectFit
                }
            }

            Text {
                id: titreprojet
                x: 175
                y: 130
                width: 515
                height: 105
                color: Constants.colorblanc
                text: qsTr(Constants.textenameprojet)
                font.pixelSize: 80
                horizontalAlignment: Text.AlignHCenter
                anchors.topMargin: 5
            }

            Text {
                id: soustitreprojet1
                x: 175
                y: 225
                width: 515
                height: 95
                color: Constants.colorblanc
                text: qsTr(Constants.texteprojet)
                font.pixelSize: 50
                horizontalAlignment: Text.AlignHCenter
                anchors.verticalCenterOffset: 7
                anchors.topMargin: 6
            }

            Text {
                id: soustitreprojet2
                x: 175
                y: 290
                width: 515
                height: 60
                color: Constants.colorblanc
                text: qsTr(Constants.texteprojet_gene)
                font.pixelSize: 30
                horizontalAlignment: Text.AlignHCenter
                anchors.leftMargin: 105
                anchors.rightMargin: 115
                anchors.horizontalCenter: soustitreprojet1.horizontalCenter
                anchors.topMargin: 5
                anchors.verticalCenterOffset: 50
            }

            Text {
                id: soustitreprojet3
                x: 175
                y: 445
                width: 515
                height: 60
                color: Constants.colorblanc
                text: qsTr(Constants.textevide)
                font.pixelSize: 20
                horizontalAlignment: Text.AlignHCenter
                scale: 0
                anchors.horizontalCenter: soustitreprojet1.horizontalCenter
                anchors.topMargin: 5
                anchors.leftMargin: 105
                anchors.verticalCenterOffset: 50
                anchors.rightMargin: 115
            }

            Text {
                id: soustitreprojet4
                x: 555
                y: 450
                width: 140
                height: 60
                color: Constants.colorblanc
                text: progressBar.state
                font.pixelSize: 20
                horizontalAlignment: Text.AlignHCenter
                anchors.horizontalCenter: soustitreprojet1.horizontalCenter
                anchors.topMargin: 5
                scale: 0
                anchors.leftMargin: 105
                anchors.verticalCenterOffset: 50
                anchors.rightMargin: 115
            }
            ProgressBar {
                id: progressBar
                x: 175
                y: 485
                width: 515
                height: 25
                scale: 0
                to: 1
                value: 1
            }
        }
    }

    Timeline {
        id: timelinetest
        animations: [
            TimelineAnimation {
                id: timelineAnimation
                duration: Constants.duration_total
                running: true
                loops: 1
                to: Constants.duration_total
                from: 0
            }
        ]
        endFrame: Constants.duration_total
        enabled: true
        startFrame: 0

        KeyframeGroup {
            target: soustitreprojet3
            property: "scale"
            Keyframe {
                value: 0
                frame: 0
            }

            Keyframe {
                value: 0
                frame: 100
            }

            Keyframe {
                value: 1
                frame: 350
            }
        }

        KeyframeGroup {
            target: progressBar
            property: "value"
            Keyframe {
                value: 0
                frame: 350
            }

            Keyframe {
                value: 1
                frame: 6000
            }
        }
        KeyframeGroup {
            target: progressBar
            property: "scale"
            Keyframe {
                value: 0
                frame: 0
            }

            Keyframe {
                value: 0
                frame: 100
            }

            Keyframe {
                value: 1
                frame: 350
            }
            Keyframe {
                value: 1
                frame: 6000
            }
            Keyframe {
                value: 0
                frame: 6050
            }
        }

        KeyframeGroup {
            target: soustitreprojet3
            property: "text"
            Keyframe {
                value: Constants.textexe_initialization
                frame: 0
            }
            Keyframe {
                value: Constants.textexe_loading
                frame: 750
            }
            Keyframe {
                value: Constants.textexe_build
                frame: 2500
            }
            Keyframe {
                value: Constants.textexe_treatment
                frame: 3500
            }
            Keyframe {
                value: Constants.textexe_Finalization
                frame: 5000
            }
            Keyframe {
                value: Constants.textexe_finish
                frame: 6000
            }
        }
    }
}