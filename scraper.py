import json
import lyricsgenius as genius
import os

with open("access_token.txt") as f:
    api_key = f.readlines()[0].strip()
    api = genius.Genius(api_key)

def get_artist_songs(artist_name):
    artist = api.search_artist(artist_name, max_songs=1000)
    filename = "lyrics/" + artist_name
    artist.save_lyrics(filename=filename, format="json")

with open("artists.json") as f:
    artists = json.load(f)

for genre in artists["genres"]:
    for i in range(len(artists["genres"][genre])):
        if (os.path.isfile("lyrics/" + artists["genres"][genre][i] +".json")):
            print("File already exists for " + artists["genres"][genre][i] + ", skipping!")
        else:
            print("Getting lyric data for " + artists["genres"][genre][i])
            get_artist_songs(artists["genres"][genre][i])
