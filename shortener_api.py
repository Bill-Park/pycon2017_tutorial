import bill
import requests
import json

post_url = 'https://www.googleapis.com/urlshortener/v1/url'
key = {"key": bill.get_shorten_key()}
metadata = {"longUrl": "https://drive.google.com/a/snue-p.com/file/d/0B_CtpwiAk5hIcC01RFN0LWp6Sk0/view?usp=drivesdk"}

response = requests.post(post_url, params=key, data=json.dumps(metadata), headers={'Content-Type': 'application/json'})
print(response.url)
print(response.json())
