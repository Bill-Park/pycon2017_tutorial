import time
from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools


try :
    import argparse
    flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
except ImportError:
    flags = None

SCOPES = 'https://www.googleapis.com/auth/drive.file'
store = file.Storage('storage.json')
creds = store.get()

if not creds or creds.invalid:
    print("make new storage data file ")
    flow = client.flow_from_clientsecrets('client_secret_api.json', SCOPES)
    creds = tools.run_flow(flow, store, flags) \
            if flags else tools.run(flow, store)

DRIVE = build('drive', 'v3', http=creds.authorize(Http()))

return_time = []
'''
for file_title in file_name.FILES :
    start_time = time.time()
    file_name = file_title
    metadata = {'name': file_name,
                'mimeType': None
                }

    res = DRIVE.files().create(body=metadata, media_body=file_name).execute()
    #if res:
        #print('Uploaded "%s" (%s)' % (file_name, res['mimeType']))
    running_time = time.time() - start_time
    return_time.append(round(running_time, 2))
    print("--- %s seconds ---" % (running_time))
'''


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
