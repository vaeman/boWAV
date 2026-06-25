import QtQuick
import QtQuick.Window


Window {
    height: 720
    width: 1280
    visible: true
    title: "music"
    color: "#0a0908"
    

    Rectangle {
        id: header
        anchors {
            top: parent.top
            left: parent.left
            right: parent.right
        }
        height: 30
        color: "brown"}
    
    Rectangle {
        anchors {
            top: header.bottom
            left: parent.left
            right: parent.right
        }
        color: "Green"
        height: Window.height - 30 - Window.height/10
        Rectangle {
            anchors {
                top: parent.top
                left: parent.left}
            width: parent.width/6
            height: parent.height
            color: "blue"
        }
        
    }

    Rectangle {
        id: footer
        anchors {
            bottom: parent.bottom
            left: parent.left
            right: parent.right
        }
        height: Window.height/10
        color: "#292929"
        
        Image {
            source: "images/download.png"
            id: footer_cover

            anchors {
                left: parent.left
                top: parent.top
            }
            height: Window.height/10
            width: Window.height/10
        }
        Rectangle {
            width: 400
            height: parent.height

            anchors {
                left: footer_cover.right
                leftMargin: 20
                verticalCenter: parent.verticalCenter
            }

            color: "transparent"

            Text {
                id: footer_title
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

}