import json

_map_key = None
_shortener_key = None
_telegram_token = None
_weather_key = None
_dust_key = None

with open("key_data.json", "r") as key_all :
    data = json.load(key_all)
    _map_key = data['map_key']
    _shortener_key = data['shorten_key']
    _telegram_token = data['telegram_token']
    _weather_key = data['weather_key']
    _dust_key = data['dust_key']


def get_shorten_key():
    return _shortener_key


def get_map_key():
    return _map_key


def get_telegram_token():
    return _telegram_token


def get_weather_key():
    return _weather_key


def get_dust_key():
    return _dust_key
