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

ID,NAME,DATE,TEXT,PARENT = "id name date text parent".split()

def readFiles(inFileNameList):
    ids = {}
    commentsByKey = {}
    for inFileName in inFileNameList:
        try:
            df = pd.read_csv(inFileName)
            for i in range(0,len(df)):
                thisId,name,date,text,parent = df.iloc[i]
                key = " ".join([name,date,text])
                if not key in commentsByKey: 
                    commentsByKey[key] = {ID:thisId,NAME:name,DATE:date,TEXT:text,PARENT:parent}
                else:
                    if thisId in ids and ids[thisId] != commentsByKey[key][ID]:
                        print(f"cannot happen! ids {thisId}",file=sys.stderr)
                    if parent in ids and ids[parent] != commentsByKey[key][PARENT]:
                        print(f"cannot happen! ids {parent}",file=sys.stderr)
                    ids[thisId] = commentsByKey[key][ID]
                    ids[parent] = commentsByKey[key][PARENT]
        except:
            print(f"read error for file {inFileName} (empty file?)",file=sys.stderr)
    return(commentsByKey,ids)

def updateCommentIds(commentsByKey,ids):
    commentsById = {}
    for key in commentsByKey:
        if commentsByKey[key][ID] in ids: 
            commentsByKey[key][ID] = ids[commentsByKey[key][ID]]
        if commentsByKey[key][PARENT] in ids: 
            commentsByKey[key][PARENT] = ids[commentsByKey[key][PARENT]]
        commentsById[commentsByKey[key][ID]] = commentsByKey[key]
    return(commentsById)

def showComments(commentsById):
    if len(commentsById) > 0:
        pd.DataFrame(commentsById).T.to_csv(sys.stdout,index=False)

commentsByKey,ids = readFiles(sys.argv[1:])
commentsById = updateCommentIds(commentsByKey,ids)
showComments(commentsById)

