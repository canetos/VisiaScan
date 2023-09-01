import QtQuick 2.12
import QtQuick.Controls 2.15

Rectangle {
    width: 500
    height: 370
    color: "transparent"

    signal onClicked()

    Rectangle {
        width: parent.width
        height: parent.height
        color: "transparent"
        Label {
            visible:false
            id: lbcustom
            objectName: 'pyLbcustom'
            text: ""
        }
        Text {
            id: lbmiddle
            objectName: 'pyLbmiddle'
        anchors.centerIn: parent
        property string content1 : "Please, place your face in front the device. \n\n"
        property string content2 : "You can swipe to the right and to the left \n\n"
        property string content3 : "                   <--- & --->\n\n\n\n\n\n"
        property string content4 : "                    " + lbcustom.text
        text: content1 + content2 + content3+content4
        }
    }
}