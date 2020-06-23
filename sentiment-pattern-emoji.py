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
sys.path.append("/home/cloud/projects/puregome/notebooks")
from library import getTweetText
sys.path.append("/home/cloud/projects/puregome/scripts")
import emoticons

DUTCH = "nl"
LANG = "lang"
IDSTR = "id_str"
COMMA = ","
NEUTRAL = "NEUTRAL"
POSITIVE = "POSITIVE"
NEGATIVE = "NEGATIVE"
POSITIVETOKEN = "<+>"
NEGATIVETOKEN = "<->"

def emojiToText(text):
    for emoji in emoticons.emoticons:
        text = re.sub(emoji," "+emoticons.emoticons[emoji]+" ",text)
    return(text)

def removeNewlines(text):
    return(re.sub(r"\n",r" ",text))

def sentimentScore(text):
    return(sentiment(text)[0])

for line in sys.stdin:
    jsonData = json.loads(line)
    tweetText = removeNewlines(getTweetText(jsonData))
    tweetLang = jsonData[LANG]
    tweetId = jsonData[IDSTR]
    if tweetLang == DUTCH:
        tweetTextEmoji = emojiToText(tweetText)
        print(tweetId,sentimentScore(tweetTextEmoji),sep=COMMA)
