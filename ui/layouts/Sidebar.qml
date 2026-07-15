import QtQuick
import QtQuick.Controls 
import "../"


Rectangle {
    required property Theme theme

    anchors {
        top: parent.top
        left: parent.left
        }

    signal buttonSelected(string labelName)

    height: parent.height
    width: theme.sidebarWidth
    color: "blue"

    Rectangle {
        id: scan

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
            top:scan.bottom
            left: parent.left
            right: parent.right
        }
        height: childrenRect.height
        color: "#1f1f1f"

        Column {
            width: parent.width
            bottomPadding: 10
            spacing: 0

            Text {
                anchors.horizontalCenter: parent.horizontalCenter
                text: "LIBRARY"
                color: "#c8c8c8"
                font.family: "Jetbrains Mono"
                font.letterSpacing: 15
                font.pixelSize: 20
                font.weight: Font.Bold
                leftPadding: 10
                topPadding: 16
                bottomPadding: 8
            }

            Repeater {
                model: [
                    { label: "Albums" },
                    { label: "Artists"},
                    { label: "Playlists"}
                ]

                delegate: Rectangle {
                    width: parent.width
                    color: mouseArea.containsMouse ? "#2a2a2a" : "transparent"
                    height: 36
                    radius: 4

                    Text {
                        text: modelData.label
                        color: "white"
                        font.family: "Jetbrains Mono"
                        font.pixelSize: 14 
                        anchors.verticalCenter: parent.verticalCenter
                        anchors.left: parent.left
                        anchors.leftMargin: 10
                    }

                    MouseArea {
                        id: mouseArea
                        anchors.fill: parent
                        hoverEnabled: true
                        onClicked: backend.buttonSelected(modelData.label)
                    }
                }
            }
        }
    }
    
    ListView {
        id: sidebar_artists
        clip: true
        boundsBehavior: Flickable.StopAtBounds

        anchors {
            top: sidebar_menu.bottom
            left: parent.left
            right: parent.right
            bottom: parent.bottom
        }
        model: artistModel

        delegate: Rectangle {
            width: ListView.view.width
            height: 35
            
            MouseArea {
                id: mouseArea
                anchors.fill: parent
                onClicked: backend.selectArtist(artistId)
                hoverEnabled: true
                }
            

            color: mouseArea.containsMouse ? "#3a3a3a" : index % 2 === 0 ? "#1a1a1a" : "#222222"

            Text {
                text: name
                color: "white"
                elide: Text.ElideRight

                anchors.verticalCenter: parent.verticalCenter
                anchors.left: parent.left
                anchors.right: parent.right
                anchors.leftMargin: 10

                font.family: "Jetbrains Mono"
        }
    }
    }
    }