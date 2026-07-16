import QtQuick

import "../"


Rectangle {
    required property Theme theme

    width: theme.playerWidth

    Rectangle {
        id: now_playing_album
        anchors {
            top: parent.top
            right: parent.right
            left: parent.left
        }
        height: 50
        color: "#171717"

        Text {
            anchors.verticalCenter: parent.verticalCenter
            anchors.left: parent.left
            anchors.right: parent.right
            anchors.leftMargin: 15;
            anchors.rightMargin: 15;
            text: player.album
            color: "white"
            font.family: "Helvetica Neue"
            font.pixelSize: 20
            font.weight: 600
            elide: Text.ElideRight
        }
    }
    Rectangle {
        anchors {
            left: parent.left
            right: parent.right
            bottom: now_playing_cover.top
        }
        height: 1
        color: "#282828"

    }
    Rectangle {
        id: now_playing_cover
        anchors {
            top: now_playing_album.bottom
            left: parent.left
            right: parent.right
        }
        Image {
            anchors.fill: parent

            source: player.coverPath
        }
        height: parent.width
        color: "black"
    }
    Rectangle {
        id: now_playing_track
        anchors {
            top: now_playing_cover.bottom
            left: parent.left
            right: parent.right
        }
        height: 60
        color: "#171717"
        Text {
            id: titletext
            // anchors.fill: parent;
            anchors {
                left: parent.left
                right: parent.right
                top: parent.top
            }
            // anchors.verticalCenter: parent.verticalCenter
            anchors.topMargin: 10
            anchors.leftMargin: 15
            anchors.rightMargin: 15
            text: player.title
            color: "white"
            font.family: "Helvetica Neue"
            font.pixelSize: 21
            elide: Text.ElideRight
            font.weight: 600       
        }
        Text {
            anchors {
                left: parent.left
                right: parent.right
                top: titletext.bottom
            }
            text: player.artist
            // anchors.verticalCenter: parent.verticalCenter
            anchors.leftMargin: 15
            anchors.rightMargin: 15
            color: "#7c7c7c"
            font.family: "Helvetica Neue"
            font.pixelSize: 16
            elide: Text.ElideRight
            font.weight: 300
        }
    }
    Rectangle {
            anchors{
                left: parent.left
                right: parent.right
                bottom: queue.top
            }
            height: 2
            color: "#323232"
        }

    Rectangle {
        id: queue
        anchors { 
            top: now_playing_track.bottom
            left:parent.left
            right: parent.right
        }
        Text {
            id: qtitle
            text: "Queue"
            color: "#585858"
            font.family: "Helvetica Neue"
            font.pixelSize: 20
            font.weight: Font.Bold
            leftPadding: 10
            topPadding: 10
            bottomPadding: 8
        }

        height: 212
        color: "#171717"
    }
}
