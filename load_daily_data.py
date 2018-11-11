import pandas as pd
import os

def load(dir):
    file_names = os.listdir(dir)
    csv_files_paths = []
    for file_name in file_names:
        csv_files_paths.append(dir+file_name)

    dfs = []
    for csv_path in csv_files_paths:
        dfs.append(pd.read_csv(csv_path))
    return pd.concat(dfs).reset_index()



