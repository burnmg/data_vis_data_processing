from __future__ import print_function
from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools
import pandas as pd


def load_events(cal_id ="rj2537@columbia.edu"):

    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.

    # If modifying these scopes, delete the file token.json.
    SCOPES = 'https://www.googleapis.com/auth/calendar.readonly'

    store = file.Storage('token.json')
    creds = store.get()
    if not creds or creds.invalid:
        flow = client.flow_from_clientsecrets('credentials.json', SCOPES)
        creds = tools.run_flow(flow, store)
    service = build('calendar', 'v3', http=creds.authorize(Http()))

    # Call the Calendar API
    # now = datetime.datetime.utcnow().isoformat() + 'Z' # 'Z' indicates UTC time

    page_token = None
    while True:
        events_result = service.events().list(calendarId=cal_id, singleEvents=True, pageToken = page_token,
                                              orderBy='startTime').execute()
        events = events_result.get('items', [])

        if not events:
            print('No events found.')
            return None


        # for event in events:
        #     print(event.keys())
        #     start = event['start'].get('dateTime', event['start'].get('date'))
        #     print(start, event['summary'])
        else:
            print("Loaded {0} events".format(len(events)))
            df = pd.DataFrame(columns=['date', 'event_name'])
            for event in events:
                # 2019-02-04T19:10:00-05:00Deep Learning
                start_time = event['start']
                if 'date' in start_time:
                    pd_time = pd.to_datetime(start_time['date'])
                elif 'dateTime' in start_time:
                    pd_time = pd.to_datetime(start_time['dateTime'][:10])
                else:
                    raise Exception('No date or dateTime key found')

                df.loc[len(df)] = [pd_time, event['summary'] if "summary" in event else ""]
        if "nextPageToken" not in events_result:
            break

    return df
