import QtQuick
import "../"

Rectangle {
    required property Theme theme

    height: theme.footerHeight
    color: "#292929"
    
    Image {
        source: player.coverPath
        id: footer_cover

        anchors {
            left: parent.left
            top: parent.top
        }
        height: theme.footerHeight 
        width: theme.footerHeight 
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
            text: player.title
            
            font.family: "Helvetica Neue"
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
            text: player.artist
            
            font.family: "Helvetica Neue"
            font.weight: 300
            font.pixelSize: 16
        }
    }

    Rectangle {
        anchors.fill: parent

        Rectangle {
            anchors.centerIn: parent
            height: 45
            width: 45
            anchors.leftMargin: 10
            anchors.rightMargin: 10
            radius : 45

            color: mousearea.containsMouse ? "#505050" :"#474747"

            MouseArea {
                id: mousearea


                anchors.fill: parent
                hoverEnabled: true
                onClicked: player.togglePlay
            }

            border.width: 2
            border.color: "#1d1d1d"

            Text {
                anchors.centerIn: parent
                anchors.verticalCenterOffset: -2
                anchors.horizontalCenterOffset: 1

                text: "▶"
                font.pixelSize: 40
                color: "#a6a6a6"
            }
        }
                Rectangle {
            anchors.centerIn: parent
            height: 40
            width: 40
            anchors.leftMargin: 10
            anchors.rightMargin: 10
            radius : 40

            color: mousearea2.containsMouse ? "#505050" :"#474747"

            MouseArea {
                id: mousearea2


                anchors.fill: parent
                hoverEnabled: true
                onClicked: player.togglePlay
            }

            border.width: 2
            border.color: "#1d1d1d"

            Text {
                anchors.centerIn: parent
                anchors.verticalCenterOffset: -2
                anchors.horizontalCenterOffset: 1

                text: "▶"
                font.pixelSize: 35
                color: "#a6a6a6"
            }
        }
        
        color: "transparent"
    }

}
