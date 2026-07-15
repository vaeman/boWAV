import backend.query_db 
from PySide6.QtCore import QObject, Signal, Slot, QUrl, QAbstractListModel, Qt, QModelIndex, Property
from PySide6.QtGui import QGuiApplication
from PySide6.QtQml import QQmlApplicationEngine

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