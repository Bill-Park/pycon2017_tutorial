import requests
import get_key

#서울, 부산, 대구, 인천, 광주, 대전, 울산, 경기, 강원, 충북, 충남, 전북, 전남, 경북, 경남, 제주, 세종

sido_list = ["서울", "부산", "대구",
             "인천", "광주", "대전",
             "울산", "경기", "강원",
             "충북", "츙남", "전북",
             "전남", "경북", "경남",
             "제주", "세종"]


def get_dust_api(sido, city, period="HOUR", page_num=1, num_of_row=100):

    # check sido in sido_list
    if sido not in sido_list:
        return None

    url = "http://openapi.airkorea.or.kr/openapi/services/rest/ArpltnInforInqireSvc/getCtprvnMesureSidoLIst?ServiceKey={}"\
        .format(get_key.get_dust_key())

    metadata = {
        "sidoName": sido,
        "searchCondition": period,
        "pageNo": str(page_num),
        "nuOfRows": str(num_of_row),
        "_returnType": "json"
    }

    response = requests.get(url, params=metadata).json()  # api run

    for dust_data in response['list']:
        if dust_data['cityName'] == city:  # change to get argument
            return dust_data['pm10Value'], dust_data['pm25Value']

if __name__ == "__main__" :
    print(get_dust_api("서울", "강남구"))
    print(get_dust_api("부산", "부산진구"))





