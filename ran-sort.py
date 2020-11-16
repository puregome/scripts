#!/usr/bin/env python3
# ran-sort.py: randomly sort line of text in stdin
# usage: ran-sort.py < file
# 20201113 erikt(at)xs4all.nl

import random
import sys

def read_lines():
    lines = []
    for line in sys.stdin:
        lines.append(line)
    return(lines)

def print_lines(lines):
    while lines:
        r = random.randint(0,len(lines)-1)
        print(lines[r],end="")
        lines[r] = lines[-1]
        lines.pop(-1)

lines = read_lines()
print_lines(lines)
sys.exit(0)
