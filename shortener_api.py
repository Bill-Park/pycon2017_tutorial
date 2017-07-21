def short_url(url):
    post_url = 'https://www.googleapis.com/urlshortener/v1/url?key={}'.format(api_key)
    params = json.dumps({'longUrl': url})
    response = requests.post(post_url,params,headers={'Content-Type': 'application/json'})
    return response.json()['id']
