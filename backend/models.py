import backend.query_db 
from PySide6.QtCore import QObject, Signal, Slot, QUrl, QAbstractListModel, Qt, QModelIndex, Property
from PySide6.QtMultimedia import QAudioOutput, QMediaPlayer
from PySide6.QtGui import QGuiApplication
from PySide6.QtQml import QQmlApplicationEngine
import os

os.environ["QT_LOGGING_RULES"] = "qt.multimedia.*=false"


class Backend(QObject):
    artistNameChanged = Signal()
    currentAlbumChanged = Signal()
    albumNameChanged = Signal()
    trackLengthChanged = Signal()

    def __init__(self, album_model, track_model):
        super().__init__()
        self._album_model = album_model
        self._track_model = track_model

        self._artist_name = ""
        self._album_name = ""
        
        self._current_album_id = ""
        
        self._track_length = ""


    def getTrackLength(self):
        return self._track_length
    
    def setTrackLength(self, value):
        if self._track_length != value:
            self._track_length = value
            self.trackLengthChanged.emit()

    trackLength = Property(str, getTrackLength, setTrackLength, notify=trackLengthChanged)

    def getAlbumName(self):
        return self._album_name
    
    def setAlbumName(self, value):
        if self._album_name != value:
            self._album_name = value
            self.albumNameChanged.emit()

    albumName = Property(str, getAlbumName, setAlbumName, notify=albumNameChanged)

    def getArtistName(self):
        return self._artist_name

    def setArtistName(self, value):
        if self._artist_name != value:
            self._artist_name = value
            self.artistNameChanged.emit()

    def getCurrentAlbumId(self):
        return self._current_album_id

    def setCurrentAlbumId(self, value):
        if self._current_album_id != value:
            self._current_album_id = value
            self.currentAlbumChanged.emit()

    # def playTrack(self, trackPath):
        

    currentAlbumId = Property(str, getCurrentAlbumId, setCurrentAlbumId, notify=currentAlbumChanged)


    @Slot(str)
    def buttonSelected(self, type):
        print(type)

    @Slot(int)
    def selectArtist(self, artist_id):
        albums = backend.query_db.fetch_albums(artist_id) 
        self._album_model.set_items(albums)
        self.setArtistName(backend.query_db.fetch_artist(artist_id))

    artistName = Property(str, getArtistName, setArtistName, notify=artistNameChanged)

    @Slot(int)
    def selectAlbum(self, album_id):
        tracks = backend.query_db.fetch_tracks(album_id)  
        self._track_model.set_items(tracks)
        self.setAlbumName(backend.query_db.fetch_album_name(album_id))
        self.setCurrentAlbumId(str(album_id))



class Player(QObject):
    titleChanged = Signal()
    artistChanged = Signal()
    albumChanged = Signal()
    coverPathChanged = Signal()
    trackPathChanged = Signal()
    isPlayingChanged = Signal()
    positionChanged = Signal()
    durationChanged = Signal()
    volumeChanged = Signal()
    playIconPathChanged = Signal()
    
    def __init__(self):
        super().__init__()
        self._media_player = QMediaPlayer()
        self._audio_output = QAudioOutput()
        self._media_player.setAudioOutput(self._audio_output)

        self._title = ""
        self._artist = ""
        self._playIconPath = "../assets/icons/play-solid-full.svg"
        self._album = ""
        self._track_path = "" 
        self._cover_path = ""

        self._media_player.playingChanged.connect(self.isPlayingChanged)
        self._media_player.positionChanged.connect(self.positionChanged)
        self._media_player.durationChanged.connect(self.durationChanged)

    def getTitle(self):
        return self._title
    
    def setTitle(self, value):
        if self._title != value:
            self._title = value
            self.titleChanged.emit()

    title = Property(str, getTitle, setTitle, notify= titleChanged)

    def getArtist(self):
        return self._artist
    
    def setArtist(self, value):
        if self._artist != value:
            self._artist = value
            self.artistChanged.emit()

    artist = Property(str, getArtist, setArtist, notify = artistChanged)

    def getAlbum(self):
        return self._album
    
    def setAlbum(self, value):
        if self._album != value:
            self._album = value
            self.albumChanged.emit()
    
    album = Property(str, getAlbum, setAlbum, notify = albumChanged)

    def getTrackPath(self):
        return self._track_path
    
    def setTrackPath(self, value):
        if self._track_path != value:
            self._track_path = value
            self.trackPathChanged.emit()

    trackPath = Property(str, getTrackPath, setTrackPath, notify = trackPathChanged)

    def getCoverPath(self):
        return self._cover_path

    def setCoverPath(self, value):
        if self._cover_path != value:
            self._cover_path = value
            self.coverPathChanged.emit()
    
    coverPath = Property(str, getCoverPath, setCoverPath, notify = coverPathChanged)

    def getIsPlaying(self):
        return self._media_player.isPlaying()
    
    isPlaying = Property(bool, getIsPlaying, notify= isPlayingChanged)

    def getPosition(self):
        return self._media_player.position() # ms
    
    position = Property(int, getPosition, notify = positionChanged)

    def getDuration(self):
        return self._media_player.duration() # ms
    
    duration = Property(int, getDuration, notify=durationChanged)

    def getVolume(self):
        return self._audio_output.volume() # 0-1
    
    def setVolume(self, value):
        self._audio_output.setVolume(value)
        self.volumeChanged.emit()

    volume = Property(int, getVolume, notify=volumeChanged)

    @Slot(str, str, str, str, str)
    def playTrack(self, track_path, title, artist, album, cover_path):
        
        self._media_player.setSource(QUrl.fromLocalFile(track_path))
        self.setPlayIconPath("../assets/icons/pause-solid-full.svg")
        self.setTitle(title)
        self.setArtist(artist)
        self.setAlbum(album)
        self.setCoverPath(cover_path)

        self._media_player.play()
    
    def getPlayIconPath(self):
        return self._playIconPath
    
    def setPlayIconPath(self, value):
        if self._playIconPath != value:
            self._playIconPath = value
            self.playIconPathChanged.emit()
            
    playIconPath = Property(str, getPlayIconPath, setPlayIconPath, notify= playIconPathChanged)

    @Slot()
    def togglePlay(self):
        if self._media_player.isPlaying():
            self.setPlayIconPath("../assets/icons/pause-solid-full.svg")
            self._media_player.pause()
        else: 
            self._media_player.play()     
            self.setPlayIconPath("../assets/icons/pause-solid-full.svg")
            

    @Slot(int)
    def seek(self, position):
        self._media_player.setPosition(position)       


class ArtistModel(QAbstractListModel):
    IdRole = Qt.UserRole + 1
    NameRole = Qt.UserRole +2

    def __init__(self):
        super().__init__()
        self._items = []
        self.refresh()

    def rowCount(self, parent=QModelIndex()):
        return len(self._items)
    
    def data(self, index, role):
        id, name = self._items[index.row()]

        if role == self.NameRole:
            return name
        if role == self.IdRole:
            return id
        return None
    
    def roleNames(self):
        return {
            self.NameRole: b"name",
            self.IdRole: b"artistId"
        }

    @Slot()
    def refresh(self):
        rows = self.list_artists()   
        self.beginResetModel()
        self._items = rows
        self.endResetModel()

    def list_artists(self):
        return backend.query_db.list_artists()
    
class AlbumModel(QAbstractListModel):
    IdRole = Qt.UserRole + 1
    NameRole = Qt.UserRole + 2
    TrackCountRole = Qt.UserRole + 3

    def __init__(self):
        super().__init__()
        self._items = []

    def rowCount(self, parent=QModelIndex()):
        return len(self._items)
    
    def data(self, index, role):
        if not index.isValid() or index.row() >= len(self._items):
            return None
        album_id, name, track_count = self._items[index.row()]
        if role == self.IdRole:
            return album_id
        if role == self.NameRole:
            return name
        if role == self.TrackCountRole:
            return track_count
        return None

    def roleNames(self):
        return {
            self.IdRole: b"albumId",
            self.NameRole: b"albumName",
            self.TrackCountRole: b"trackCount"
        }
    
    def set_items(self, rows):
        self.beginResetModel()
        self._items = rows
        self.endResetModel()
    

class TrackModel(QAbstractListModel):
    IdRole = Qt.UserRole + 1 
    TitleRole = Qt.UserRole + 2
    PathRole = Qt.UserRole + 3
    LengthRole = Qt.UserRole + 4

    def __init__(self):
        super().__init__()
        self._items = []  # list of (id, title) tuples

    def rowCount(self, parent=QModelIndex()):
        return len(self._items)

    def data(self, index, role):
        if not index.isValid() or index.row() >= len(self._items):
            return None
        track_id, title, path, length = self._items[index.row()]
        if role == self.IdRole:
            return track_id
        if role == self.TitleRole:
            return title
        if role == self.PathRole:
            return path
        if role == self.LengthRole:
            minutes = length // 60
            seconds = length % 60
            if seconds < 10:
                return f"{minutes}:0{seconds}"
            return f"{minutes}:{seconds}"
        return None

    def roleNames(self):
        return {
            self.IdRole: b"trackId",
            self.TitleRole: b"trackTitle",
            self.PathRole: b"trackPath",
            self.LengthRole: b"trackLength"
        }

    def set_items(self, rows):
        self.beginResetModel()
        self._items = rows
        self.endResetModel()