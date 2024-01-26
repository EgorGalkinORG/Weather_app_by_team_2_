import requests
import customtkinter, os
import modules.api as m_api
from PIL import Image


img = Image.open(os.path.abspath(__file__ + f"/../../images/night.png"))
def iconka(city: str):
    weather = m_api.get_data_weth()['list'][0]['weather'][0]['icon']

    # print(weather)
    if "01n" in weather:
        if "n" in weather:
            img = Image.open(os.path.abspath(__file__ + "/../../images/night.png"))
        elif "d" in weather:
            img = Image.open(os.path.abspath(__file__ + "/../../images/sun.png"))
    elif "02" in weather:
        if "n" in weather:
            img = Image.open(os.path.abspath(__file__ + "/../../images/night.png"))
        elif "d" in weather:
            img = Image.open(os.path.abspath(__file__ + "/../../images/sunny_1.png"))
    elif "03" in weather:
        if "n" in weather:
            img = Image.open(os.path.abspath(__file__ + "/../../images/night.png"))
        elif "d" in weather:
            img = Image.open(os.path.abspath(__file__ + "/../../images/lata.png"))
    elif "04" in weather:
        if "n" in weather:
            img = Image.open(os.path.abspath(__file__ + "/../../images/rain.png"))
        elif "d" in weather:
            img = Image.open(os.path.abspath(__file__ + "/../../images/sunny_1.png"))
    elif "09" in weather:
        if "n" in weather:
            img = Image.open(os.path.abspath(__file__ + "/../../images/drizzle_1.png"))
        elif "d" in weather:
            img = Image.open(os.path.abspath(__file__ + "/../../images/drizzle_1.png"))
    elif "10" in weather:
        if "n" in weather:
            img = Image.open(os.path.abspath(__file__ + "/../../images/rain.png"))
        elif "d" in weather:
            img = Image.open(os.path.abspath(__file__ + "/../../images/rainy.png"))
    elif "11" in weather:
        if "n" in weather:
            img = Image.open(os.path.abspath(__file__ + "/../../images/storm.png"))
        elif "d" in weather:
            img = Image.open(os.path.abspath(__file__ + "/../../images/storm.png"))
    elif "13" in weather:
        if "n" in weather:
            img = Image.open(os.path.abspath(__file__ + "/../../images/snowy_3.png"))
        elif "d" in weather:
            img = Image.open(os.path.abspath(__file__ + "/../../images/snowy_2.png"))
    elif "50" in weather:
        if "n" in weather:
            img = Image.open(os.path.abspath(__file__ + "/../../images/drizzle_1.png"))
        elif "d" in weather:
            img = Image.open(os.path.abspath(__file__ + "/../../images/drizzle_1.png"))
    else:
        img = Image.open(os.path.abspath(__file__ + "/../../images/snowy_3.png"))
    return img

print(img)



# img1 = customtkinter.CTkImage(dark_image= img1_1, size= [171, 159])

# icon = customtkinter.Ctk