import QtQuick
import QtQuick.Window
import QtQuick.Layouts
import QtQuick.Controls
import "layouts"

ApplicationWindow {
    height: 720
    width: 1280
    visible: true
    visibility: Window.Maximized
    title: "BoWAV"
    color: "#0a0908"

    Theme {id: theme}

    Rectangle {
        id: main
        anchors {
            top: parent.top
            left: parent.left
            right: parent.right
        }
        color: "Green"
        height: Window.height - theme.footerHeight
        
        Search {id: search
                theme: theme}
        
        Rectangle {
            anchors {
                left: parent.left
                right: parent.right
                top: search.bottom
            }
            height: 1
            color: "#282828"
        }

        Sidebar {
            id: sidebar
            theme:theme
            onButtonSelected: function(labelName) {
                central_view.stack.replace(pageComponents[labelName])
            }
            anchors{
                topMargin: 1
                top: search.bottom
                left: parent.left
            }
        }
        Rectangle {
            anchors {
                right: sidebar.right
                top: search.bottom
                bottom: footer.top
            }
            width: 1
            color: "#282828"
        }
        Central {
            id: central_view
            theme: theme
            anchors {
                topMargin: 1
                left: sidebar.right
                right: now_playing.left
                top: search.bottom
                bottom: parent.bottom
            }
            }
        Rectangle {
            anchors {
                right: now_playing.left
                top: search.bottom
                bottom : parent.bottom
            }
            width: 1
            color: "#282828"
        }
        NowPlaying {
            id: now_playing
            theme: theme
            anchors {
                topMargin: 1
                top: search.bottom
                right: parent.right
            }
            width: theme.playerWidth} 

                    Rectangle {
            anchors {
                left: parent.left
                right: parent.right
                bottom: footer.top
            }
            height: 1
            color: "#282828"
            }

            Footer {
                id: footer
                theme: theme

                anchors {
                    top: parent.bottom
                    left: parent.left
                    right: parent.right
                }
            }
    }




}