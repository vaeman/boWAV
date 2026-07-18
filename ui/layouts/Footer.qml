import QtQuick
import QtQuick.Controls
import "../"

Rectangle {
    required property Theme theme

    height: theme.footerHeight
    color: "#121212"
    
    Image {
        source: player.coverPath
        id: footer_cover

        anchors {
            left: parent.left
            top: parent.top
        }
        height: theme.footerHeight 
        width: theme.footerHeight 
    }
    Rectangle {
        width: 400
        height: parent.height

        anchors {
            left: footer_cover.right
            leftMargin: 20
            verticalCenter: parent.verticalCenter
        }

        color: "transparent"

        Text {
            id: footer_title
            anchors {
                left: parent.left
                top: parent.top
                topMargin: 12
            }

            color: "white"
            text: player.title
            
            font.family: "Helvetica Neue"
            font.pixelSize: 20
            font.weight: 600
            
        }

        Text {
            anchors {
                left: parent.left
                top: footer_title.bottom
                topMargin: 2
            }

            color: "white"
            text: player.artist
            
            font.family: "Helvetica Neue"
            font.weight: 300
            font.pixelSize: 16
        }
    }

    Rectangle {
        anchors.fill: parent
        color: "transparent"

        // Slider {
        //     anchors.bottom: parent.bottom
        //     anchors.horizontalCenter: parent.horizontalCenter
        //     anchors.bottomMargin: 10
        //     value: 0.5
            
        //     height: 10

        //     handle: Rectangle {
        //         x: Progress
        //     }
        // }

        Row {
            anchors.centerIn: parent
            spacing: 20

            Item {
                width: 45
                height: 45

                Rectangle {
                    height: 35
                    width: 35
                    radius : 35

                    anchors.centerIn: parent

                    color: mousearea1.containsMouse ? "#505050" :"#474747"

                    MouseArea {
                        id: mousearea1


                        anchors.fill: parent
                        hoverEnabled: true
                        onClicked: player.togglePlay()
                    }

                    border.width: 1
                    border.color: "#1d1d1d"

                    Image {
                        // anchors.fill: parent
                        anchors.centerIn: parent

                        width: 30
                        height: 30
                        
                        fillMode: Image.PreserveAspectFit
                        source: "../assets/icons/angles-left-solid-full.svg"
                    }
                }
            }
            

            Rectangle {
                height: 45
                width: 45
                radius : 45

                color: mousearea.containsMouse ? "#505050" :"#474747"

                MouseArea {
                    id: mousearea
                    anchors.fill: parent
                    hoverEnabled: true
                    onClicked: player.togglePlay()
                }

                border.width: 1
                border.color: "#1d1d1d"

                Image {
                    // anchors.fill: parent
                    anchors.centerIn: parent

                    width: 30
                    height: 30
                    
                    fillMode: Image.PreserveAspectFit
                    source: player.playIconPath
                }
            }
            Item {
                width: 45
                height: 45

                Rectangle {
                    height: 35
                    width: 35
                    radius : 35

                    anchors.centerIn: parent

                    color: mousearea3.containsMouse ? "#505050" :"#474747"

                    MouseArea {
                        id: mousearea3


                        anchors.fill: parent
                        hoverEnabled: true
                        onClicked: player.togglePlay()
                    }

                    border.width: 1
                    border.color: "#1d1d1d"

                    Image {
                        // anchors.fill: parent
                        anchors.centerIn: parent

                        width: 30
                        height: 30
                        
                        fillMode: Image.PreserveAspectFit
                        source: "../assets/icons/angles-right-solid-full.svg"
                    }
                }
            }
        }
    }
}