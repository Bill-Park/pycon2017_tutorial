import requests
import get_key

# custom api, bill's aws lambda
def get_weather_map_coordinate(f1="", f2="", f3=""):
    base_url = "https://57b1zt4gf3.execute-api.ap-northeast-2.amazonaws.com/dev"
    print(f1)
    print(f2)
    print(f3)

    arguments = {
        "f1": f1,
        "f2": f2,
        "f3": f3
    }

    response = requests.get(base_url, params=arguments).json()

    return response


# kakao map api
def get_map_address(longitude, latitude):
    base_url = 'https://dapi.kakao.com/v2/local/geo/coord2regioncode.json'

    arguments = {
        "x": longitude,
        "y": latitude
    }

    response = requests.post(base_url, params=arguments, headers={'Authorization': "KakaoAK " + get_key.get_map_key()}).json()

    for map_address_list in response['documents']:
        if map_address_list['region_type'] == 'H':
            return map_address_list['region_1depth_name'], map_address_list['region_2depth_name'], map_address_list['region_3depth_name']

    return None


if __name__ == "__main__":
    #print(get_weather_map_coordinate("서울특별시", "강남구"))
    #print(get_map_address(129.03, 35.15))   # 부산광역시 부산진구 가야2동

    address_1, address_2, address_3 = get_map_address(129.03, 35.15)
    print(get_weather_map_coordinate(address_1, address_2, address_3))