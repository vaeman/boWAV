import sys
from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QLabel,
    QVBoxLayout,
    QHBoxLayout,
    QProgressBar,
    QPushButton,
    QLineEdit,
    QStackedWidget,
    QTableWidget,
    QTableWidgetItem,
    QHeaderView,
    QAbstractItemView
)
from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtCore import Qt
import dbq
import os


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Bowav")
        self.setFixedSize(350, 500)
        self.drag_pos = None

        self.initUI()

    def closeEvent(self, a0):
        QApplication.closeAllWindows()
        a0.accept()

    def initUI(self):
        
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(0, 15, 0, 0)
        main_layout.setSpacing(0)

        # Album Art Section

        self.cover_art = QLabel()
        self.cover_art.setFixedSize(320,320)

        pixmap = QPixmap("Adventure/cover.jpg")
        self.cover_art.setPixmap(pixmap)
        self.cover_art.setScaledContents(True)
        main_layout.addWidget(self.cover_art,alignment = Qt.AlignCenter)

        # Info Section

        info_widget = QWidget()

        info_widget.setStyleSheet("""
            background: rgb(20,20,20);
        """)

        central_widget.setStyleSheet("background: rgb(20,20,20);")

        info_layout = QVBoxLayout()
        info_layout.setContentsMargins(0,0,0,0)
        
        # TopBar 
        top_layout = QHBoxLayout()
        top_layout.setContentsMargins(0,0,0,0)

        # Track (Artist and Title)

        track = QVBoxLayout()
        track.setSpacing(0)
        track.setContentsMargins(0,0,0,0)

        self.title = QLabel('Days')
        self.title.setAlignment(Qt.AlignCenter)
        self.title.setFixedHeight(25)
        self.title.setAlignment(Qt.AlignBottom)
        self.title.setAlignment(Qt.AlignHCenter)
        self.title.setStyleSheet("""
            background: none;
            color: rgb(200,200,200);
            font-weight: 300;
        """)
        self.title.setFont(QFont("Jetbrains Mono", 12))
        self.title.setFixedWidth(200)

        self.artist_name = QLabel('Television')
        self.artist_name.setFixedHeight(20)
        self.artist_name.setAlignment(Qt.AlignTop)
        self.artist_name.setAlignment(Qt.AlignHCenter)
        self.artist_name.setStyleSheet("""
            background: none;
            color: rgb(100,100,100);
            font-weight: 100;
        """)
        self.artist_name.setFont(QFont("Jetbrains Mono", 10))
        self.artist_name.setFixedWidth(200)

        # search and queue

        self.search_button = QPushButton("S")
        self.search_button.setMaximumWidth(30)
        self.search_button.setStyleSheet("background: none;")
        self.search_button.setFont(QFont("Jetbrains Mono", 10 ))
        self.search_button.clicked.connect(self.open_search)

        self.queue = QPushButton("Q")
        self.queue.setMaximumWidth(30)
        self.queue.setStyleSheet("background: none;")
        self.queue.setFont(QFont("Jetbrains Mono", 10 ))

        track.addWidget(self.title)
        track.setContentsMargins(0,0,0,0)
        track.setSpacing(0)
        track.addWidget(self.artist_name)

        top_layout.addWidget(self.search_button)
        top_layout.addLayout(track)
        top_layout.addWidget(self.queue)

        #bar 

        self.progress_bar = QProgressBar()
        self.progress_bar.setFixedWidth(225)
        self.progress_bar.setFixedHeight(6)
        self.progress_bar.setTextVisible(False)

        self.Ltime  = QLabel("0:01")
        self.Rtime  = QLabel("3:14")

        self.Ltime.setStyleSheet("color:white;")
        self.Ltime.setFont(QFont("Jetbrains Mono", 10))
        self.Rtime.setFont(QFont("Jetbrains Mono", 10))
        self.Rtime.setStyleSheet("color:white;")

        # Center Progress Bar

        progress_layout = QHBoxLayout()
        
        progress_layout.addWidget(self.Ltime) 
        progress_layout.addStretch()
        progress_layout.addWidget(self.progress_bar)
        progress_layout.addStretch()
        progress_layout.addWidget(self.Rtime)
        
        progress_layout.setContentsMargins(10,0,10,0)
        progress_layout.setAlignment(Qt.AlignVCenter)
        progress_layout.setAlignment(Qt.AlignTop)
        
        
        # Controls Placeholder
        self.previous = QPushButton("<=")
        self.play = QPushButton("<||")
        self.next= QPushButton("=>")

        self.previous.setStyleSheet(""" color: white;
                                        background: red;""")
        self.play.setStyleSheet("""     color: white;
                                        background: red;""")    
        self.next.setStyleSheet("""     color: white;
                                        background: red;""")
        
        controls_layout = QHBoxLayout()
        controls_layout.addWidget(self.previous)
        controls_layout.addWidget(self.play)
        controls_layout.addWidget(self.next)

        info_layout.addSpacing(10)
        info_layout.addLayout(top_layout)
        info_layout.addLayout(progress_layout)
        info_layout.addLayout(controls_layout)
        # info_layout.addSpacing(0)
        # info_layout.addWidget(controls)

        info_widget.setLayout(info_layout)
        main_layout.addWidget(info_widget)
        central_widget.setLayout(main_layout)

    # making whole window movable by holding left click anywhere

    def open_search(self):
        self.search_window = Search()
        self.search_window.show()

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.drag_pos = event.globalPos()

    def mouseMoveEvent(self, event):
        if self.drag_pos is not None:
            delta = event.globalPos() - self.drag_pos
            self.move(self.x() + delta.x(), self.y() + delta.y())
            self.drag_pos = event.globalPos()

    def mouseReleaseEvent(self, event):
        self.drag_pos = None
    
# search window

class Search(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("search")
        self.setMinimumSize(700, 500)
        # self.setWindowFlags(Qt.FramelessWindowHint)
        self.drag_pos = None

        self.initUI()
        

    # making whole window movable by holding left click anywhere
    
    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.drag_pos = event.globalPos()

    def mouseMoveEvent(self, event):
        if self.drag_pos is not None:
            delta = event.globalPos() - self.drag_pos
            self.move(self.x() + delta.x(), self.y() + delta.y())
            self.drag_pos = event.globalPos()

    def mouseReleaseEvent(self, event):
        self.drag_pos = None

    def initUI(self):
        # css

        self.setStyleSheet(
            """

            QPushButton {
                background: rgb(50,50,50);
                border: none;
                padding: 10px 10px;
                margin: 0 10px;
                color: white;
                font-size: 18px;
                font-weight: 600;
                font-family: "Jetbrains Mono";
            }            
            
            QPushButton:pressed {
                background: none;
                border: none;
            }
            
            QPushButton:hover {
                color: rgb(200,200,200);
                font-weight: 100;
            }


            QLineEdit {
                color: white;
                font-size: 16px;
                font-family: "Jetbrains Mono";
                font-style: italic;
                border: 1px red;
                margin: 0 10px;
            }
                QTableWidget {
                background: rgb(20,20,20);
                border: none;
                border-right: 1px solid grey;
                padding: 3px;
                color: white;
                selection-background-color: rgb(60,60,60);
                }

                QHeaderView::section {
                    background: rgb(20,20,20);
                    color: rgb(150,150,150);
                    font-family: 'jetbrains mono';
                    border: none;
                }
                QScrollBar:vertical {
                background: transparent;
                color: grey;
                width: 8px;
                margin: 0;
                }

                QScrollBar::handle:vertical {
                    background: rgb(90,90,90);
                    border-radius: 4px;
                    min-height: 30px;
                }

                QScrollBar::handle:vertical:hover {
                    background: rgb(120,120,120);
                }

                QScrollBar::add-line:vertical,
                QScrollBar::sub-line:vertical {
                    height: 0px;
                }

                QScrollBar::add-page:vertical,
                QScrollBar::sub-page:vertical {
                    background: transparent;
                }

            """
        )

        # window layout

        search_window_layout = QVBoxLayout()
        
        search_window_layout.setContentsMargins(0,0,0,0)
        search_window_layout.setSpacing(0)

        # nav bar
        
        nav_bar_widget = QWidget()
        nav_bar_layout = QHBoxLayout()

        nav_bar_widget.setStyleSheet("background: rgb(50,50,50);")
        nav_bar_widget.setFixedHeight(55)

        nav_bar_layout.setContentsMargins(0,0,0,0)
        nav_bar_layout.setSpacing(0)
        
        # search

        search_bar = QLineEdit()
        search_bar.setPlaceholderText("Search...")
        search_bar.setStyleSheet("background: rgb(20,20,20);"
                                 "padding: 5px 3px;"
                                 "border: 1px solid rgb(150,150,150)")
        search_bar.setMaximumWidth(200)

        # artists

        search_artists_button = QPushButton("Artists") 

        # albums

        search_albums_button = QPushButton("Albums") 

        # tracks

        search_tracks_button = QPushButton("Tracks") 

        nav_bar_layout.addWidget(search_bar)
        
        nav_bar_layout.addStretch()
        
        nav_bar_layout.addWidget(search_albums_button)
        nav_bar_layout.addWidget(search_artists_button)
        nav_bar_layout.addWidget(search_tracks_button)

        nav_bar_widget.setLayout(nav_bar_layout)        
        
        # tables 

        tables_widget = QWidget()
        tables_widget.setStyleSheet("background: rgb(20,20,20)")

        tables_layout = QHBoxLayout()
        tables_layout.setContentsMargins(0,0,0,0)
        tables_layout.setSpacing(0)

        # artists table
        artists_table_widget = QWidget()
        artists_table_layout = QVBoxLayout()

        # number of albums

        album_length = dbq.album_len()

        artists_no = QLabel(f"{album_length} Albums")
        artists_no.setStyleSheet("font-size: 16px;"
                                 "color: grey;"
                                 "font-family: 'Jetbrains Mono';")

    

        # album name and artist name

        album_li = dbq.album_list()
        artists_table = QTableWidget(len(album_li),1)

        album_id_li = []

        for i in range(len(album_li)):
            # album cover
            cover_art = QLabel()
            cover_art.setFixedSize(50,50)

            if os.path.isfile(f"covers/{album_li[i][2]}.png"):
                pixmap = QPixmap(f"covers/{album_li[i][2]}.png")
            else:
                pixmap = QPixmap(f"images/ash-baby.png")

            cover_art.setPixmap(pixmap)
            cover_art.setScaledContents(True)

            artists_table_album = QLabel(f"{album_li[i][0]}") 
            artists_table_album.setFixedHeight(20)
            artists_table_album.setContentsMargins(0,0,0,0)
            artists_table_album.setStyleSheet("font-family: 'Jetbrains Mono';"
                                              "color: white;"
                                              "font-size: 16px;"
                                              )
            artists_table_artist = QLabel(f"{album_li[i][1]}")
            artists_table_artist.setFixedHeight(20)
            artists_table_artist.setContentsMargins(0,0,0,0)
            artists_table_artist.setStyleSheet("font-family: 'Jetbrains Mono';"
                                               "color: grey;"
                                               "font-size: 14px;"
                                                )

            artists_wid1 = QWidget() 
            artists_wid1.setStyleSheet("")

            artists_lay1 = QHBoxLayout()
            artists_lay1.setSpacing(0)
            artists_lay1.setContentsMargins(0,0,0,0)

            artist_albuminfo_wid = QWidget()
            artist_albuminfo_lay = QVBoxLayout()
            artist_albuminfo_lay.setSpacing(0)
            artist_albuminfo_lay.setContentsMargins(10,0,0,0)
            artist_albuminfo_lay.addWidget(artists_table_album)
            artist_albuminfo_lay.addWidget(artists_table_artist)
            artist_albuminfo_wid.setLayout(artist_albuminfo_lay)

            artists_lay1.addWidget(cover_art)
            artists_lay1.addWidget(artist_albuminfo_wid)
            artists_wid1.setLayout(artists_lay1)
            artists_wid1.setStyleSheet("")
            
            
            artists_table.setRowHeight(i, 50)
            artists_table.setCellWidget(i,0,artists_wid1)
            
            album_id_li.append(album_li[i][2])

                
        # making table behave
        artists_table.setEditTriggers(QTableWidget.NoEditTriggers)
        artists_table.setSelectionBehavior(QTableWidget.SelectRows)
        artists_table.setFocusPolicy(Qt.NoFocus)
        artists_table.horizontalHeader().setVisible(False)
        artists_table.setSortingEnabled(True)
        artists_table.horizontalHeader().setHighlightSections(False)
        artists_table.setMaximumWidth(500)
        artists_table.setColumnWidth(0, artists_table.size().width())
        artists_table.verticalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Fixed)
        artists_table.verticalHeader().setStyleSheet("color: red;")
        artists_table_layout.addWidget(artists_no)
        artists_table_layout.addWidget(artists_table)

        artists_table_widget.setLayout(artists_table_layout)
        tables_layout.addWidget(artists_table_widget)            

        # tracks table
        tracks_table_widget = QWidget()
        tracks_table_layout = QVBoxLayout()

        tracks_table = QTableWidget()

        tracks_no = QLabel(f"{dbq.tracks()[0][0]} Tracks")
        tracks_no.setStyleSheet("font-size: 16px;"
                                 "color: grey;"
                                 "font-family: 'Jetbrains Mono';")                


        tracks_table.setSelectionBehavior(QTableWidget.SelectRows)
        tracks_table.setEditTriggers(QTableWidget.NoEditTriggers)
        tracks_table.setFocusPolicy(Qt.NoFocus)
        tracks_table.horizontalHeader().setVisible(False)
        tracks_table.setSortingEnabled(True)
        tracks_table.horizontalHeader().setHighlightSections(False)
        tracks_table.setMaximumWidth(500)
        tracks_table.setColumnWidth(0, artists_table.size().width())
        
        tracks_table.verticalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Fixed)
        tracks_table.verticalHeader().setStyleSheet("color: red;")
        
        tracks_table_layout.addWidget(tracks_no)
        tracks_table_layout.addWidget(tracks_table)

        tracks_table_widget.setLayout(tracks_table_layout)
        artists_table_widget.setLayout(artists_table_layout)
        
        tables_layout.addWidget(tracks_table_widget)
        tables_layout.addWidget(artists_table_widget)

        tables_layout.addWidget(tracks_table)
        tables_widget.setLayout(tables_layout)



        search_window_layout.addWidget(nav_bar_widget)
        search_window_layout.addWidget(tables_widget)
        
        self.setLayout(search_window_layout)


def main():
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec_())



if __name__ == "__main__":
    main()