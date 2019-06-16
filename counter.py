import json
import os
import collections


trash = [
]

with open("artists.json") as f:
    artists = json.load(f)

for genre in artists["genres"]:
    for i in range(len(artists["genres"][genre])):
        if (os.path.isfile("lyrics/" + artists["genres"][genre][i] +".txt")):
            with open("lyrics/" + artists["genres"][genre][i] +".txt") as f:
                wordcount = {}
                words = f.read().split()
                words = [word.lower() for word in words]
                wordcount = collections.Counter(words)
                for word in trash:
                    del wordcount[word]
                common = wordcount.most_common(1000)
                output = []
                for wordtup in common:
                    output.append({wordtup[0]: wordtup[1]})
                with open("reports/" + artists["genres"][genre][i] + "-report.json", "w") as f:
                    f.write(json.dumps(output))
        else:
            print("Missing artist info")
