import QtQuick 2.12
import QtQuick.Controls 2.15
import QtQuick.Timeline 1.0
import "Constants.js" as Constants 

ApplicationWindow {
    visible: true
    title : Constants.titlefirstlunch
    width: Constants.fullscreenWidth
    height: Constants.fullscreenHeight
    color: Constants.colorgris

    flags: Qt.FramelessWindowHint | Qt.Window

    Image {
        id: imagefirstlunch
        width: parent.width
        height: parent.height
        source: Constants.picture_fisrt_lunch
        anchors.centerIn: parent
    }
}