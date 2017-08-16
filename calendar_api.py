import time
import datetime
import pytz
import re
from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools

try:
    import argparse
    flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
except ImportError:
    flags = None

SCOPES = 'https://www.googleapis.com/auth/calendar'
store = file.Storage('calendar_storage.json')
creds = store.get()

if not creds or creds.invalid:
    print("make new storage data file ")
    flow = client.flow_from_clientsecrets('client_secret_api.json', SCOPES)
    creds = tools.run_flow(flow, store, flags)\
        if flags else tools.run(flow, store)

DRIVE = build('calendar', 'v3', http=creds.authorize(Http()))


# get calendar list
def get_calendar_list(time_min=None):

    if time_min is None:
        time_min = datetime.datetime.now(tz=pytz.timezone('Asia/Seoul')).isoformat('T')

    eventsResult = DRIVE.events().list(
            calendarId='primary', maxResults=10, singleEvents=True,
            orderBy='startTime', timeMin=time_min).execute()

    for item in eventsResult['items']:
        print(item['summary'])
        print(item['start'])
        print(item['end'])

    return eventsResult['items']


# add event
def add_calendar_list(summary, start_time, end_time=None, spend_time=1):

    if end_time is None :
        end_time = start_time + datetime.timedelta(hours=spend_time)

    start_time = start_time.isoformat('T')
    end_time = end_time.isoformat('T')

    insertResult = DRIVE.events().insert(
        calendarId='primary', body={
            'summary': summary,
            'start': {
                'dateTime': start_time,
                'timeZone': 'Asia/Seoul'
            },
            'end': {
                'dateTime': end_time,
                'timeZone': 'Asia/Seoul'
            }
        }
    ).execute()

    print(insertResult)

    return insertResult


if __name__ == "__main__" :
    #add_calendar_list('출근', datetime.datetime(2017, 8, 17, 8), datetime.datetime(2017, 8, 17, 18))
    add_calendar_list('출근', datetime.datetime(2017, 8, 17, 8), spend_time=9)
    get_calendar_list()
