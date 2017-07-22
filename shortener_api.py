import json
import requests

api_key = "AIzaSyApn7CApnBFrAaepfELDV_foyPjTyz6PMU"

url = "https://www.youtube.com/"

post_url = 'https://www.googleapis.com/urlshortener/v1/url?key={}'.format(api_key)
metadata = {"longUrl": "https://www.youtube.com/"}

response = requests.post(post_url, str(metadata), headers={'Content-Type': 'application/json'})
print(response.json())
