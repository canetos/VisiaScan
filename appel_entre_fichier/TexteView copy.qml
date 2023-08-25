
import QtQuick 2.12
import QtQuick.Controls 2.15

Rectangle {
    width: 500
    height: 370
    color: "lightgreen"

    property string clickText: "" // Propriété pour stocker le texte du clic

    Text {
        width: parent.width - 40
        height: parent.height - 40
        anchors.centerIn: parent
        font.pixelSize: 14
        text: clickText // Afficher le texte du clic
    }
}
