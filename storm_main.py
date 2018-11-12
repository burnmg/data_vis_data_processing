from load_daily_data import load
import pandas as pd

storm = load("/Users/rl/PycharmProjects/data_vis_data_processing/data_set/storm/")
energy_load = storm.groupby(['Time Stamp'], as_index=False)["Integrated Load"].sum().sort_values(by=["Time Stamp"])
energy_load.columns.values[0] = "Time_Stamp"
energy_load.columns.values[1] = "Integrated_Load"
energy_load.to_json('output/storm.json', orient="records")

storm = load("/Users/rl/PycharmProjects/data_vis_data_processing/data_set/storm_2018/")
energy_load = storm.groupby(['Time Stamp'], as_index=False)["Integrated Load"].sum().sort_values(by=["Time Stamp"])
energy_load.columns.values[0] = "Time_Stamp"
energy_load.columns.values[1] = "Integrated_Load"
energy_load.to_json('output/storm2018.json', orient="records")