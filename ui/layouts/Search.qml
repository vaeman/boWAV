import QtQuick
import QtQuick.Controls

import "../"

Rectangle {
    required property Theme theme

    anchors {
        top: parent.top
        left: parent.left
        right: parent.right
    }
    
    Rectangle {
        id: folder

        anchors {
            left: parent.left
            top: parent.top
            bottom: parent.bottom
            leftMargin: 10
        }
        

        Text {
            anchors.verticalCenter: parent.verticalCenter

            text: "Playing from: D:/Music"

            color: "#909090"
            font.family: "Helvetica Neue"
            font.weight: 600
            }
        }

    Rectangle {
        id: home

        width: 35

        anchors {
            top: parent.top
            bottom: parent.bottom
            right: search.left
            rightMargin: 40
        }
        color: "transparent"
        Rectangle {
            anchors.verticalCenter: parent.verticalCenter
            width: 35
            height: 35
            radius: 10
            color: "#282828"

            Image {
                height: 30
                width: 30

                anchors.centerIn: parent

                source: "../assets/icons/house-regular-full.svg"
                
            }

        }
        
    }

    Rectangle {
        id: search

        color: "#282828"
        width: 600
        height: 30
        radius: 4
        border {
            width: 1
            color: "#565656"
        }
        anchors.centerIn: parent

        TextField {

            anchors {
                fill: parent
                verticalCenter: parent.verticalCenter
                // topMargin: 6
                // leftMargin: 20
            }

            leftPadding: 20
            topPadding: 8

            // border: 0
            
            // background: Rectangle {
            //     color: "transparent"
            //     border.width: 0
            // }

            placeholderText: "Search.."
            color: "#909090"
            font.family: "Helvetica Neue"
            font.weight: 600

        }
        }
    
    height: theme.headerHeight
    color: "#151515"}