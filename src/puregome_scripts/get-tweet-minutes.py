#!/usr/bin/env python3
"""
   get-tweets-minutes.py: get minute of tweets sending from a json file
   usage: get-tweet-minutes.py < file.json | sort | uniq -c
   20200423 erikt(at)xs4all.nl
"""

from datetime import datetime, timedelta
import json
import sys

DATEFORMAT = "%a %b %d %H:%M:%S %z %Y"
SUMMERTIMEDATE = datetime.strptime("Sun Mar 29 02:00:00 +0000 2020",DATEFORMAT)
WINTERTIMEDATE = datetime.strptime("Sun Oct 25 03:00:00 +0000 2020",DATEFORMAT)

def getTweetMinute(jsonData):
    dateString = jsonData["created_at"]
    dateData = datetime.strptime(dateString,DATEFORMAT)+timedelta(hours=1)
    if dateData >= SUMMERTIMEDATE:
        if dateData >= WINTERTIMEDATE: sys.exit("cannot happen")
        dateData += timedelta(hours=1)
    return(dateData.strftime("%Y%m%d%H%M"))

def main(argv):
    for line in sys.stdin:
        try:
            jsonData = json.loads(line)
            minute = getTweetMinute(jsonData)
            print(minute)
        except: pass

if __name__ == "__main__":
    sys.exit(main(sys.argv))
