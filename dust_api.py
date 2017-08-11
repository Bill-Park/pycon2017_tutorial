
import requests
import bill

#서울, 부산, 대구, 인천, 광주, 대전, 울산, 경기, 강원, 충북, 충남, 전북, 전남, 경북, 경남, 제주, 세종

def get_dust_api(sido):
    print(sido)
    # 시군구별 실시간 평균정보(6)
    url = "http://openapi.airkorea.or.kr/openapi/services/rest/ArpltnInforInqireSvc/getCtprvnMesureSidoLIst?ServiceKey={}".format(bill.get_dust_key())

    metadata = {
        "sidoName": "부산",
        "searchCondition": "HOUR",
        "pageNo": "1",
        "nuOfRows": "100",
        "_returnType": "json"
    }

    response = requests.get(url, params=metadata).json() # api run
    print(response)

    for dust_data in response['list'] :
        if dust_data['cityName'] == '부산진구' :
            #get pm10, pm2.5 value
            #print(dust_data['pm10Value'])
            return dust_data['pm10Value'], dust_data['pm25Value']

if __name__ == "__main__" :
    print(get_dust_api("부산"))





