import requests

key = "GNm5kxMEGzPxAQ0FKgDmPDMcUDtBIFED%2BGcT2B3Ft53696UCqjhNPArrHtcyCzn8qZtz6wZKvOPu%2B15CPiPNfA%3D%3D"

sidoName = "부산"
dataTerm = "HOUR"
numOfRows = 100


# 시군구별 실시간 평균정보(6)
url = "http://openapi.airkorea.or.kr/openapi/services/rest/ArpltnInforInqireSvc/getCtprvnMesureSidoLIst?"
metadata = "sidoName={}&searchCondition={}&pageNo=1&numOfRows={}&ServiceKey={}".format(sidoName, dataTerm, numOfRows, key)
r_json = "&_returnType=json"
response = requests.get(url, metadata + r_json)
print(url + metadata + r_json)
print(response.json())
