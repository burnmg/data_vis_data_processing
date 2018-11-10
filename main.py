import event_data_loader
import energy_data_loader
import pandas as pd


def generate_json():
    energy_data = energy_data_loader.load_energy_data()
    event_data = event_data_loader.load_events(cal_id="columbia.edu_9br3c22tiv68m1ksr1sfngjbno@group.calendar.google.com")

    # merge event
    df = pd.merge(energy_data, event_data, how="left", on="date")

    indices_with_events = df.loc[(df['event_name'].notna()), :].index.tolist()
    df["type"] = [[] for _ in range(len(df))]
    df.loc[(df['event_name'].notna()), 'type'] = ["23", '123']
    # for i in indices_with_events:
    #     df.loc[i, "type"] = ["event1"]
    #     df.at[i, "desc"] = [df.loc[i, "event_name"]]

    print(df.loc[(df['event_name'].notna()), :])

    return df


if __name__ == '__main__':
    df = generate_json()
    # print(df)
    df.T.to_json("output.json")