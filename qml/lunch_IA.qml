import QtQuick 2.12
import QtQuick.Controls 2.15
import "Constants.js" as Constants

ApplicationWindow {
    visible: true
    width: Constants.demiscreenWidth
    height: Constants.demiscreenHeight
    title: "lunch_IA"
    
    flags: Qt.FramelessWindowHint | Qt.Window

    Rectangle {
        id: rectanglesous
        width: parent.width //500
        height: parent.height //370
        color: Constants.transparent

        Rectangle {
            id: rectangle
            width: 500
            height: 370

            color: Constants.backgroundColor

            ProgressBar {
                id: progressBar
                x: 101
                y: 261
                width: 300
                height: 75
                value: 0

                Button {
                    id: buttonRecoIA
                    text: qsTr("Reconnaissance_IA")
                    checkable: true
                    x: -24
                    y: -45
                    width: 350
                    height: 100

                    Connections {
                        target: button
                        onClicked: animation.start()
                    }
                }
            }

            Timeline {
                id: timeline
                animations: [
                    TimelineAnimation {
                        id: timelineAnimation
                        running: true
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
            }

            states: [
                State {
                    name: "clicked"
                    when: button.checked

                    PropertyChanges {
                        target: timeline
                        enabled: true
                    }

                    PropertyChanges {
                        target: timelineAnimation
                        running: true
                    }
                }
            ]
        }
    }        
}