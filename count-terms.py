#!/usr/bin/env python3
"""
    count-terms.py: count tweets that contain specific term
    usage: count-term.py term < file.json
    20200424 erikt(at)xs4all.nl
"""

import json
import re
import sys
sys.path.append("/home/erikt/projects/puregome/notebooks")
from library import getTweetText
from library import getTweetDate

DUTCH = "nl"
LANG = "lang"
USAGE = "count-term.py term < file.json"

def removeNewlines(text):
    return(re.sub(r"\n",r" ",text))

try: term = sys.argv[1]
except: sys.exit(USAGE)

counts = {term:{}}
for line in sys.stdin:
    jsonData = json.loads(line)
    tweetText = removeNewlines(getTweetText(jsonData))
    tweetDate = getTweetDate(jsonData)
    tweetLang = jsonData[LANG]
    if re.search(r"\b"+term+r"\b",tweetText,flags=re.IGNORECASE) and tweetLang == DUTCH:
        counts[term][tweetDate] = counts[term][tweetDate]+1 if tweetDate in counts[term] else 0
print(counts)
