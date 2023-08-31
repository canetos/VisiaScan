import QtQuick 2.12
import QtQuick.Controls 2.15

Rectangle {
    width: 500
    height: 370
    color: "transparent"

    signal onClicked()

    Rectangle {
        Text {
        anchors.centerIn: parent
        text: "swiper de droite à gauche \n      <--- & --->"
    } 
        width: parent.width
        height: parent.height
        color: "lightgray"
    }
}