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


def load_nyc(old_path, i2018_path, output1, output2):
    z911_df = load(old_path)
    z911_df_nyc = z911_df.loc[z911_df["Name"] == "N.Y.C.", :]
    z911_df_nyc.columns.values[1] = "Time_Stamp"
    z911_df_nyc.columns.values[5] = "Integrated_Load"
    z911_df_nyc.to_json('output/' + output2, orient="records")

    z911_df = load(i2018_path)
    z911_df_nyc = z911_df.loc[z911_df["Name"] == "N.Y.C.", :]
    z911_df_nyc.columns.values[1] = "Time_Stamp"
    z911_df_nyc.columns.values[5] = "Integrated_Load"
    z911_df_nyc.to_json('output/' + output1, orient="records")