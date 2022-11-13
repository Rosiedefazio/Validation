import pandas as pd
import gc 
import logging 
import os
import subprocess
import yaml 
import datetime
import re

def read_config_file(filepath):
    with open(filepath, 'r') as a:
        try: 
            return yaml.safe_load(a)
        except yaml.YAMLError as exc:
            logging.error[exc]

def col_header_val(df.table_config):
    df.columns = df.columns.str.lower()
    df.columns = df.columns.str.replace("'[^\',", "_", regex= True )
    df.columns = list(map(lambda x: x.strip('_', list(df.columns))))
    expectedcol = list(map(lambda x: x.lower(), table_config["columns"]))
    expectedcol.sort 
    df.comlumns = list(map(lambda x: x.lower(), list(df.columns)))
    df = df.reindex(sorted(df.columns, axis=1))
    if len(df.columns) == len(expectedcol)  and list(expectedcol) == list(df.columns):
        print("passed")
        return 1 
    else: 
        print("FAILED")
        return 0 
