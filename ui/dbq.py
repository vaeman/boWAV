import sqlite3

conn = sqlite3.connect("data.db")
cur = conn.cursor()

cur.execute("drop table artists")
cur.execute("drop table albums")
cur.execute("drop table songs")
cur.execute("CREATE TABLE songs(id INTEGER PRIMARY KEY, title STRING, length INT, path STRING, genre STRING, artist_id INT, album_id INT, FOREIGN KEY (artist_id) REFERENCES artists(id), FOREIGN KEY (album_id) REFERENCES albums(id))")
cur.execute("CREATE TABLE albums(id INTEGER PRIMARY KEY, album STRING, artist_id INT)")
cur.execute("CREATE TABLE artists(id INTEGER PRIMARY KEY, artist STRING)")

def album_len():
    cur.execute("SELECT COUNT(*) FROM albums")
    length = cur.fetchall()
    print(length)
    return length[0][0]

def album_list():
    cur.execute("SELECT albums.album, artists.artist, albums.id from albums join artists on albums.artist_id = artists.id")
    # li = set(item[0] for item in cur.fetchall())
    return cur.fetchall()
    
def tracks():
    cur.execute("SELECT count(*) FROM songs")
    return cur.fetchall()
# album_list()

def fetch_songs(album_id = None, artist_id = None):
    if album_id is not None:
        cur.execute("SELECT songs.title, artists.artist, albums.album, songs.length FROM songs JOIN artists ON songs.artist_id = artists.id JOIN albums ON songs.album_id = albums.id WHERE songs.album_id like ?",(album_id,))
        return cur.fetchall()

    
def artist_list():
    cur.execute("SELECT artist FROM artists")
    return cur.fetchall()

