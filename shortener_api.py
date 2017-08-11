import bill
import requests
import json

post_url = 'https://www.googleapis.com/urlshortener/v1/url'
key = {"key": bill.get_shorten_key()}
metadata = {"longUrl": "https://www.youtube.com/"}

response = requests.post(post_url, params=key, data=json.dumps(metadata), headers={'Content-Type': 'application/json'})
print(response.url)
print(response.json())
