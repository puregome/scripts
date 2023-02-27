#!/usr/bin/env python3
"""
   text-unique.py: remove duplicate tweets from text format files
   usage: text-uniq.py [--target_dir target_dir] file1.gz file2.gz ...
   20200803 erikt(at)xs4all.nl
"""


import argparse
import os
import pandas as pd
import warnings


def text_unique(source_file_names, target_dir):
    seen = {}
    for source_file_name in source_file_names:
        file_name = os.path.basename(source_file_name)
        print(file_name)
        target_file_name = os.path.join(target_dir, file_name)
        try:
            df_hour_data = pd.read_csv(source_file_name, index_col="id_str", dtype=object).drop_duplicates()
            to_be_deleted = []
            for i in range(0, len(df_hour_data)):
                id_str = df_hour_data.iloc[i].name
                if id_str in seen: 
                    to_be_deleted.append(id_str)
                else: 
                    seen[id_str] = True
            df_hour_data.drop(to_be_deleted, inplace=True)
            df_hour_data.to_csv(target_file_name)
        except Exception as e:
            print(f"exception for file {source_file_name}: {str(e)}")
    return


parser = argparse.ArgumentParser()
parser.add_argument("--target_dir", help = "target directory", default="../text-unique")
parser.add_argument("source_file_names", type=str, nargs="*", help = "source file names")
args = parser.parse_args()

text_unique(args.source_file_names, args.target_dir)
