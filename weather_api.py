import datetime
import pytz
import requests
import get_key

standard_time = [2, 5, 8, 11, 14, 17, 20, 23]  # api response time
sky_code = ["맑음", "구름조금", "구름많음", "흐림"]  # sky code change to understandable

def get_api_data() :
    time_now = datetime.datetime.now(tz=pytz.timezone('Asia/Seoul')).strftime('%H')
    check_time = int(time_now) - 1
    day_calibrate = 0
    # hour to api time
    while check_time not in standard_time:
        check_time -= 1
        if check_time < 2:
            day_calibrate = 1  # yesterday
            check_time = 23

    date_now = datetime.datetime.now(tz=pytz.timezone('Asia/Seoul')).strftime('%Y%m%d')  # get date
    check_date = int(date_now) - day_calibrate

    return str(check_date), str(check_time) + '00'


def get_weather_api(nx, ny):

    api_date, api_time = get_api_data()
    base_url = "http://newsky2.kma.go.kr/service/SecndSrtpdFrcstInfoService2/ForecastSpaceData?serviceKey={}"\
        .format(get_key.get_weather_key())

    metadata = {
        "base_date": api_date,
        "base_time": api_time,
        "nx": nx,
        "ny": ny,
        "numOfRows": "100",
        "pageNo": "1",
        "_type": "json"
    }

    response = requests.get(base_url, params=metadata).json()['response']['body']['items']['item']
    target_date = response[0]['fcstDate']  # get date and time
    target_time = response[0]['fcstTime']
    weathercast_return = {
        "date": target_date,
        "time": target_time
    }

    # SKY = 하늘 상태
    # T3H = 기온
    # REH = 습도
    # POP = 강수확률
    weather_i_want = ['SKY', 'T3H', 'REH', 'POP']
    for weathercast in response:
        if weathercast['fcstDate'] == target_date and weathercast['fcstTime'] == target_time:
            if weathercast['category'] in weather_i_want:
                if weathercast['category'] == 'SKY':  # sky value change to understandable
                    weathercast_return[weathercast['category']] = sky_code[weathercast['fcstValue'] - 1]
                    continue
                weathercast_return[weathercast['category']] = weathercast['fcstValue']


    return weathercast_return

if __name__ == "__main__" :
    print(get_weather_api(97, 76))