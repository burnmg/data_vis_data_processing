from load_daily_data import load

z911_df = load("/Users/rl/PycharmProjects/data_vis_data_processing/data_set/911/")

z911_df_nyc = z911_df.loc[z911_df["Name"] == "N.Y.C.", :]
z911_df_nyc.to_json('output/911.json')