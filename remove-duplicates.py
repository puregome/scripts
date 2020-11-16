#!/usr/bin/env python3
# remove-duplicates.py: remove tweets with identical text from stdin
# usage: remove-duplicates.py < file
# 20201113 erikt(at)xs4all.nl

import csv
import re
import sys

seen_text = {}
csvreader = csv.reader(sys.stdin) 
csvwriter = csv.writer(sys.stdout) 
for row in csvreader:
    text = row[4]
    text = row[4].lower()
    text = re.sub("https?://\S*","",text)
    text = re.sub("\\\\n"," ",text)
    text = re.sub("\s+"," ",text)
    text = re.sub("^rt\s+\S+:\s*","",text)
    if text.strip() not in seen_text:
        csvwriter.writerow(row)
        seen_text[text.strip()] = True
