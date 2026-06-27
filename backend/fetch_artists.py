from PySide6.QtSql import QSqlDatabase, QSqlTableModel
from PySide6.QtQml import QQmlApplicationEngine
import sqlite3

# db = QSqlDatabase.addDatabase("QSQLITE")
# db.setDatabaseName("../data.db")
# db.open()

# model = QSqlTableModel()
# model.setTable("songs")
# model.select()

# engine = QQmlApplicationEngine()

# engine.rootContext().setContextProperty("musicModel", model)

conn = sqlite3.connect("D:/Vibhu/Code/Python/Music/data.db")
cur = conn.cursor()

def count_albums():
    cur.execute("SELECT COUNT(*) FROM albums")
    length = cur.fetchall()
    return length[0][0]

def count_tracks():
    cur.execute("SELECT COUNT(*) FROM songs")
    return cur.fetchall()[0][0]

def count_artists(): 
    cur.execute("SELECT COUNT(*) FROM artists")
    return cur.fetchall()[0][0]


def list_artists(): # show all artists
    cur.execute("SELECT id, artist FROM artists")
    return cur.fetchall()

def list_albums(): # show all albums
    cur.execute("SELECT albums.album, artists.artist, albums.id, artists.id FROM albums JOIN artists ON albums.artist_id = artists.id")
    # li = set(item[0] for item in cur.fetchall())
    return cur.fetchall()

def fetch_tracks(album_id = None, artist_id = None): # show songs based on album id or artist id 
    if album_id is not None:
        cur.execute("SELECT songs.id, songs.path, songs.title, artists.artist, albums.album, songs.length, albums.id FROM songs JOIN artists ON songs.artist_id = artists.id JOIN albums ON songs.album_id = albums.id WHERE songs.album_id = ?",(album_id,))
        return cur.fetchall()
    else:
        cur.execute("SELECT songs.id, songs.path, songs.title, artists.artist, albums.album, songs.length FROM songs JOIN artists ON songs.artist_id = artists.id JOIN albums ON songs.album_id = albums.id WHERE songs.artist_id = ?",(artist_id,))
        return cur.fetchall()
    
def fetch_albums(artist_id):
    cur.execute("SELECT albums.id, albums.album, COUNT(songs.id) FROM albums LEFT JOIN SONGS on albums.id = songs.album_id WHERE albums.artist_id = ? GROUP BY albums.id, albums.album", (artist_id,))
    return cur.fetchall()

