import QtQuick
import "../.."

Rectangle {
    required property Theme theme
    
    anchors {
            bottom: parent.bottom
            left: parent.left
            right: parent.right
        }

    height: theme.footerHeight
    color: "#292929"
    
    Image {
        source: "../../images/download.png"
        id: footer_cover

        anchors {
            left: parent.left
            top: parent.top
        }
        height: Window.height/10
        width: Window.height/10
    }
    Rectangle {
        id: footer_title
        width: 400
        height: parent.height

        anchors {
            left: footer_cover.right
            leftMargin: 20
            verticalCenter: parent.verticalCenter
        }

        color: "transparent"

        Text {
            anchors {
                left: parent.left
                top: parent.top
                topMargin: 12
            }

            color: "white"
            text: "Fitter Happier"
            
            font.family: "Helvetica"
            font.pixelSize: 20
            font.weight: 600
            
        }

        Text {
            anchors {
                left: parent.left
                top: footer_title.bottom
                topMargin: 2
            }

            color: "white"
            text: "Radiohead"
            
            font.family: "Helvetica"
            font.weight: 300
            font.pixelSize: 16
        }
    }

}
