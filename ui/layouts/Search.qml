import QtQuick

import "../.."

Rectangle {
    required property Theme theme

    anchors {
        top: parent.top
        left: parent.left
        right: parent.right
    }
    
    height: theme.headerHeight
    color: "brown"}