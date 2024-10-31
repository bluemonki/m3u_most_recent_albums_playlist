
import sys
from os import walk
from os import path
import random

root = "/home/john/Music/" if len(sys.argv) == 1 else sys.argv[1] 

if False == path.isdir(root):
    raise Exception(("'{}' is not a valid directory".format(root)))

# force add a trailing slash
root = path.join(root, '') 

albums = []
for (dirpath, dirnames, filenames) in walk(root):
    if len(dirnames) == 0:
        albums.append(dirpath)

albums.sort(key=lambda x: path.getmtime(x))

albums = albums[-5:]

mp3s = []

for album in albums: 
    for (dirpath, dirnames, filenames) in walk(album):
        for filename in filenames:
            mp3s.append(album + "/" + filename)

random.shuffle(mp3s)

# stdout for cli shenanigans
for mp3 in mp3s:
    print(mp3)
