#!/usr/bin/env python3
# get-text.py: get text column from csv file
# usage: get-text.py < file
# 20201114 erikt(at)xs4all.nl

import csv
import sys

TEXT = "text"

csvreader = csv.DictReader(sys.stdin)
for row in csvreader: 
    print(row[TEXT])
