import pandas as pd


def load_energy_data(dir="data/ny_load_1711-1810.json"):

    energy_data = pd.read_json(dir)

    date = pd.to_datetime(energy_data.loc[:, ['year', 'month', 'day']])
    energy_data['date'] = date

    return energy_data.sort_values(by=['date'])