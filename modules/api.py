import requests, time
api_key =  "96fdd776c47b76136d40d34b601d15a3"
api_key1 =  "96fdd776c47b76136d40d34b601d15a3"

def temper(kelvin: float):
    return str(int(kelvin - 273.15))
def get_data_weth(city = "Днепр"):
    url_api = f"https://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}&lang=English"
    response = requests.get(url_api)
    if response.status_code == 200:
        return response.json()
    else:
        print(response)


def main_waether(sf: str):

    data = get_data_weth(city= sf)['list'][0]['weather'][0]['main']

    if data == "Clouds":
        text_weath = "Хмарно"
    elif data == "Snow":
        text_weath = "Сніжно"
    elif data == "Rain":
        text_weath = "Дощь"
    elif data == "Mist":
        text_weath = "Туман"
    elif data == "Clear":
        text_weath = "Ясно"
    return text_weath

wth1_t = main_waether("Київ")
wth2_t = main_waether("Рим")
wth3_t = main_waether("Лондон")
wth4_t = main_waether("Варшава")
wth5_t = main_waether("Прага")
wth6_t = main_waether("Дніпро")

#   data['list'][0]['main']['temp']
#   data['list'][0]['weather'][0]['description']
ilf1_t = temper(get_data_weth(city= "Київ")['list'][0]['main']['temp']) + "°"
ilf2_t = temper(get_data_weth(city= "Рим")['list'][0]['main']['temp']) + "°"
ilf3_t = temper(get_data_weth(city= "Лондон")['list'][0]['main']['temp']) + "°"
ilf4_t = temper(get_data_weth(city= "Варшава")['list'][0]['main']['temp']) + "°"
ilf5_t = temper(get_data_weth(city= "Прага")['list'][0]['main']['temp']) + "°"
ilf6_t = temper(get_data_weth(city= "Дніпро")['list'][0]['main']['temp']) + "°"
print(get_data_weth()['list'][0]['main']['temp_max'])
# print(time.localtime())
today = time.localtime()
if today.tm_wday == 0:
    text_day = "Понеділок"
elif today.tm_wday == 1:
    text_day = "Вівторок"
elif today.tm_wday == 2:
    text_day = "Середа"
elif today.tm_wday == 3:
    text_day = "Четвер"
elif today.tm_wday == 4:
    text_day = "П'ятниця"
elif today.tm_wday == 5:
    text_day = "Субота"
elif today.tm_wday == 6:
    text_day = "Неділя"