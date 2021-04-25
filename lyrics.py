import lyricsgenius
from os import system, name



#Access Code
genius = lyricsgenius.Genius("8nAj0wf8E4crmKV51JmotTw23m7ECfGGLgySDpEiQSDSiBbpA8aV9U4zD9JI8HPt")
ch='69'
while(ch!='q'):
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

# Inputs
    artist = input ("Enter Artist :")
    song = input ("Enter Song Name :")

# Search Song Lyrics
    ding = genius.search_song(song, artist)

# Print The Lyrics
    print(ding.lyrics)
#Close The Program
    ch = input("Enter q to exit or ENTER to try another song")
