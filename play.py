import vlc
import sqlite3
import threading
import time



player = vlc.MediaPlayer()

def play(path):
    media = vlc.Media(path)
    player.set_media(media)
    player.play()

def pause():
    player.pause()  

# queue system
# 1. ALBUMS
#   -> user plays album
#   -> add all songs to the queue 
#   -> anything else can be added to the queue

# Q: How does one implement the queue???? While True?

class Queue:

    def __init__(self):
        self.songs = []
        self.current_index = 0
    
    def add(self, song):
        self.songs.append(song)
    
    def remove(self,index):
        self.songs.pop(index)
    
    def length(self):
        return len(self.songs)
    
    def current(self):
        return self.songs[self.current_index]
    
    def next(self):
        if self.current_index < len(self.songs):
            self.current_index+=1
    
    def previous(self):
        if self.current_index > 0:
            self.current_index-=1
        

q = Queue
q.add(q,song="Song1")
q.add(q,song="Song1")
q.add(q,song="Song1")
q.add(q,song="Song1")
print(q.current())
# def play_album(album):
#     conn = sqlite3.connect("data.db")
#     cursor = conn.cursor()
#     cursor.execute("select * from songs join albums on songs.album_id = albums.id where albums.album like LOWER((?))", (f"%{album}%",))
#     tracks = cursor.fetchall()
#     print(tracks)