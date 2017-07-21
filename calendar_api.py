import time
from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools

try :
    import argparse
    flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
except ImportError:
    flags = None

SCOPES = 'https://www.googleapis.com/auth/calendar'
store = file.Storage('storage.json')
creds = store.get()

if not creds or creds.invalid:
    print("make new storage data file ")
    flow = client.flow_from_clientsecrets('client_secret_api.json', SCOPES)
    creds = tools.run_flow(flow, store, flags) \
            if flags else tools.run(flow, store)

DRIVE = build('calendar', 'v3', http=creds.authorize(Http()))
'''
calendarlist = DRIVE.calendarList().list(
    calendarId='primary', maxResults=10, singleEvents=True,
        orderBy='startTime'
)
print(calendarlist)
'''

eventsResult = DRIVE.events().list(
        calendarId='primary', maxResults=10, singleEvents=True,
        orderBy='startTime').execute()
#print(eventsResult['items'])
for item in eventsResult['items'] :
    print(item['summary'])
    print(item['start'])

'''
{'accessRole': 'owner', 'etag': '"p33kdpvugvj2t60g"', 'timeZone': 'Asia/Seoul', 'summary': 'tkddn0916@student.snue.ac.kr', 'defaultReminders': [{'minutes': 10, 'method': 'popup'}], 'updated': '2017-04-28T01:14:05.073Z', 'kind': 'calendar#events', 'items': []}


start_time = time.time()
file_name = file_name.FILES[upload_num]
metadata = {'name': file_name,
            'mimeType': None
            }

res = DRIVE.files().create(body=metadata, media_body=file_name).execute()
# if res:
# print('Uploaded "%s" (%s)' % (file_name, res['mimeType']))
running_time = time.time() - start_time
return_time.append(round(running_time, 2))
print("--- %s seconds ---" % (running_time))

'''

