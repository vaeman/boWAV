import QtQuick
import QtQuick.Controls 
import "../"


Rectangle {
    required property Theme theme

    signal buttonSelected(string labelName)

    height: parent.height
    width: theme.sidebarWidth
    color: "blue"

    // Rectangle {
    //     id: scan

    //     anchors {
    //         top: parent.top
    //         left: parent.left
    //         right: parent.right
    //     }
    //     height: theme.headerHeight
    //     color: "purple"

    // }

    
    Rectangle {
        id: sidebar_menu
        anchors {
            top: parent.top
            left: parent.left
            right: parent.right
        }
        height: childrenRect.height
        color: "#1f1f1f"

        Row {
            width: parent.width
            spacing: 0

            Repeater {
                model: [
                    { label: "Artists"},
                    { label: "Playlists"}
                ]

                delegate: Rectangle {
                    color: mouseArea.containsMouse ? "#1d1d1d" : "#141414"
                    width: parent.width /2
                    height: 40

                    Text {
                        text: modelData.label
                        color: "white"
                        font.family: "Helvetica Neue"
                        font.weight: 600
                        font.pixelSize: 16
                        anchors.verticalCenter: parent.verticalCenter
                        anchors.horizontalCenter: parent.horizontalCenter

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
            

            color: mouseArea.containsMouse ? "#202020" : "#171717"

            Text {
                text: name
                color: "white"
                elide: Text.ElideRight

                anchors.verticalCenter: parent.verticalCenter
                anchors.left: parent.left
                anchors.right: parent.right
                anchors.leftMargin: 10
                anchors.rightMargin: 10

                font.pixelSize: 13
                font.weight: 600
                font.family: "Helvetica Neue"
        }
    }
    }
    }