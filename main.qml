import QtQuick
import QtQuick.Window
import QtQuick.Layouts


Window {
    height: 720
    width: 1280
    visible: true
    visibility: Window.Maximized
    title: "music"
    color: "#0a0908"

    
    Rectangle {
        id: main
        anchors {
            top: parent.top
            left: parent.left
            right: parent.right
        }
        color: "Green"
        height: Window.height - Window.height/10
        
        Rectangle {
            id: search
            anchors {
                top: parent.top
                left: parent.left
                right: parent.right
            }
            height: 60
            color: "brown"}
        
        Rectangle {
            id: sidebar
            anchors {
                top: parent.top
                left: parent.left
                }

            height: parent.height
            width: 200
            color: "blue"

            Rectangle {
                id: folder
                anchors {
                    top: parent.top
                    left: parent.left
                    right: parent.right
                }
                height: 60
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

        Rectangle {
            id: central_view
            anchors {
                left: sidebar.right
                right: now_playing.left
                top: search.bottom
                bottom: parent.bottom
            }
            color: "blue"
            }

        Rectangle {
            id: now_playing
            anchors {
                top: search.bottom
                right: parent.right
            }
            height: parent.height
            width: 500

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
                height: 500
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
    }


    Rectangle {
        id: footer
        anchors {
            bottom: parent.bottom
            left: parent.left
            right: parent.right
        }
        height: Window.height/10
        color: "#292929"
        
        Image {
            source: "images/download.png"
            id: footer_cover

            anchors {
                left: parent.left
                top: parent.top
            }
            height: Window.height/10
            width: Window.height/10
        }
        Rectangle {
            id: footer_title
            width: 400
            height: parent.height

            anchors {
                left: footer_cover.right
                leftMargin: 20
                verticalCenter: parent.verticalCenter
            }

            color: "transparent"

            Text {
                anchors {
                    left: parent.left
                    top: parent.top
                    topMargin: 12
                }

                color: "white"
                text: "Fitter Happier"
                
                font.family: "Helvetica"
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
                text: "Radiohead"
                
                font.family: "Helvetica"
                font.weight: 300
                font.pixelSize: 16
            }
        }

        }

}