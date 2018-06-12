import json
import os

trash = [
    "snippet",
    "tracklist",
    "album art",
    "cover art",
    "live at",
    "remix",
    "medley",
    "radio edit",
    "credits",
    "version",
    "dub",
    "translation"
    "traduction",
    "türkçe"
    "fix",
    "mix",
    "club",
    "edit",
    "booklet",
    "speech",
    "demo",
    "skit",
    "voicemail",
    "mtv unlugged",
    "intro",
    "interlude",
    "freestyle"
]

output = []

def format_songs(lyrics_object):
    output_object = []
    for i in range(len(lyrics_object["songs"])):
        if any(x in lyrics_object["songs"][i]["title"].lower() for x in trash):
            print("Found naughty song title, popping " + lyrics_object["songs"][i]["title"])
        else:
            print("Adding "  + lyrics_object["songs"][i]["title"])
            output_object += os.linesep.join([s for s in lyrics_object["songs"][i]["lyrics"].splitlines() if s])
    return output_object

with open("artists.json") as f:
    artists = json.load(f)

for genre in artists["genres"]:
    for i in range(len(artists["genres"][genre])):
        if (os.path.isfile("lyrics/" + artists["genres"][genre][i] +".json")):
            with open("lyrics/" + artists["genres"][genre][i] +".json") as f:
                lyrics = json.load(f)
                #output.append(format_songs(lyrics))
                output += format_songs(lyrics)
        else:
            print("Missing artist info")

with open("output.txt", "w") as f:
    for item in output:
        f.write(item)
