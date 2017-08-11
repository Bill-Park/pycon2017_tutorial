import requests

#https://57b1zt4gf3.execute-api.ap-northeast-2.amazonaws.com/dev?f1=부산광역시&f2=영도구&f3=동삼제1동"


def get_weather_map_coordinate(f1="", f2="", f3=""):
    base_url = "https://57b1zt4gf3.execute-api.ap-northeast-2.amazonaws.com/dev?"

    arguments = {
        "f1": f1,
        "f2": f2,
        "f3": f3
    }

    response = requests.get(base_url, params=arguments).json()
    #print(response['x'])
    #print(response['y'])

    return response
