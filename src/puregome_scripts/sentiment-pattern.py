#!/usr/bin/env python3
"""
    sentiment.py: estimate sentiment of individual tweets
    usage: sentiment.py < file.json
    20200514 erikt(at)xs4all.nl
"""

import json
import re
import sys
from pattern.nl import sentiment
from nltk.tokenize import TweetTokenizer
sys.path.append("/home/erikt/projects/puregome/notebooks")
from library import getTweetText

DUTCH = "nl"
LANG = "lang"
IDSTR = "id_str"
COMMA = ","
NEUTRAL = "NEUTRAL"
POSITIVE = "POSITIVE"
NEGATIVE = "NEGATIVE"
POSITIVETOKEN = "<+>"
NEGATIVETOKEN = "<->"

def removeNewlines(text):
    return(re.sub(r"\n",r" ",text))

def sentimentScore(text,debug=False):
    return(sentiment(text)[0])

debug = len(sys.argv) > 1
for line in sys.stdin:
    jsonData = json.loads(line)
    tweetText = removeNewlines(getTweetText(jsonData))
    tweetLang = jsonData[LANG]
    tweetId = jsonData[IDSTR]
    if tweetLang == DUTCH:
        print(tweetId,sentimentScore(tweetText,debug),sep=COMMA)
