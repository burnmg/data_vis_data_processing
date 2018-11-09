from __future__ import print_function
from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools
import pandas as pd

# If modifying these scopes, delete the file token.json.
SCOPES = 'https://www.googleapis.com/auth/calendar.readonly'


def load_calendar_to_df(cal_id ="rj2537@columbia.edu"):
    """Shows basic usage of the Google Calendar API.
    Prints the start and name of the next 10 events on the user's calendar.
    """
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    store = file.Storage('token.json')
    creds = store.get()
    if not creds or creds.invalid:
        flow = client.flow_from_clientsecrets('credentials.json', SCOPES)
        creds = tools.run_flow(flow, store)
    service = build('calendar', 'v3', http=creds.authorize(Http()))

    # Call the Calendar API
    # now = datetime.datetime.utcnow().isoformat() + 'Z' # 'Z' indicates UTC time
    print('Getting the upcoming 10 events')

    events_result = service.events().list(calendarId=cal_id,
                                        maxResults=3, singleEvents=True,
                                        orderBy='startTime').execute()
    events = events_result.get('items', [])

    if not events:
        print('No upcoming events found.')
        return None
    # for event in events:
    #     print(event.keys())
    #     start = event['start'].get('dateTime', event['start'].get('date'))
    #     print(start, event['summary'])
    else:
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
            df.loc[len(df)] = [pd_time, event['summary']]
    return df

if __name__ == '__main__':
    print(load_calendar_to_df(cal_id="columbia.edu_s45i9kuao35a2rvqqt43k8sf6s@group.calendar.google.com"))