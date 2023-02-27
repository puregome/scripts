import os
import pytest
import random
import pandas as pd
from puregome_scripts import text_unique


RANDOM_FACTOR = 100000
SOURCE_DATA = [ [ {"id_str": "a", "filler": "a"}, 
                  {"id_str": "b", "filler": "b"}, 
                  {"id_str": "b", "filler": "b"}, 
                  {"id_str": "c", "filler": "c"}, 
                  {"id_str": "b", "filler": "b"},
                  {"id_str": "a", "filler": "a"} ],
                [ {"id_str": "c", "filler": "c"}, 
                  {"id_str": "d", "filler": "d"},
                  {"id_str": "a", "filler": "a"} ] ]
TARGET_DATA = [ [ {"id_str": "a", "filler": "a"}, 
                  {"id_str": "b", "filler": "b"}, 
                  {"id_str": "c", "filler": "c"} ], 
                [ {"id_str": "d", "filler": "d"} ] ]
SOURCE_FILE_NAMES = [ "file_1.csv.gz", "file_2.csv.gz" ]


def make_dir_name(base_string):
    return "_".join([ base_string, str(os.getpid()), str(int(RANDOM_FACTOR*random.random()))])


def save_source_data(source_dir_name, source_file_name, source_data):
    source_data_df = pd.DataFrame(source_data)
    source_file_name_with_dir = os.path.join(source_dir_name, source_file_name)
    source_data_df.to_csv(source_file_name_with_dir, index=False)
    return source_file_name_with_dir


def set_up_data(source_data, source_file_names):
    source_dir_name = make_dir_name("test_text_unique_source")
    target_dir_name = make_dir_name("test_text_unique_target")
    os.mkdir(source_dir_name)
    os.mkdir(target_dir_name)
    source_file_names_with_dir = []
    for i in range(0, len(source_data)):
        source_file_names_with_dir.append(save_source_data(source_dir_name, source_file_names[i], source_data[i]))
    return source_file_names_with_dir, source_dir_name, target_dir_name


def check_target_data(target_data, file_names, target_dir_name):
    for i in range(0, len(file_names)):
        df = pd.read_csv(os.path.join(target_dir_name, file_names[i]))
        assert df.equals(pd.DataFrame(target_data[i]))


def cleanup(source_file_names_with_dir, source_dir_name, target_dir_name):
    for source_file_name in source_file_names_with_dir:
        os.remove(source_file_name)
    os.rmdir(source_dir_name)
    for source_file_name in source_file_names_with_dir:
        base_file_name = os.path.basename(source_file_name)
        os.remove(os.path.join(target_dir_name, base_file_name))
    os.rmdir(target_dir_name)


def test_text_unique():
    source_file_names_with_dir, source_dir_name, target_dir_name  = set_up_data(SOURCE_DATA, SOURCE_FILE_NAMES)
    text_unique.text_unique(source_file_names_with_dir, target_dir_name)
    check_target_data(TARGET_DATA, SOURCE_FILE_NAMES, target_dir_name)
    cleanup(source_file_names_with_dir, source_dir_name, target_dir_name)
