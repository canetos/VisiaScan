import QtQuick 2.12
import QtQuick.Controls 2.15
import QtQuick.Timeline 1.0

Rectangle {
    id: rectangle
    width: 500
    height: 370

    color: "#c2c2c2"

   
    ProgressBar {
        id: progressBar
        x: 101
        y: 261
        width: 300
        height: 75
        value: 0
        
        Button {
            id: buttonRecoIA
            text: qsTr("Press me")
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
    Text {
        id: label
        text: qsTr("Hello IHM_Interphone")
        anchors.top: button.bottom
        font.family: Constants.font.family
        anchors.topMargin: 45
        anchors.horizontalCenter: parent.horizontalCenter

        SequentialAnimation {
            id: animation

            ColorAnimation {
                id: colorAnimation1
                target: buttonRecoIA
                property: "color"
                to: "#2294c6"
                from: Constants.backgroundColor
            }

            ColorAnimation {
                id: colorAnimation2
                target: rectangle
                property: "color"
                to: Constants.backgroundColor
                from: "#007acc"
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
                target: label
                text: qsTr("Button Checked")
            }
            
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