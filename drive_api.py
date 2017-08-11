import time
from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools
from apiclient import http
import io

# api가 전부 접근할 수는 없음 google drive로 작성됨이 있어야함

try :
    import argparse
    flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
except ImportError:
    flags = None

SCOPES = 'https://www.googleapis.com/auth/drive.file'
store = file.Storage('drive_api.json')
creds = store.get()

if not creds or creds.invalid:
    print("make new storage data file ")
    flow = client.flow_from_clientsecrets('client_secret_api.json', SCOPES)
    creds = tools.run_flow(flow, store, flags) \
            if flags else tools.run(flow, store)

DRIVE = build('drive', 'v3', http=creds.authorize(Http()))


'''
# mutliple file upload
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
# single file upload
metadata = {'name': "bill.txt",
            'mimeType': None
            }

#media_body is necessary
res = DRIVE.files().create(body=metadata, media_body="bill.txt").execute()
# if res:
# print('Uploaded "%s" (%s)' % (file_name, res['mimeType']))
'''



# ...

def print_file_metadata(service, file_id):
  """Print a file's metadata.

  Args:
    service: Drive API service instance.
    file_id: ID of the file to print metadata for.
  """
  try :
    file = service.files().get(fileId=file_id).execute()
    print('Title: %s' % file['name'])
    print('MIME type: %s' % file['mimeType'])
  except :
      print("error")


  #except(errors.HttpError, error):
  #  print('An error occurred: %s' % error)



def print_file_content(service, file_id):
  """Print a file's content.

  Args:
    service: Drive API service instance.
    file_id: ID of the file.

  Returns:
    File's content if successful, None otherwise.
  """
  try:
    print(service.files().get_media(fileId=file_id).execute())
  except:
    print("error")
  #except errors.HttpError, error:
  #  print('An error occurred: %s' % error)


def download_file(service, file_id, local_fd):
  """Download a Drive file's content to the local filesystem.

  Args:
    service: Drive API Service instance.
    file_id: ID of the Drive file that will downloaded.
    local_fd: io.Base or file object, the stream that the Drive file's
        contents will be written to.
  """
  request = service.files().get_media(fileId=file_id)
  media_request = http.MediaIoBaseDownload(local_fd, request)

  while True:
    try:
      download_progress, done = media_request.next_chunk()
    #except errors.HttpError, error:
    #  print 'An error occurred: %s' % error
    except :
      return
    if download_progress:
      print('Download Progress: %d%%' % int(download_progress.progress() * 100))
    if done:
      print('Download Complete')
      return


def get_file_id(file_title) :
    query = "name contains '{}'".format(file_title)

    response = DRIVE.files().list(q=query,
                                  spaces='drive',
                                  fields='files(id, name)').execute()
    for exist_folder in response.get('files', []):
        print(exist_folder)
        # Process change
        if exist_folder.get('name') == file_title :
            print('Found folder: %s (%s)' % (exist_folder.get('name'), exist_folder.get('id')))
            return exist_folder.get('id')

    print("nothing to find")


#print(get_file_id("bill.txt"))

#print_file_metadata(DRIVE, get_file_id("bill.txt"))

#print_file_content(DRIVE, get_file_id("bill.txt"))


f = open("bill.txt", "wb")

download_file(DRIVE, get_file_id("bill.txt"), f)

f.close()

#print(DRIVE.files().get(fileId=get_file_id("bill.txt")).execute())
