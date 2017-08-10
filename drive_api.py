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
store = file.Storage('drive_permission.json')
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
'''
# upload file
file_name = "123.jpg"
metadata = {'name': file_name,
            'mimeType': None
            }

res = DRIVE.files().create(body=metadata, media_body=file_name).execute()
if res:
    print('Uploaded "%s" (%s)' % (file_name, res['mimeType']))
'''


def get_file_id(file_title) :
    query = "name = '{}'".format(file_title)
    response = DRIVE.files().list(q=query,
                                  spaces='drive',
                                  fields='files(id, name)').execute()
    print(response)

    for exist_folder in response.get('files', []):
        # Process change
        print(exist_folder)
        if exist_folder.get('name') == file_title :
            print('Found file: %s (%s)' % (exist_folder.get('name'), exist_folder.get('id')))
            return exist_folder.get('id')

#print(get_file_id("123.jpg"))
res = DRIVE.files().get(fileId=get_file_id("123.jpg"))
print(res.execute())
'''
file_id = '0BwwA4oUTeiV1UVNwOHItT0xfa2M'
request = DRIVE.files().get_media(fileId=file_id)
fh = io.BytesIO()
downloader = MediaIoBaseDownload(fh, request)
done = False
while done is False:
    status, done = downloader.next_chunk()
    print "Download %d%%." % int(status.progress() * 100)


def get_file_id(file_title) :
    query = "name contains '{}'".format(file_title)
    response = DRIVE.files().list(q=query,
                                  spaces='drive',
                                  fields='files(id, name)').execute()

    for exist_folder in response.get('files', []):
        # Process change
        if exist_folder.get('name') == file_title :
            print('Found folder: %s (%s)' % (exist_folder.get('name'), exist_folder.get('id')))
            return exist_folder.get('id')


def delete_file(file_id, isteam=False):
    deleted_file = DRIVE.files().delete(fileId=file_id,
                                        supportsTeamDrives=isteam).execute()
    print(deleted_file)


'''