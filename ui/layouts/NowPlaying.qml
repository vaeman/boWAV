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
            text: backend.albumName
            color: "white"
            font.family: "Helvetica"
            font.pixelSize: 20
            font.weight: 600
        }
    }
    Rectangle {
        id: now_playing_cover
        anchors {
            top: now_playing_album.bottom
            left: parent.left
            right: parent.right
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
            bottom: parent.bottom
        }
        color: "pink" 
    }
}
