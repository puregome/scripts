#!/usr/bin/env python3
"""
    get-tweets-by-ids.py: get tweets from files given ids
    usage: get-tweet-ids.py id1 [id2 ...] < idStrFile.csv
    note: idStrFile.csv contain idStr minimum and maximum per file
    20200709 erikt(at)xs4all.nl
"""

import gzip
import json
import sys

DATADIR="/home/erikt/media/20160616/twitter/"
IDSTR = "id_str"
MIN = "min"
MAX = "max"

files = {}
for line in sys.stdin:
    try:
        fileName,idStrMin,idStrMax = line.split(",")
        files[fileName] = {MIN:int(idStrMin),MAX:int(idStrMax)}
    except: pass

for idStrTarget in sys.argv[1:]:
    idStrTarget = int(idStrTarget)
    idStrFound = False
    for fileName in files.keys():
        if idStrTarget >= files[fileName][MIN] and \
           idStrTarget <= files[fileName][MAX]:
            inFile = gzip.open(DATADIR+fileName,"r")
            for line in inFile:
                try:
                    jsonData = json.loads(line)
                    idStr = int(jsonData[IDSTR])
                    if idStr == idStrTarget:
                        print(line.decode("utf"),end="")
                        idStrFound = True
                        break
                except: pass
            inFile.close()
            if idStrFound: break 
