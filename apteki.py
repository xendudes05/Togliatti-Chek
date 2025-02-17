import sys
import requests
from io import BytesIO
from PIL import Image
from geocoder2 import get_coodrinates, get_orzanization, get_distance

# toponym_to_find = ' '.join(sys.argv[1:])
toponym_to_find = "Тольятти Приморский бульвар 40"
lon, lan = get_coodrinates(toponym_to_find)
spn = "0.005,0.005"
address_ll = f"{lon},{lan}"
organization = get_orzanization(address_ll, spn, "аптека")

# Название организации.
org_name = organization["properties"]["CompanyMetaData"]["name"]
# Адрес организации.
org_address = organization["properties"]["CompanyMetaData"]["address"]

# Получаем координаты ответа.
point = organization["geometry"]["coordinates"]
org_point = f"{point[0]},{point[1]}"
delta = "0.005"
# apikey = "f3a0fe3a-b07e-4840-a1da-06f18b2ddf13"
apikey = "f5e8d0d9-e8bf-40fb-8f03-b0f301319c2a"

# Собираем параметры для запроса к StaticMapsAPI:
map_params = {
    # позиционируем карту центром на наш исходный адрес
    "ll": address_ll,
    "spn": ",".join([delta, delta]),
    "apikey": apikey,
    # добавим точку, чтобы указать найденную аптеку
    "pt": f"{org_point},pm2dgl~{address_ll},pm2rdl"}

map_api_server = "https://static-maps.yandex.ru/v1"
# ... и выполняем запрос
response = requests.get(map_api_server, params=map_params)
if response:
    im = BytesIO(response.content)
    opened_image = Image.open(im)
    opened_image.show()
else:
    raise RuntimeError(response.status_code)
org_time = organization["properties"]["CompanyMetaData"]["Hours"]["text"]
snippet = (f"Название:\t{org_name}\nАдрес:\t{org_address}\nВремя работы:\t{org_time}")
print(snippet)

a = (lon, lan)
b = (point[0], point[1])
distance = get_distance(a, b)
print(f"Расстояние: {distance}")
