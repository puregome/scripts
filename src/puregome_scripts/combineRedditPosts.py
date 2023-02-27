#!/usr/bin/env python3
# combineNunlComments.py: combine comments of nu.nl stored in csv files
# usage: combineNunlComments.py file1 file2 [file3 ...]
# note: news article comments volume can both grow and shrink over time:
#       this comments extracts all the comments on one article from 
#       different files (nontrivial because the ids are different)
# 20200915 erikt(at)xs4all.nl

import csv
import pandas as pd
import sys

ID,SUBREDDIT = "id subreddit".split()

def readFiles(inFileNameList):
    comments = {}
    for inFileName in inFileNameList:
        try:
            df = pd.read_csv(inFileName)
            for i in range(0,len(df)):
                thisId = df.iloc[i][ID]
                subreddit = df.iloc[i][SUBREDDIT]
                key = " ".join([thisId,subreddit])
                comments[key] = df.iloc[i]
        except:
            pass
    return(comments)

def showComments(comments):
    pd.DataFrame(comments).T.to_csv(sys.stdout,index=False)

comments = readFiles(sys.argv[1:])
showComments(comments)

