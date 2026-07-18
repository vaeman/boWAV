import mutagen
from mutagen.easyid3 import EasyID3
from mutagen.flac import FLAC
from mutagen.mp4 import MP4
from mutagen.oggvorbis import OggVorbis
from mutagen.id3 import ID3
from mutagen.wave import WAVE
import sqlite3
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


# scans the given folder, stores it in a database

def scan(folder):
    conn = sqlite3.connect(os.path.join(BASE_DIR, "../data.db"))
    cursor = conn.cursor()

    SUPPORTED = {".mp3", ".flac", ".ogg", ".wav", ".m4a"}
    count = 0

    cursor.execute("SELECT path FROM songs") # fetching all songs in database for comparison
    songs_path = set(item[0] for item in cursor.fetchall())

    cursor.execute("SELECT artist FROM artists")
    artist_names = set(item[0] for item in cursor.fetchall())

    cursor.execute("SELECT id, album, artist_id FROM albums")
    album_names = set(item[0] for item in cursor.fetchall())

    # print(artist_table, album_table)

    for root, dirs, files in os.walk(folder): #walking through every item in the root folder,  
        
        for file in files:
            track_path = os.path.join(root, file) 
            
            if os.path.isfile(track_path): # if the given path is a file
                ext = os.path.splitext(file)[1].lower()
                
                if ext in SUPPORTED: # if the given file is an audio file
                    try:

                        if track_path not in songs_path: # if path is not in our db (file is new)
                                                    
                            song = get_metadata(track_path) # created a track object 

                            songs_path.add(track_path)
                            song.album.replace('"','')

                            if song.artist not in artist_names: # if artist of song is not known
                                
                                cursor.execute("INSERT INTO artists (artist) VALUES (?)", (song.artist,))
                                artist_id = cursor.lastrowid
                                
                                artist_names.add(song.artist)
                                

                                # print(f"artist_id: {artist_id}, album_id: {album_id}")
                    
                                cursor.execute("INSERT INTO albums (album,artist_id) VALUES (?,?)", (song.album,artist_id))
                                album_id = cursor.lastrowid

                                album_names.add(song.album)

                                cursor.execute("INSERT INTO songs (title, length, path, genre, album_id, artist_id) VALUES (?,?,?,?,?,?)", (song.title, song.length, song.path, song.genre, album_id, artist_id))
                                # conn.commit()
                                try:
                                    get_cover(track_path, album_id)
                                except Exception as e:
                                    print(e)
                                    pass
                            
                            elif song.album not in album_names: # if artist is known but album is not 
                                
                                album_names.add(song.album)

                                cursor.execute("SELECT id from artists WHERE artist = (?)", (song.artist,))
                                artist_id = cursor.fetchone()[0]
                                # print(f"artist_id: {artist_id}, album_id: {album_id}")

                                cursor.execute("INSERT INTO albums (album,artist_id) VALUES (?,?)", (song.album, artist_id))
                                album_id = cursor.lastrowid
                                
                                cursor.execute("INSERT INTO songs (title, length, path, genre, album_id, artist_id) VALUES (?,?,?,?,?,?)", (song.title, song.length, song.path, song.genre,album_id, artist_id))
                                # conn.commit()

                                # album cover
                                try:
                                    get_cover(track_path, album_id)
                                except Exception as e:
                                    print(e)
                                    pass
                            else: # both are known, we just add song into db
                                cursor.execute("SELECT id from albums WHERE album = (?)", (song.album,))
                                album_id = cursor.fetchone()[0]
                                
                                cursor.execute("SELECT id from artists WHERE artist = (?)", (song.artist,))
                                artist_id = cursor.fetchone()[0]
                                # # print(f"artist_id: {artist_id}, album_id: {album_id}")
                                
                                cursor.execute("INSERT INTO songs (title, length, path, genre, album_id, artist_id) VALUES (?,?,?,?,?,?)", (song.title, song.length, song.path, song.genre,album_id, artist_id))
                                # conn.commit()
                            
                            count+=1
                        else:
                            continue
                    except Exception as e:
                        print(f"Skipping {track_path}: {e}")
                        continue
    
    conn.commit()

    cursor.execute("SELECT id, path FROM songs")
    songs = cursor.fetchall()  # list of (id, path) tuples

    delcount = 0
    for song_id, path in songs:
        if not os.path.isfile(path):
            cursor.execute("DELETE FROM songs WHERE id = ?", (song_id,))
            delcount+=1

    cursor.execute("DELETE FROM artists WHERE id NOT IN (SELECT artist_id FROM songs)")
    cursor.execute("DELETE FROM albums WHERE id NOT IN (SELECT album_id FROM songs)")
    conn.commit()

    print(f"Scan completed, {count} songs added, {delcount} songs removed")
# -> GETTING TRACK METADATA

class Track:

    def __init__ (self, length, title, path, album, artist, genre, year):
        self.length = length
        self.title = title
        self.path = path
        self.album = album
        self.artist = artist
        self.genre = genre
        self.year = year

        
def get_metadata(track_path): # gets song metadata (title, length, artist etc)
    
    track = mutagen.File(track_path) # type: ignore
    if track is None:
        raise ValueError(f"Could not read audio file: {track_path}")
    track_length = int(track.info.length)
    ext = os.path.splitext(track_path)[1].lower()

    if ext == ".mp3" or ext == ".flac":
        track = EasyID3(track_path) if ext == ".mp3" else FLAC(track_path)
        track_title = (track.get("title") or ["Unknown"])[0]
        track_artist = (track.get("artist") or ["Unknown"])[0]
        track_album = (track.get("album") or ["Unknown"])[0]
        track_genre = (track.get("genre") or ["Unknown"])[0]
        track_year = (track.get("year") or ["Unknown"])[0]
    
    elif ext == ".ogg":
        track = OggVorbis(track_path)
        track_title = (track.get("title") or ["Unknown"])[0]
        track_artist = (track.get("artist") or ["Unknown"])[0]
        track_album = (track.get("album") or ["Unknown"])[0]
        track_genre = (track.get("genre") or ["Unknown"])[0]
        track_year = (track.get("year") or ["Unknown"])[0]

    
    elif ext == ".m4a" or ext == ".mp4":
        track = MP4(track_path)
        track_title = (track.get("©nam") or ["Unknown"])[0]
        track_artist = (track.get("©ART") or ["Unknown"])[0]
        track_album = (track.get("©alb") or ["Unknown"])[0]
        track_year = (track.get("year") or ["Unknown"])[0]
        track_genre = (track.get("©gen") or ["Unknown"])[0]
        # metadata = track.tags
        # print(metadata.pprint())

    split = track_artist.split(" ")

    # removing featured artist from the maain artist name

    for i in range(len(split)): 

        if split[i].lower() in ("feat.", "feat", "ft.", "featuring", "ft"):
            track_artist = ""
            
            for j in range(i):
                track_artist += split[j] + " "
            track_artist = track_artist.rstrip()
        
        else:
            continue
    
    return Track(track_length, track_title, track_path, track_album, track_artist, track_genre, track_year)


def get_cover(track_path,album_id):

    ext = os.path.splitext(track_path)[1].lower() 
    data = None

    if ext == ".mp3":
        tags = ID3(track_path)
        cover = tags.get("APIC:")
        if cover != None:
            data = cover.data
            with open(os.path.join(BASE_DIR, f"../ui/assets/covers/{album_id}.png"), "wb") as f:
                f.write(data)
        else:
            print(album_id)
    elif ext == ".flac":
        tags = FLAC(track_path)
        if len(tags.pictures) != 0:
            data = tags.pictures[0].data
            with open(os.path.join(BASE_DIR, f"../ui/assets/covers/{album_id}.png"), "wb") as f:
                f.write(data)
        else:
            print(album_id)
            
    elif ext == ".wav":
        tags = WAVE(track_path)
        art = tags.get("APIC:")
        if art != None:
            data = art.data
            with open(os.path.join(BASE_DIR, f"../ui/assets/covers/{album_id}.png"), "wb") as f:
                f.write(data)
        else:
            print(album_id)
    elif ext == ".m4a":
        tags = MP4(track_path)
        covr = tags.get("covr")
        if covr:
            data = bytes(covr[0])
            with open(os.path.join(BASE_DIR, f"../ui/assets/covers/{album_id}.png"), "wb") as f: 
                f.write(data)

    
    # check folder
    if data is None:
        folder = os.path.dirname(track_path)
        for name in ("cover", "folder", "front", "album", "artwork"):
            for img_ext in (".jpg", ".jpeg", ".png"):
                candidate = os.path.join(folder, name + img_ext)
                if os.path.isfile(candidate):
                    with open(candidate, "rb") as f:
                        data = f.read()
                    break
            if data:
                break
    if data:
        with open(os.path.join(BASE_DIR, f"../ui/assets/covers/{album_id}.png"), "wb") as f:
            f.write(data)
    else:
        print(f"No cover found for album_id {album_id}")
    
    
scan("D:/Music/")