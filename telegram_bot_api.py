import telegram
import dust_api
import weather_api
import bill
import requests
import map_coordinate_api
from telegram.ext import Updater, CommandHandler
from telegram.ext import MessageHandler, Filters

my_token = bill.get_telegram_token()


bot = telegram.Bot(token = my_token)   #bot을 선언합니다.

updates = bot.getUpdates()  #업데이트 내역을 받아옵니다.

pm10, pm25 = dust_api.get_dust_api("부산") #get sidoname need

send2telegram_dust = "pm 10 Value : {}\npm 25 Value : {}".format(pm10, pm25)

'''
weather_all = weather_api.get_weather_api()
weather_REH = weather_all['REH']
weather_T3H = weather_all['T3H']
weather_SKY = weather_all['SKY']

sky_code = [
    '맑음',
    '구름조금',
    '구름많음',
    '흐림',
]

send2telegram_sky = "내일 날씨 : {}\n"\
                    "현재 기온 : {}\n"\
                    "현재 습도 : {}".format(weather_SKY, weather_T3H, weather_REH)

bot.sendMessage(chat_id = chat_id, text=send2telegram_sky)
'''

def bot_start(bot, update) :
    send2start = "날씨 챗봇입니다.\n"\
                 "위치를 설정하시려면 [/location]을 클릭해 주세요"
    update.message.reply_text(send2start)

def set_location(bot, update) :
    send2location = "위치를 설정합니다.\n" \
                 "위치 정보를 보내주시거나 시-동을 입력해 주세요."
    update.message.reply_text(send2location)

def get_location(bot, update) :
    print(update.message.location.latitude)
    print(update.message.location.longitude)
    target_latitude = update.message.location.latitude
    target_longitude = update.message.location.longitude
    post_url = 'https://dapi.kakao.com/v2/local/geo/coord2regioncode.json?x={}&y={}'.format(target_longitude, target_latitude)
    #metadata = {"longUrl": "https://www.youtube.com/"}

    response = requests.post(post_url, headers={'Authorization': "KakaoAK " + bill.get_map_key()}).json()
    print(response['documents'])
    for get_map_coordinate in response['documents'] :
        if get_map_coordinate['region_type'] == 'H' :
            #print(get_map_coordinate['region_1depth_name'])
            weather_coordinate = map_coordinate_api.get_weather_map_coordinate(get_map_coordinate['region_1depth_name'], get_map_coordinate['region_2depth_name'], get_map_coordinate['region_3depth_name'])
            weather_data = weather_api.get_weather_api(weather_coordinate['x'], weather_coordinate['y'])
            print(weather_data)
    '''
    GET /v2/local/geo/coord2regioncode.{format} HTTP/1.1
    Host: dapi.kakao.com
    Authorization: KakaoAK {app_key}
    
    curl -v -X GET "https://dapi.kakao.com/v2/local/geo/coord2regioncode.json?x=127.1086228&y=37.4012191" \
    -H "Authorization: KakaoAK kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk"
    '''

def notie_weather(bot, update) :
    weather_all = weather_api.get_weather_api()
    weather_REH = weather_all['REH']
    weather_T3H = weather_all['T3H']
    weather_SKY = weather_all['SKY']

    sky_code = [
        '',
        '맑음',
        '구름조금',
        '구름많음',
        '흐림',
    ]

    send2telegram_weather = "내일 날씨 : {}\n" \
                            "현재 기온 : {}\n" \
                            "현재 습도 : {}".format(sky_code[weather_SKY], weather_T3H, weather_REH)

    update.message.reply_text(send2telegram_weather)


updater = Updater(my_token)

start_handler = CommandHandler('start', bot_start)
updater.dispatcher.add_handler(start_handler)

request_location_handler = CommandHandler('location', set_location)
updater.dispatcher.add_handler(request_location_handler)

get_location_handler = MessageHandler(Filters.location, get_location)
updater.dispatcher.add_handler(get_location_handler)

help_handler = CommandHandler('help', help)
updater.dispatcher.add_handler(help_handler)

weather_handler = CommandHandler('weather', notie_weather)
updater.dispatcher.add_handler(weather_handler)

updater.start_polling(timeout=3, clean=True)
print("bot start")
updater.idle()

'''
db 추가해서 개인 내역 저장하기(ORM)
챗봇 내용
start - 소개, 기능설명
설정- 위치, 알림기능 여부(최저, 최고온도, 하루 강수확률 - 낮, 점심, 오후로 나눠서)  
weather(dust 포함)
    저장된 위치 or 원하는 위치(파싱)
    시간대(최근 24시간) 요청
        내역 출력(미세먼지 포함) - 12시 이후일 경우 최고온도만, 다음날일 경우 최저/최고온도
'''