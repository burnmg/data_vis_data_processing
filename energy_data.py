import pandas as pd
energy_data = pd.read_json("data/ny_load_1711-1810.json")

date = pd.to_datetime(energy_data.loc[:, ['year', 'month', 'day']])
energy_data['date'] = date

# get max and min time
print(energy_data['date'])
print(pd.DataFrame.max(energy_data['date']))
print(pd.DataFrame.min(energy_data['date']))
