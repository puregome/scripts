#!/usr/bin/env python3
"""
    ran-select-text.py: randomly select lines from file
    usage: python3 [-h] ran-select-text.py < file.txt
    note: option -h: always output initial header line
    20200507 erikt(at)xs4all.nl
"""

import getopt
import random
import sys


try:
    opts, args = getopt.getopt(sys.argv[1:], "h")
except:
    sys.exit(f"usage: {sys.argv[0]} [-h] [sample_size]")

sample_size = 0.01
if len(args) > 0: 
    sample_size = float(args.pop(0))
line_nbr = 0
for line in sys.stdin:
    line_nbr += 1
    if line_nbr == 1 and "-h" in [list(opt)[0] for opt in opts]:
        print(line, end="")
    elif random.random() < sample_size:
        print(line, end="")
