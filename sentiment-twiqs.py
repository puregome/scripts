#!/usr/bin/env python3
"""
    sentiment.py: estimate sentiment of individual tweets
    usage: sentiment.py < file.json
    20200514 erikt(at)xs4all.nl
"""

import json
import re
import sys
from nltk.tokenize import TweetTokenizer
sys.path.append("/home/erikt/projects/puregome/notebooks")
from library import getTweetText

POSITIVEWORDS = "hoera gelukkig blij vrolijk vrolijke vrolijker blije blijer haha hahaha hihi hihihi xd winnen win wint gewonnen ja yes whoehoe wajoo nice mooi mooier mooie mooist lach lacht lachen dank bedankt dankje goed gelukkig gelukkige gelukkiger geluk gelukt leuk leuker leukst aardig aardiger aardigst veel luxe geniaal genialer geniaalst happy lol lekker meest fijn fijne sexy sexier mooiso goed beter best beste wel fack hou succes cool gaaf top prachtige prachtig :) ;) :-) ;-) :b :d :> :-b :-d :-> =) trots super briljant amazing geweldig geweldige grapje grap grappen plezier xx :p :$ :-$ :') lt;3 <3 smile smiley ok oke okej okey okay".lower().split()
NEGATIVEWORDS = "fail slecht boos bozer arrogant arrogante haat haten kut lul gvd fuck fucking fuckin faal faalhaas faalhazen slecht slechter slechtst rot rotter rotst eindeloos eindeloze nergens verlies verliest verliezen verloren argh bah nee no vadsig vadsige crimineel criminele schurk schurken boef boeven bandiet bandieten rover rovers sukkel sukkels liegen lieg liegt jokken jok jokt liegbeest liegbeesten jokkebrok jokkebrokken achterlijk achterlijke dom domme sukkel sukkels smoesje smoesjes pijn klaag klaagt klagen huil huilt huilen verdriet verdrietig fuckte homo niet weinig wijf wijven lui chagerijnig chagerijnige chagerijniger ranzig ranziger ranzigst minder minst fout fouter foutst fouten corrupt corruptst shit paardenlul irriteer irriteert irriteren vies vieze last dwing dwingt dwingen gedwongen sla slaat slaan geslagen idioot idiote idioter gek gekker kaulo holo hoer hoeren tering kolere kanker godverdomme verkakt kk konjo bek irritant minacht minachting meh holy mislukt mislukking mislukte foei jezus erg erge nare zelfmoord verwend gezeik :( ;( :< :-( ;-( :-< =( onzin jank jankt janken huil huilt huilen schreeuw schreeuwt schreeuwen lauw lauwe raar rare nep cc fck watje nondejuu nondeju flikker debiel debiele ongelooflijke ongelooflijk mongoool mongolen stink stinkt stinken ruzie ruzies ruzien stress gestresst bedrieg bedriegt bedriegen bot schok schokkend shocking probleem problemen sterf sterft sterven scheld scheldt schelden gescheld schold scholden ziekte ziekten ziektes zooi boeit boeien pff pfff spoort sporen kloot klote klootzak klootzakken ziek scheldwoord scheldwoordennrespectloosi leugen slet sletteni tyfus zwak schokkend schokkende godver not geen".lower().split() 
NEGATIVEMODALWORDS = "geen niet not".lower().split()

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
    sentimentScore = 0
    lastWord = ""
    debugOutput = []
    for word in TweetTokenizer().tokenize(text.lower()):
        if word in POSITIVEWORDS: 
            if lastWord in NEGATIVEMODALWORDS:
                sentimentScore += 0
                debugOutput.append(NEGATIVETOKEN+word)
            else: 
                sentimentScore += 1
                debugOutput.append(POSITIVETOKEN+word)
        if word in NEGATIVEWORDS or word in NEGATIVEMODALWORDS: 
            if lastWord in NEGATIVEMODALWORDS: 
                sentimentScore += 2
                debugOutput.append(POSITIVETOKEN+word)
            else: 
                sentimentScore += -1
                debugOutput.append(NEGATIVETOKEN+word)
        if not word in POSITIVEWORDS and not word in NEGATIVEWORDS:
            debugOutput.append(word)
        lastWord = word
    if debug: print(" ".join(debugOutput))
    return(sentimentScore)

debug = len(sys.argv) > 1
for line in sys.stdin:
    jsonData = json.loads(line)
    tweetText = removeNewlines(getTweetText(jsonData))
    tweetLang = jsonData[LANG]
    tweetId = jsonData[IDSTR]
    if tweetLang == DUTCH:
        sentiment = sentimentScore(tweetText,debug)
        if sentiment > 0: print(tweetId,POSITIVE,sep=COMMA)
        elif sentiment < 0: print(tweetId,NEGATIVE,sep=COMMA)
        else: print(tweetId,NEUTRAL,sep=COMMA)
