    import QtQuick
    import QtQuick.Controls
    import "../"

    Rectangle {
        required property Theme theme
        property alias stack: stack

        color: "#121212"

        Connections {
            target: backend
            function onArtistNameChanged() {
                stack.pop(null)
            }
        }

        StackView {
            id: stack
            anchors.fill: parent
            initialItem: albumView

                pushEnter: Transition {}
                pushExit: Transition {}
                popEnter: Transition {}
                popExit: Transition {}

        }

        Component {
            id: albumView

            Column {

                // anchors.fill: parent
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
            // anchors.fill: parent
            spacing: 0

            Column {
                width: parent.width
                height: parent.height
                spacing: 0
                // anchors.top: backbutton.bottom

                // album cover + info on the left
                Rectangle {
                    width: parent.width
                    height: 250
                    color: "#121212"

                    Row {
                        anchors { fill: parent; margins: 20}
                        spacing: 12
                        

                        Image {
                            id: trackimg
                            width: 220
                            height: 220
                            // anchors.verticalCenter: parent.verticalCenter
                            source: "../assets/covers/" + backend.currentAlbumId + ".png"
                            fillMode: Image.PreserveAspectCrop
                        }
                        Column {
                        
                            Rectangle{
                                width: 600
                                height: albumText.height + 20
                                color: "transparent"
                                
                                Text {
                                    id: albumText
                                    text: backend.albumName
                                    anchors.verticalCenter: parent.verticalCenter
                                    color: "white"
                                    font.family: "Helvetica"
                                    font.pixelSize: 50
                                    wrapMode: Text.WordWrap
                                    font.weight: Font.Bold
                                    width: parent.width
                                }
                            }
                            Rectangle {
                                width: 600
                                height: artistText.height
                                color: "transparent"

                                Text {
                                    id: artistText
                                    text: backend.artistName
                                    // anchors.verticalCenter: parent.verticalCenter
                                    color: "white"
                                    font.family: "Helvetica"
                                    font.pixelSize: 25
                                    wrapMode: Text.WordWrap
                                    // font.weight: Font.Bold
                                    width: parent.width
                                }
                            }
                        }
                    }
                        
                }

                // track list on the right
                ListView {
                    width: parent.width
                    height: parent.height
                    clip: true
                    boundsBehavior: Flickable.StopAtBounds
                    model: trackModel

                    delegate: Rectangle {
                        width: parent.width
                        height: 48
                        color: mouseArea.containsMouse ? "#333333" : "transparent" 

                        MouseArea {
                            id: mouseArea
                                anchors.fill: parent
                                hoverEnabled: true
                        }

                        Text {
                            text: (index + 1) + ".    " + trackTitle
                            color: "white"
                            anchors.verticalCenter: parent.verticalCenter
                            anchors.left: parent.left
                            anchors.leftMargin: 16
                            font.family: "Jetbrains Mono"
                            font.pixelSize: 13
                        }
                        Text {
                            text: trackLength
                            color: "white"
                            anchors.verticalCenter: parent.verticalCenter
                            anchors.right: parent.right
                            anchors.rightMargin: 16
                            font.family: "Jetbrains Mono"
                            font.pixelSize: 13
                        }
                    }
                }
            }
        }
    }}