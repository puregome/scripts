#!/usr/bin/env python3
# remove-duplicates.py: remove tweets with identical text from stdin
# usage: remove-duplicates.py < file
# 20201113 erikt(at)xs4all.nl

import csv
import re
import sys

def cleanup_text(text):
    text = text.lower()
    text = re.sub("https?://\S*","",text)
    text = re.sub("\\\\n"," ",text)
    text = re.sub("\s+"," ",text)
    text = re.sub("^rt\s+\S+:\s*","",text)
    text = text.strip()
    return(text)

def process_file_arguments(file_names):
    seen_texts = {}
    for file_name in file_names:
        file_handle = open(file_name,"r")
        csvreader = csv.reader(file_handle)
        for row in csvreader:
            text = cleanup_text(row[4])
            seen_texts[text] = True
        file_handle.close()
    return(seen_texts)

seen_texts = process_file_arguments(sys.argv[1:])
csvreader = csv.reader(sys.stdin) 
csvwriter = csv.writer(sys.stdout) 
for row in csvreader:
    text = cleanup_text(row[4])
    if text not in seen_texts:
        csvwriter.writerow(row)
        seen_texts[text] = True
