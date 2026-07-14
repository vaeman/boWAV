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
        color: "beige"
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
