import time
from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools
from apiclient import http
import io

# api가 전부 접근할 수는 없음 google drive로 작성됨이 있어야함

try:
    import argparse
    flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
except ImportError:
    flags = None

SCOPES = 'https://www.googleapis.com/auth/drive.file'
store = file.Storage('drive_storage.json')
creds = store.get()

if not creds or creds.invalid:
    print("make new storage data file ")
    flow = client.flow_from_clientsecrets('client_secret_api.json', SCOPES)
    creds = tools.run_flow(flow, store, flags) \
            if flags else tools.run(flow, store)

DRIVE = build('drive', 'v3', http=creds.authorize(Http()))

# find file_id by file_name
def get_file_id(file_title) :
    query = "name contains '{}'".format(file_title)

    response = DRIVE.files().list(q=query,
                                  spaces='drive',
                                  fields='files(id, name)').execute()
    for exist_folder in response.get('files', []):
        print(exist_folder)
        # Process change
        if exist_folder.get('name') == file_title :
            print('Found : %s (%s)' % (exist_folder.get('name'), exist_folder.get('id')))
            return exist_folder.get('id')

    print("fail to find")
    return None


# single file upload
def upload_file(file_title, folder_id=None):

    metadata = {'name': file_title,
                'mimeType': None,
                }

    if folder_id is not None :
        metadata['parents'] = [folder_id]

    res = DRIVE.files().create(body=metadata, media_body=file_title, fields='id, name, webViewLink').execute()
    if res:
        print('Uploaded "%s" (%s)' % (res['name'], res['webViewLink']))


def download_file(file_title, local_fd=None):

    file_id = get_file_id(file_title)

    request = DRIVE.files().get_media(fileId=file_id)
    if local_fd is None:
        local_fd = file_title
    file_to_save = open(local_fd, "wb")
    media_request = http.MediaIoBaseDownload(file_to_save, request)

    while True:
        try:
            download_progress, done = media_request.next_chunk()
        except Exception as e:
            print(e)
            file_to_save.close()
            return
        if download_progress:
            print('Download Progress: %d%%' % int(download_progress.progress() * 100))
        if done:
            print('Download Complete')
            file_to_save.close()
            return


if __name__ == "__main__" :
    #upload_file("test.jpg", "0B_CtpwiAk5hIZDJhMGlneURHTUE")
    #upload_file("test.jpg")
    download_file("test.jpg")
