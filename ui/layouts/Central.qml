    import QtQuick
    import QtQuick.Controls
    import "../"

    Rectangle {
        required property Theme theme
        property alias stack: stack

        color: "#121212"

        StackView {
            id: stack
            anchors.fill: parent
            initialItem: albumView
        }

        Component {
            id: albumView

            Column {

                anchors.fill: parent
                spacing: 0

                // Artist name header
                Rectangle {
                    width: parent.width
                    height: 100
                    color: "#121212"

                    Text {
                        anchors {
                            left: parent.left
                            leftMargin: 24
                            verticalCenter: parent.verticalCenter
                        }
                        text: backend.artistName
                        color: "white"
                        font.family: "Helvetica"
                        font.pixelSize: 36
                        font.weight: Font.Bold
                    }
                }

                // Album grid
                GridView {
                    width: parent.width
                    height: parent.height - 120
                    clip: true
                    boundsBehavior: Flickable.StopAtBounds

                    model: albumModel

                    cellWidth: width / 3
                    cellHeight: cellWidth + 48  // square cover + text below

                    delegate: Rectangle {

                        width: GridView.view.cellWidth
                        height: GridView.view.cellHeight
                        color: mouseArea.containsMouse ? "#333333" : "transparent" 

                        MouseArea {
                                id: mouseArea
                                anchors.fill: parent
                                onClicked: { backend.selectAlbum(albumId)
                                            stack.push(trackView)}
                                hoverEnabled: true
                            }

                        Column {
                            anchors {
                                fill: parent
                                margins: 12
                            }
                            spacing: 8

                            // Album cover
                            Rectangle {
                                width: parent.width
                                height: parent.width
                                color: "#2a2a2a"  // fallback if no cover

                                Image {
                                    anchors.fill: parent
                                    source: "../assets/covers/" + albumId + ".png"
                                    fillMode: Image.PreserveAspectCrop
                                }
                            }

                            // Album name + track count
                            Text {
                                text: albumName
                                color: "white"
                                font.family: "Helvetica"
                                font.pixelSize: 13
                                font.weight: Font.Bold
                                elide: Text.ElideRight
                                width: parent.width
                            }

                            Text {
                                text: trackCount + " songs"
                                color: "#888888"
                                font.family: "Helvetica"
                                font.pixelSize: 12
                                width: parent.width
                            }
                        }
                    }
                }
            }
        }
        Component {
        id: trackView

        Column {
            anchors.fill: parent
            spacing: 0

            Rectangle {
                width: parent.width
                height: 50
                color: "#1a1a1a"

                Text {
                    anchors.verticalCenter: parent.verticalCenter
                    anchors.left: parent.left
                    anchors.leftMargin: 16
                    text: "← Back"
                    color: "white"
                    font.pixelSize: 14

                    MouseArea {
                        anchors.fill: parent
                        onClicked: stack.pop()
                    }
                }
            }

            Row {
                width: parent.width
                height: parent.height - 50
                spacing: 0

                // album cover + info on the left
                Rectangle {
                    width: 220
                    height: parent.height
                    color: "#1a1a1a"

                    Column {
                        anchors { fill: parent; margins: 20 }
                        spacing: 12

                        Image {
                            id: trackimg
                            width: 180
                            height: 180
                            source: "../assets/covers/" + backend.currentAlbumId + ".png"
                            fillMode: Image.PreserveAspectCrop
                        }
                        Text {
                            anchors {
                                top: trackimg.bottom
                            }
                            text: albumName
                        }
                    }
                }

                // track list on the right
                ListView {
                    width: parent.width - 220
                    height: parent.height
                    clip: true
                    boundsBehavior: Flickable.StopAtBounds
                    model: trackModel

                    delegate: Rectangle {
                        width: parent.width
                        height: 48
                        color: index % 2 === 0 ? "#1a1a1a" : "#222222"

                        Text {
                            text: (index + 1) + ".    " + trackTitle
                            color: "white"
                            anchors.verticalCenter: parent.verticalCenter
                            anchors.left: parent.left
                            anchors.leftMargin: 16
                            font.family: "Jetbrains Mono"
                            font.pixelSize: 13
                        }
                    }
                }
            }
        }
    }}