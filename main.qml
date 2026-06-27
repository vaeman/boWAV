import QtQuick
import QtQuick.Window
import QtQuick.Layouts
import QtQuick.Controls
import "ui/layouts"

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
        
        Sidebar {
            id: sidebar
            theme:theme
        }
        Central {
            id: central_view
            theme: theme
            anchors {
                left: sidebar.right
                right: now_playing.left
                top: search.bottom
                bottom: parent.bottom
            }
            }

        NowPlaying {
            id: now_playing
            theme: theme
            anchors {
                top: search.bottom
                right: parent.right
            }
            width: theme.playerWidth} 
    }


    Footer {
        id: footer
        theme: theme

        }

}