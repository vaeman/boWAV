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
                        font.family: "Helvetica Neue"
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
                                    id: img2
                                    anchors.fill: parent
                                    source: "../assets/covers/" + albumId + ".png"
                                    fillMode: Image.PreserveAspectCrop
                                    Image {
                                        id: default_img
                                        width: 220
                                        height:200
                                        anchors.fill: parent

                                        source: "../assets/images/download.png"
                                        visible: img2.status != Image.Ready
                                    }
                                }
                            }

                            // Album name + track count
                            Text {
                                text: albumName
                                color: "white"
                                font.family: "Helvetica Neue"
                                font.pixelSize: 13
                                font.weight: Font.Bold
                                elide: Text.ElideRight
                                width: parent.width
                            }

                            Text {
                                text: trackCount + " songs"
                                color: "#888888"
                                font.family: "Helvetica Neue"
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

                            Image {
                                id: default_img
                                width: 220
                                height:200
                                anchors.fill: parent

                                source: "../assets/images/download.png"
                                visible: trackimg.status != Image.Ready
                            }
                        }

                        Column {
                            anchors.verticalCenter: parent.verticalCenter
                            

                            Rectangle{
                                id:albumTextContainer
                                width: 600
                                height: 100
                                color: "transparent"
                                
                                Text {
                                    id: albumText
                                    anchors.fill: parent
                                    text: backend.albumName
                                    verticalAlignment: Text.AlignVCenter
                                    color: "white"
                                    
                                    font.family: "Helvetica Neue"
                                    font.pixelSize: 70
                                    wrapMode: Text.WordWrap
                                    font.weight: Font.Bold
                                    elide: Text.ElideRight
                                    
                                    fontSizeMode: Text.Fit
                                    minimumPixelSize: 40
                                    maximumLineCount: 2
                                }
                            }
                            Rectangle {
                                width: 600
                                height: artistText.height
                                color: "transparent"

                                Text {
                                    id: artistText
                                    text: backend.artistName
                                    font.capitalization: Font.AllUppercase
                                    // anchors.verticalCenter: parent.verticalCenter
                                    color: "#6d6d6d"
                                    font.family: "Helvetica Neue"
                                    font.pixelSize: 25
                                    font.weight: 300
                                    wrapMode: Text.WordWrap
                                    // font.weight: Font.Bold
                                    width: parent.width
                                }
                            }
                        }
                    }
                        
                }

                Rectangle {
                    width: parent.width
                    height: 51
                    color: "#121212"

                    Text {
                        id: headerindex
                        text: "#"
                        width: 35
                        color: "#888888"
                        font.family: "Helvetica Neue"
                        font.pixelSize: 12
                        font.weight: Font.Bold
                        font.letterSpacing: 1
                        anchors.verticalCenter: parent.verticalCenter
                        anchors.left: parent.left
                        anchors.leftMargin: 30
                    }
                    Text {
                        text: "TITLE"
                        color: "#888888"
                        font.family: "Helvetica Neue"
                        font.pixelSize: 12
                        font.weight: Font.Bold
                        font.letterSpacing: 1
                        anchors.verticalCenter: parent.verticalCenter
                        anchors.left: headerindex.right
                        anchors.leftMargin: 16
                    }

                    Text {
                        text: "LENGTH"
                        color: "#888888"
                        font.family: "Helvetica Neue"
                        font.pixelSize: 12
                        font.weight: Font.Bold
                        font.letterSpacing: 1
                        anchors.verticalCenter: parent.verticalCenter
                        anchors.right: parent.right
                        anchors.rightMargin: 16
                    }

                    // thin separator line under the header
                    Rectangle {
                        width: parent.width
                        height: 1
                        anchors.bottomMargin: 10
                        color: "#333333"
                        anchors.bottom: parent.bottom
                    }
                }


                ListView {
                    width: parent.width
                    height: 470
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
                                onDoubleClicked: player.playTrack(trackPath, backend.tracktitle,
                                                            backend.artistName, 
                                                            backend.albumName, 
                                                            "../assets/covers/" + backend.currentAlbumId + ".png")
                        }

                        Text {
                            id: trackindex
                            anchors.left: parent.left
                            text: (index+1) + ".    "
                            anchors.leftMargin: 30
                            width: 40
                            font.pixelSize: 15
                            color: "#9e9e9e"
                            anchors.verticalCenter: parent.verticalCenter
                            elide: Text.ElideRight
                            font.family: "Helvetica Neue"
                            font.weight: 400

                        }
                        
                        Text {
                            width: parent.width - 100
                            text: trackTitle
                            color: "white"
                            anchors.verticalCenter: parent.verticalCenter
                            anchors.left: trackindex.right
                            elide: Text.ElideRight
                            anchors.leftMargin: 10
                            font.family: "Helvetica Neue"
                            font.weight: 400
                            font.pixelSize: 18
                        }
                        Text {
                            text: trackLength
                            color: "#9e9e9e"
                            anchors.verticalCenter: parent.verticalCenter
                            anchors.right: parent.right
                            anchors.rightMargin: 30
                            font.family: "Helvetica Neue"
                            font.pixelSize: 15
                        }
                    }
                }
            }
        }
    }}