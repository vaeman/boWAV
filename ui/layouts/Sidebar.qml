import QtQuick

import "../.."

Rectangle {
    required property Theme theme

    anchors {
        top: parent.top
        left: parent.left
        }

    height: parent.height
    width: theme.sidebarWidth
    color: "blue"

    Rectangle {
        id: folder
        anchors {
            top: parent.top
            left: parent.left
            right: parent.right
        }
        height: theme.headerHeight
        color: "purple"
    }
    Rectangle {
        id: sidebar_menu
        anchors {
            top: folder.bottom
            left: parent.left
            right: parent.right
        }
        height: 200
        color: "wheat"
    }
    Rectangle {
        id: sidebar_artists
        anchors {
            top: sidebar_menu.bottom
            left: parent.left
            right: parent.right
            bottom: parent.bottom
        }
        color: "magenta"
    }
}    
