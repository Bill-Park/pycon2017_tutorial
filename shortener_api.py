import get_key
import requests
import json


def get_shorten_url(long_url):

    post_url = 'https://www.googleapis.com/urlshortener/v1/url'
    key = {"key": get_key.get_shorten_key()}
    metadata = {"longUrl": long_url}

    response = requests.post(post_url, params=key, data=json.dumps(metadata), headers={'Content-Type': 'application/json'})

    return response.json()['id']


if __name__ == "__main__":
    print(get_shorten_url("youtube.com"))
