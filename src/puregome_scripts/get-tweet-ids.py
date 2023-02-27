#!/usr/bin/env python3
"""
    get-tweet-ids.py: extract lowest and highest tweet id from file
    usage: get-tweet-ids.py file1.out.gz [file2.out.gz ...]
    20200709 erikt(at)xs4all.nl
"""

import gzip
import json
import sys

IDSTR = "id_str"

for inFileName in sys.argv[1:]:
    lowestIdstr = ""
    highestIdstr = ""
    try:
        inFile = gzip.open(inFileName,"r")
        for line in inFile:
            try:
                jsonData = json.loads(line)
                idstr = int(jsonData[IDSTR])
                if lowestIdstr == "":
                    lowestIdstr = idstr
                    highestIdstr = idstr
                elif idstr < lowestIdstr: lowestIdstr = idstr
                elif idstr > highestIdstr: highestIdstr = idstr
            except: pass
        inFile.close()
        print(inFileName,lowestIdstr,highestIdstr,sep=",")
    except: pass
