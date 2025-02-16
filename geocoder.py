import requests

APIKEY = "8013b162-6b42-4997-9691-77b7074026e0"


def geocode(adress):
    geocoder_api_server = "http://geocode-maps.yandex.ru/1.x/"
    geocoder_params = {
        "apikey": "8013b162-6b42-4997-9691-77b7074026e0",
        "geocode": adress,
        "format": "json"}

    response = requests.get(geocoder_api_server, params=geocoder_params)
    if response:
        json_response = response.json()
        toponym = json_response["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]
        return toponym
    else:
        raise RuntimeError('Ошибка запроса')
        return None


def get_coodrinates(toponym_to_find):
    toponym = geocode(toponym_to_find)
    if toponym:
        toponym_coodrinates = toponym["Point"]["pos"]
        lon, lan = toponym_coodrinates.split(" ")
        return float(lon), float(lan)
    return None

def get_spn(toponym_to_find):
    toponym = geocode(toponym_to_find)
    if not toponym:
        return (None, None)
    toponym_coodrinates = toponym["Point"]["pos"]
    lon, lan = toponym_coodrinates.split(" ")
    border = toponym["boundedBy"]["Envelope"]
    left, bottom = border["lowerCorner"].split(' ')
    right, top = border["upperCorner"].split(' ')
    dx = abs(float(left) - float(right)) / 2
    dy = abs(float(top) - float(bottom)) / 2
    return dx, dy


