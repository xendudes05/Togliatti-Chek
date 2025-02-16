import sys
from io import BytesIO
from geocoder import get_coodrinates, get_spn
import requests
from PIL import Image


def main():
    toponym_to_find = "Москва, ул. Ак. Королева, 12"
    # toponym_to_find = sys.argv[1:]
    lon, lan = get_coodrinates(toponym_to_find)
    ll = f'{lon},{lan}'
    # delta = '0.005'
    dx, dy = get_spn(toponym_to_find)
    print(dx, dy)
    if dx and dy:
        spn = f'{dx},{dy}'
    apikey = "f3a0fe3a-b07e-4840-a1da-06f18b2ddf13"
    map_params = {
        "ll": ll,
        "spn": spn,
        "apikey": apikey,
        "pt": ll}
    map_api_server = "https://static-maps.yandex.ru/v1"
    response = requests.get(map_api_server, params=map_params)
    im = BytesIO(response.content)
    opened_image = Image.open(im)
    opened_image.show()


if __name__ == '__main__':
    main()
