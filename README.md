PYCON2017 api tutorial 관련 자료
=======================

## 1. 구글 API
#### 1.1. Google Calendar API
#### 1.2. Google Drive API
#### 1.3. Google URL Shortener API

## 2. 공공데이터 포털 API
#### 2.1. 공공데이터 포털 날씨 API
#### 2.2. 공공데이터 포털 미세먼지 API

## 3. 텔레그램 봇 (Telegra Bot)
#### 3.1. 텔레그램 봇 만들기

## 부록. 키값 관리하기


# 파일별 설명
#### calendar_api.py     : Google Calendar API
#### drive_api.py        : Google Drive API
#### dust_api.py         : 공공데이터 포털 미세먼지 API
#### get_key.py          : 키값 관리 파일
#### map_coordinate_api  : 지도 관련(좌표변환) API
#### shortener_api.py    : Google URL Shortener API
#### telegram_bot_api.py : python telegram bot
#### weather_api.py      : 공공데이터 포털 날씨 API


# 키값 관리하기
json 형태로 키값을 저장
파일명 : **key_data.json**

This is a normal paragraph:

{

	"map_key": "kakao map's key",
	
	"telegram_token": "telegram bot token",
	
	"shorten_key": "google shortener api key",
	
	"weather_key": "weather api key",
	
	"dust_key": "dust api key"
	
}
end code block.

![key_data.json](/key_data.png)