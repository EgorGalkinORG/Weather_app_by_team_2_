import os , customtkinter, sqlite3, time
from PIL import Image
import modules.font as m_font
import modules.api as m_api
import modules.icons as m_ico
import modules.time as m_time
def main_waether(sf: str):

    data = m_api.get_data_weth(sf)['list'][0]['weather'][0]['main']

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
def get_value(cursor: object, name_table='Signed', name_column='*'):
    cursor.execute(f"SELECT {name_column} FROM {name_table}")
    return cursor.fetchall()
path = os.path.abspath(__file__ + "/../database")
os.chdir(path)

connect = sqlite3.connect("databas31.db")


cursor = connect.cursor()


text_min_max = "↓ " + m_api.temper(m_api.get_data_weth()['list'][0]['main']['temp_max'])+ "° " + " ↑ " + m_api.temper(m_api.get_data_weth()['list'][0]['main']['temp_min']) + "°"


text_where = "Поточна позиція"


city_info = get_value(cursor, "Signed", "city")[0][0]


gradus21w = m_api.temper(m_api.get_data_weth()['list'][0]['main']['temp']) + "°"


text_weather = main_waether("Дніпро")


img = m_ico.iconka(city= "Dnipro")

label1_t = "Київ"

label2_t = "Рим"

label3_t = "Лондон"

label4_t = "Варшава"

label5_t = "Прага"

label6_t = "Дніпро"


frame1_c = "#096C82"

frame2_c = "#096C82"

frame3_c = "#096C82"

frame4_c = "#096C82"

frame5_c = "#096C82"

frame6_c = "#5DA7B1"

gradus1_text = m_api.temper(m_api.get_data_weth(get_value(cursor, "Signed", "city")[0][0])['list'][0]['main']['temp']) + "°"

gradus2_text =  m_api.temper(m_api.get_data_weth(get_value(cursor, "Signed", "city")[0][0])['list'][1]['main']['temp']) + "°"

gradus3_text = m_api.temper(m_api.get_data_weth(get_value(cursor, "Signed", "city")[0][0])['list'][2]['main']['temp']) + "°"

gradus4_text = m_api.temper(m_api.get_data_weth(get_value(cursor, "Signed", "city")[0][0])['list'][3]['main']['temp']) + "°"

gradus5_text = m_api.temper(m_api.get_data_weth(get_value(cursor, "Signed", "city")[0][0])['list'][4]['main']['temp']) + "°"

gradus6_text = m_api.temper(m_api.get_data_weth(get_value(cursor, "Signed", "city")[0][0])['list'][5]['main']['temp']) + "°"

gradus7_text = m_api.temper(m_api.get_data_weth(get_value(cursor, "Signed", "city")[0][0])['list'][6]['main']['temp']) + "°"

gradus8_text = m_api.temper(m_api.get_data_weth(get_value(cursor, "Signed", "city")[0][0])['list'][7]['main']['temp']) + "°"

gradus9_text = m_api.temper(m_api.get_data_weth(get_value(cursor, "Signed", "city")[0][0])['list'][8]['main']['temp']) + "°"









def topi2t():
    global main_scr, city_info, gradus21w, text_where, text_min_max, img, text_weather, frame1_c, label1_t, frame2_c, label2_t, frame3_c, label3_t, frame4_c, label4_t, frame5_c, label5_t, frame6_c, label6_t
    global gradus1_text, gradus2_text, gradus3_text, gradus4_text, gradus5_text, gradus6_text, gradus7_text, gradus8_text, gradus9_text
    vera = search.get()
    # vera1_0 = m_api.main_waether(sf= vera)
    
    main_scr.destroy()

    text_where = " "    
    city_info = vera
    gradus21w = m_api.temper(m_api.get_data_weth(city= vera)['list'][0]['main']['temp']) + "°"
    text_min_max = "↓ " + m_api.temper(m_api.get_data_weth(city= vera)['list'][0]['main']['temp_min'])+ "° " + " ↑ " + m_api.temper(m_api.get_data_weth(city= vera)['list'][0]['main']['temp_max']) + "°"
        
    gradus1_text = m_api.temper(m_api.get_data_weth(city_info)['list'][0]['main']['temp']) + "°"

    gradus2_text =  m_api.temper(m_api.get_data_weth(city_info)['list'][1]['main']['temp']) + "°"

    gradus3_text = m_api.temper(m_api.get_data_weth(city_info)['list'][2]['main']['temp']) + "°"

    gradus4_text = m_api.temper(m_api.get_data_weth(city_info)['list'][3]['main']['temp']) + "°"

    gradus5_text = m_api.temper(m_api.get_data_weth(city_info)['list'][4]['main']['temp']) + "°"

    gradus6_text = m_api.temper(m_api.get_data_weth(city_info)['list'][5]['main']['temp']) + "°"

    gradus7_text = m_api.temper(m_api.get_data_weth(city_info)['list'][6]['main']['temp']) + "°"

    gradus8_text = m_api.temper(m_api.get_data_weth(city_info)['list'][7]['main']['temp']) + "°"

    gradus9_text = m_api.temper(m_api.get_data_weth(city_info)['list'][8]['main']['temp']) + "°"


    img = m_ico.iconka(city= vera)
    text_weather = main_waether(vera)

    if vera == label1_t:
        frame1_c = "#5DA7B1"
    else: 
        frame1_c = "#096C82"

    if vera == label2_t:
        frame2_c = "#5DA7B1"
    else: 
        frame2_c = "#096C82"

    if vera == label3_t:
        frame3_c = "#5DA7B1"
    else: 
        frame3_c = "#096C82"

    if vera == label4_t:
        frame4_c = "#5DA7B1"
    else: 
        frame4_c = "#096C82"

    if vera == label5_t:
        frame5_c = "#5DA7B1"
    else: 
        frame5_c = "#096C82"

    if vera == label6_t:
        frame6_c = "#5DA7B1"
    else: 
        frame6_c = "#096C82"
    
    print(text_weather)
    app_main()


min_maxx11_t = "↓ " + m_api.temper(m_api.get_data_weth("Київ")['list'][0]['main']['temp_min'])+ "° " + " ↑ " + m_api.temper(m_api.get_data_weth()['list'][0]['main']['temp_max']) + "°"

min_maxx2_t = "↓ " + m_api.temper(m_api.get_data_weth("Рим")['list'][0]['main']['temp_min'])+ "° " + " ↑ " + m_api.temper(m_api.get_data_weth()['list'][0]['main']['temp_max']) + "°"

min_maxx3_t = "↓ " + m_api.temper(m_api.get_data_weth("Лондон")['list'][0]['main']['temp_min'])+ "° " + " ↑ " + m_api.temper(m_api.get_data_weth()['list'][0]['main']['temp_max']) + "°"

min_maxx4_t = "↓ " + m_api.temper(m_api.get_data_weth("Варшава")['list'][0]['main']['temp_min'])+ "° " + " ↑ " + m_api.temper(m_api.get_data_weth()['list'][0]['main']['temp_max']) + "°"

min_maxx5_t = "↓ " + m_api.temper(m_api.get_data_weth("Прага")['list'][0]['main']['temp_min'])+ "° " + " ↑ " + m_api.temper(m_api.get_data_weth()['list'][0]['main']['temp_max']) + "°"

min_maxx6_t = "↓ " + m_api.temper(m_api.get_data_weth("Дніпро")['list'][0]['main']['temp_min'])+ "° " + " ↑ " + m_api.temper(m_api.get_data_weth()['list'][0]['main']['temp_max']) + "°"

today = time.localtime()
def today1(index: int):
    global today, tm_mmon, tm_day
    if today.tm_mday < 10:
        tm_day = "0" + str(today.tm_mday)
    else:
        tm_day = today.tm_mday
    if today.tm_mon < 10:
        tm_mmon = "0" + str(today.tm_mon)
    else:
        tm_mmon = today.tm_mon
    if today.tm_hour < 10:
        tm_hhour = "0" + str(today.tm_hour)
    else:
        tm_hhour = today.tm_hour
    if today.tm_min < 10:
        tm_mmin = "0" + str(today.tm_min)
    else:
        tm_mmin = today.tm_min
    if index == 1:
        return tm_day
    elif index == 2:
        return tm_mmon
    elif index == 3:
        return tm_hhour
    elif index == 4:
        return tm_mmin

def another():
    global city_super
    city_super._text = "ndsllajdksj"
def app_main():
    global main_scr, today, city_super, tm_mmon, tm_day, search, connect, cursor, path, gradus21w, img, text_weather, frame1_c, label1_t, frame2_c, label2_t, frame3_c, label3_t, frame4_c, label4_t, frame5_c, label5_t, frame6_c, label6_t

    main_scr = customtkinter.CTkToplevel()
    main_scr.geometry("1200x800")
    main_scr.config(bg="#5DA7B1")
    main_scr.resizable(False, False)
    main_scr.title("Main Window")
    main_scr.iconbitmap(os.path.abspath(__file__ + "/../../2.ico"))

    text_for_date = f"{today1(index=1)}.{today1(index=2)}.{today.tm_year}"
    print(today)

    text_time = f"{today1(3)}:{today1(4)}"

    def go_to_toiletik():
        main_scr.destroy()
        import modules.cabinet as m_cab
        m_cab.cabinet_scr = customtkinter.CTk()
        m_cab.cabinet_scr.geometry("460x645")
        m_cab.cabinet_scr.config(bg="#5DA7B1")
        m_cab.cabinet_scr.resizable(False, False)
        m_cab.create_win_cabinka()
        m_cab.cabinet_scr.mainloop()
    name = get_value(cursor, 'Signed', 'name')[0][0]

    surname =get_value(cursor, 'Signed', 'lastname')[0][0]


    go_cabinka = customtkinter.CTkButton(
        master= main_scr,
        width= 0,
        height= 31,
        fg_color="#5DA7B1",
        bg_color="#5DA7B1",
        font= (m_font.font, 14),
        hover= False,
        border_width=0,
        command=go_to_toiletik,
        text= name+ " " +surname,
        text_color= "#FFFFFF"
    )



    date = customtkinter.CTkLabel(
        master= main_scr,
        width= 160,
        height= 47,
        text= text_for_date,
        text_color= "#FFFFFF",
        font= (m_font.font,40),
        fg_color= "#5DA7B1",
        bg_color= "#5DA7B1"     
    )

    time22 = customtkinter.CTkLabel(
        master= main_scr,
        width= 70,
        height= 47,
        text= text_time,
        text_color= "#FFFFFF",
        font= (m_font.font,30),
        fg_color="#5DA7B1",
        bg_color="#5DA7B1"
    )

    where = customtkinter.CTkLabel(
        master= main_scr,
        width= 214,
        height= 61,
        text= text_where,
        text_color= "#FFFFFF",
        font=(m_font.font,35),
        fg_color= "#5DA7B1",
        bg_color= "#5DA7B1"
    )
    fram3 = customtkinter.CTkButton(
        master = main_scr,
        text = "",
        width = 818,
        height = 240,
        bg_color="#5DA7B1",
        fg_color="#5DA7B1",
        border_width = 5,
        border_color = "#FFFFFF",
        corner_radius= 20,
        hover = False
    )
    fram3.place(x = 325, y = 430)
    print("10")
    left_widget = customtkinter.CTkButton(
        master= main_scr,
        width= 275,
        height= 800,
        fg_color="#096C82",
        bg_color="#5DA7B1",
        border_width=3,
        border_color="#FFFFFF",
        text= " ",
        hover= False
    )    
            


    city_super = customtkinter.CTkLabel(
        master=main_scr,
        text=city_info,
        text_color="#FFFFFF",
        width=87,
        height=31,
        font=(m_font.font,22),
        bg_color="#5DA7B1",
        fg_color="#5DA7B1",
    )
    gradus1 = customtkinter.CTkLabel(
        master = main_scr,
        text = gradus21w,
        width = 79,
        height = 71,
        font = ("Inter Bold",80),
        bg_color="#5DA7B1",
        fg_color="#5DA7B1",
        text_color = "#FFFFFF"
    )
    
    day = customtkinter.CTkLabel(
        master= main_scr,
        width = 105,
        text= m_api.text_day,
        font= (m_font.font,27),
        bg_color="#5DA7B1",
        fg_color="#5DA7B1",
        text_color = "#FFFFFF"
    )


    weather1 = customtkinter.CTkLabel(
        master= main_scr,
        text = text_weather,
        width = 140,
        height = 31,
        font = (m_font.font,30),
        bg_color = "#5DA7B1",
        fg_color = "#5DA7B1",
        text_color = "#FFFFFF"
    )
    print("img")
    
    print(img)
    img1 = customtkinter.CTkImage(dark_image= img, size= [171, 159])
    print(img1)
    img1_lbl = customtkinter.CTkLabel(master= main_scr,width= 171,height=159,fg_color = "#5DA7B1",bg_color= "#5DA7B1",text="",image= img1)




    img2_1 = Image.open(os.path.abspath(__file__ + f"/../../images/user.png"))
    img2_2 = customtkinter.CTkImage(dark_image= img2_1, size= [48, 50])
    img2_lbl = customtkinter.CTkLabel(master= main_scr,width= 48.48,height=50,fg_color = "#5DA7B1",bg_color= "#5DA7B1",text="",image= img2_2)

    # img3_1 = Image.open(os.path.abspath(__file__ + "/../../images/lata.png"))
    img3_2 = customtkinter.CTkImage(dark_image= img, size= [50, 52])
    img3_lbl = customtkinter.CTkLabel(master= main_scr,width= 50,height=52.08,fg_color = "#5DA7B1",bg_color= "#5DA7B1",text="",image= img3_2)

    img4_1 = Image.open(os.path.abspath(__file__ + "/../../images/sun.png"))
    img4_2 = customtkinter.CTkImage(dark_image= img, size= [54, 50])
    img4_lbl = customtkinter.CTkLabel(master= main_scr,width= 54,height=50,fg_color = "#5DA7B1",bg_color= "#5DA7B1",text="",image= img4_2)

    img5_1 = Image.open(os.path.abspath(__file__ + "/../../images/sun.png"))
    img5_2 = customtkinter.CTkImage(dark_image= img, size= [54, 50])
    img5_lbl = customtkinter.CTkLabel(master= main_scr,width= 54,height=50,fg_color = "#5DA7B1",bg_color= "#5DA7B1",text="",image= img5_2)
    
    img6_1 = Image.open(os.path.abspath(__file__ + "/../../images/sun1.png"))
    img6_2 = customtkinter.CTkImage(dark_image= img, size= [50, 50])
    img6_lbl = customtkinter.CTkLabel(master= main_scr,width= 50,height=50,fg_color = "#5DA7B1",bg_color= "#5DA7B1",text="",image= img6_2)

    img7_1 = Image.open(os.path.abspath(__file__ + "/../../images/night.png"))
    img7_2 = customtkinter.CTkImage(dark_image= img, size= [50, 50])
    img7_lbl = customtkinter.CTkLabel(master= main_scr,width= 50,height=50,fg_color = "#5DA7B1",bg_color= "#5DA7B1",text="",image= img7_2)

    img8_1 = Image.open(os.path.abspath(__file__ + "/../../images/night.png"))
    img8_2 = customtkinter.CTkImage(dark_image= img, size= [50, 50])
    img8_lbl = customtkinter.CTkLabel(master= main_scr,width= 50,height=50,fg_color = "#5DA7B1",bg_color= "#5DA7B1",text="",image= img8_2)

    img9_1 = Image.open(os.path.abspath(__file__ + "/../../images/rain.png"))
    img9_2 = customtkinter.CTkImage(dark_image= img, size= [50, 50])
    img9_lbl = customtkinter.CTkLabel(master= main_scr,width= 50,height=50,fg_color = "#5DA7B1",bg_color= "#5DA7B1",text="",image= img9_2)

    img10_1 = Image.open(os.path.abspath(__file__ + "/../../images/rain.png"))
    img10_2 = customtkinter.CTkImage(dark_image= img, size= [50, 50])
    img10_lbl = customtkinter.CTkLabel(master= main_scr,width= 50,height=50,fg_color = "#5DA7B1",bg_color= "#5DA7B1",text="",image= img10_2)

    img11_1 = Image.open(os.path.abspath(__file__ + "/../../images/rain.png"))
    img11_2 = customtkinter.CTkImage(dark_image= img, size= [50, 50])
    img11_lbl = customtkinter.CTkLabel(master= main_scr,width= 50,height=50,fg_color = "#5DA7B1",bg_color= "#5DA7B1",text="",image= img11_2)
    print("end imgs")

    gradus = customtkinter.CTkLabel(
        master = main_scr,
        text = gradus1_text,
        width = 41.02,
        height = 30,
        font = ("Roboto Slab Bold", 30),
        bg_color="#5DA7B1",
        fg_color="#5DA7B1",
        text_color = "#FFFFFF"
    )
    gradus2 = customtkinter.CTkLabel(
        master = main_scr,
        text = gradus2_text,
        width = 45,
        height = 30,
        font = ("Roboto Slab Bold", 30),
        bg_color="#5DA7B1",
        fg_color="#5DA7B1",
        text_color = "#FFFFFF"
    )
    gradus3 = customtkinter.CTkLabel(
        master = main_scr,
        text = gradus3_text,
        width = 48,
        height = 30,
        font = ("Roboto Slab Bold", 30),
        bg_color="#5DA7B1",
        fg_color="#5DA7B1",
        text_color = "#FFFFFF"  
    )
    gradus4 = customtkinter.CTkLabel(
        master = main_scr,
        text = gradus4_text,
        width = 32.25,
        height = 30,
        font = ("Roboto Slab Bold", 30),
        bg_color="#5DA7B1",
        fg_color="#5DA7B1",
        text_color = "#FFFFFF"
    )
    gradus5 = customtkinter.CTkLabel(
        master = main_scr,
        text = gradus5_text,
        width = 32.25,
        height = 30,
        font = ("Roboto Slab Bold", 30),
        bg_color="#5DA7B1",
        fg_color="#5DA7B1",
        text_color = "#FFFFFF"  
    )
    gradus6 = customtkinter.CTkLabel(
        master = main_scr,
        text = gradus6_text,
        width = 32.25,
        height = 30,
        font = ("Roboto Slab Bold", 30),
        bg_color="#5DA7B1",
        fg_color="#5DA7B1",
        text_color = "#FFFFFF"
    )
    gradus7= customtkinter.CTkLabel(
        master = main_scr,
        text = gradus7_text,
        width = 32.25,
        height = 30,
        font = ("Roboto Slab Bold", 30),
        bg_color="#5DA7B1",
        fg_color="#5DA7B1",
        text_color = "#FFFFFF"  
    )
    gradus8= customtkinter.CTkLabel(
        master = main_scr,
        text = gradus8_text,
        width = 32.25,
        height = 30,
        font = ("Roboto Slab Bold", 30),
        bg_color="#5DA7B1",
        fg_color="#5DA7B1",
        text_color = "#FFFFFF"  
    )
    gradus9= customtkinter.CTkLabel(
        master = main_scr,
        text = gradus9_text,
        width = 32.25,
        height = 30,
        font = ("Roboto Slab Bold", 30),
        bg_color="#5DA7B1",
        fg_color="#5DA7B1",
        text_color = "#FFFFFF"  
    )
    # time.struct_time(tm_year=2023, tm_mon=12, tm_mday=29, tm_hour=22, tm_min=3, tm_sec=16, tm_wday=4, tm_yday=363, tm_isdst=0)

    times = lambda plus: f"{plus+time.localtime()[3]}:00" if plus+time.localtime()[3] > 23 else f"{plus+time.localtime()[3]-24}:00"
        
    time11 = m_time.crttm("Зараз")
    time2 = m_time.crttm(f"{(time.localtime()[3]+1)%24}:00")
    time3 = m_time.crttm(f"{(time.localtime()[3]+2)%24}:00")
    time4 = m_time.crttm(f"{(time.localtime()[3]+3)%24}:00")
    time5 = m_time.crttm(f"{(time.localtime()[3]+4)%24}:00")
    time6 = m_time.crttm(f"{(time.localtime()[3]+5)%24}:00")
    time7 = m_time.crttm(f"{(time.localtime()[3]+6)%24}:00")
    time8 = m_time.crttm(f"{(time.localtime()[3]+7)%24}:00")
    time9 = m_time.crttm(f"{(time.localtime()[3]+8)%24}:00")
    print("gradusnik 411")
    

    smaller = customtkinter.CTkLabel(
        master = main_scr,
        text = "<", 
        text_color = "#FFFFFF",
        height = 31,
        font = (m_font.font, 50),
        bg_color="#5DA7B1",
        fg_color="#5DA7B1",
    )
    bigger = customtkinter.CTkLabel(
        master = main_scr,
        text = ">", 
        text_color = "#FFFFFF",
        height = 31,
        font = (m_font.font, 50),
        bg_color="#5DA7B1",
        fg_color="#5DA7B1",
    )

    search = customtkinter.CTkEntry(
        master = main_scr,
        width = 218,
        height = 46,
        font = (m_font.font, 18),
        bg_color ="#5DA7B1",
        fg_color ="#096C82",
        border_width = 3,
        corner_radius = 20,
        border_color = "#FFFFFF",
        placeholder_text='Пошук'
    )
    print("446")
    
    

    frame1 = customtkinter.CTkFrame(
        master = main_scr,
        width = 236,
        height = 101,
        corner_radius = 20,
        border_width = 2,
        bg_color = "#096C82",
        fg_color = frame1_c,
        border_color = "#FFFFFF"
    )
    label1 = customtkinter.CTkLabel(
        master = main_scr,
        height = 31,
        text = label1_t,
        font = (m_font.font, 16),
        bg_color = frame1_c,
        fg_color = frame1_c,
        text_color = "#FFFFFF"
    )
    frame2 = customtkinter.CTkFrame(
        master = main_scr,
        width = 236,
        height = 101,
        corner_radius = 20,
        border_width = 2,
        bg_color = "#096C82",
        fg_color = frame2_c,
        border_color = "#FFFFFF"
    )
    label2 = customtkinter.CTkLabel(
        master = main_scr,
        height = 31,
        text = label2_t,
        font = (m_font.font, 16),
        bg_color = frame2_c,
        fg_color = frame2_c,
        text_color = "#FFFFFF"   
    )
    frame3 = customtkinter.CTkFrame(
        master = main_scr,
        width = 236,
        height = 101,
        corner_radius = 20,
        border_width = 2,
        bg_color = "#096C82",
        fg_color = frame3_c,
        border_color = "#FFFFFF"
    )
    label3 = customtkinter.CTkLabel(
        master = main_scr,
        height = 31,
        text = label3_t,
        font = (m_font.font, 16),
        bg_color = frame3_c,
        fg_color = frame3_c,
        text_color = "#FFFFFF"   
    )
    frame4 = customtkinter.CTkFrame(
        master = main_scr,
        width = 236,
        height = 101,
        corner_radius = 20,
        border_width = 2,
        bg_color = "#096C82",
        fg_color = frame4_c,
        border_color = "#FFFFFF"
    )
    label4 = customtkinter.CTkLabel(
        master = main_scr,
        height = 31,
        text = label4_t,
        font = (m_font.font, 16),
        bg_color = frame4_c,
        fg_color = frame4_c,
        text_color = "#FFFFFF"   
    )
    frame5 = customtkinter.CTkFrame(
        master = main_scr,
        width = 236,
        height = 101,
        corner_radius = 20,
        border_width = 2,
        bg_color = "#096C82",
        fg_color = frame5_c,
        border_color = "#FFFFFF"
    )
    label5 = customtkinter.CTkLabel(
        master = main_scr,
        height = 31,
        text = label5_t,
        font = (m_font.font, 16),
        bg_color = frame5_c,
        fg_color = frame5_c,
        text_color = "#FFFFFF"   
    )
    frame6 = customtkinter.CTkFrame(
        master = main_scr,
        width = 236,
        height = 101,
        corner_radius = 20,
        border_width = 2,
        bg_color = "#096C82",
        fg_color = frame6_c,
        border_color = "#FFFFFF"
    )
    label6 = customtkinter.CTkLabel(
        master = main_scr,
        height = 17,
        text = label6_t,
        font = (m_font.font, 12),
        bg_color = frame6_c,
        fg_color = frame6_c,
        text_color = "#FFFFFF"   
    )
    label61 = customtkinter.CTkLabel(
        master = main_scr,
        height = 31,
        text = "Поточна позиція",
        font = (m_font.font, 16),
        bg_color = frame6_c,
        fg_color = frame6_c,
        text_color = "#FFFFFF"   
    )
    print("570")
    print("ilf1")
    ilf1 = customtkinter.CTkLabel(
        master= main_scr,
        height = 42,
        text = m_api.ilf1_t,
        font = ("Inter", 40),
        bg_color = frame1_c,
        fg_color = frame1_c,
        text_color = "#FFFFFF"   
    )
    print("ilf2")
    ilf2 = customtkinter.CTkLabel(
        master= main_scr,
        height = 42,
        text = m_api.ilf2_t,
        font = ("Inter", 40),
        bg_color = frame2_c,
        fg_color = frame2_c,
        text_color = "#FFFFFF"   
    )
    print("ilf3")
    ilf3 = customtkinter.CTkLabel(
        master= main_scr,
        height = 42,
        text = m_api.ilf3_t,
        font = ("Inter", 40),
        bg_color = frame3_c,
        fg_color = frame3_c,
        text_color = "#FFFFFF"   
    )
    print("ilf4")
    ilf4 = customtkinter.CTkLabel(
        master= main_scr,
        height = 42,
        text = m_api.ilf4_t,
        font = ("Inter", 40),
        bg_color = frame4_c,
        fg_color = frame4_c,
        text_color = "#FFFFFF"   
    )
    print("ilf5")
    ilf5 = customtkinter.CTkLabel(
        master= main_scr,
        height = 42,
        text = m_api.ilf5_t,
        font = ("Inter", 40),
        bg_color = frame5_c,
        fg_color = frame5_c,
        text_color = "#FFFFFF"   
    )
    print("ilf6")
    ilf6 = customtkinter.CTkLabel(
        master= main_scr,
        height = 42,
        text = m_api.ilf6_t,
        font = ("Inter", 40),
        bg_color = frame6_c,
        fg_color = frame6_c,
        text_color = "#FFFFFF"   
    )
    
    print("ilf 626")
    weath1 = customtkinter.CTkLabel(
        master= main_scr,
        height = 14,
        text = m_api.wth1_t,
        font = (m_font.font, 12),
        bg_color = frame1_c,
        fg_color = frame1_c,
        text_color = "#FFFFFF"  
    )
    weath2 = customtkinter.CTkLabel(
        master= main_scr,
        height = 14,
        text = m_api.wth2_t,
        font = (m_font.font, 12),
        bg_color = frame2_c,
        fg_color = frame2_c,
        text_color = "#FFFFFF"  
    )
    weath3 = customtkinter.CTkLabel(
        master= main_scr,
        height = 14,
        text = m_api.wth3_t,
        font = (m_font.font, 12),
        bg_color = frame3_c,
        fg_color = frame3_c,
        text_color = "#FFFFFF"  
    )
    weath4 = customtkinter.CTkLabel(
        master= main_scr,
        height = 14,
        text = m_api.wth4_t,
        font = (m_font.font, 12),
        bg_color = frame4_c,
        fg_color = frame4_c,
        text_color = "#FFFFFF"  
    )
    weath5 = customtkinter.CTkLabel(
        master= main_scr,
        height = 14,
        text = m_api.wth5_t,
        font = (m_font.font, 12),
        bg_color = frame5_c,
        fg_color = frame5_c,
        text_color = "#FFFFFF"  
    )
    weath6 = customtkinter.CTkLabel(
        master= main_scr,
        height = 14,
        text = m_api.wth6_t,
        font = (m_font.font, 12),
        bg_color = frame6_c,
        fg_color = frame6_c,
        text_color = "#FFFFFF"  
    )
    print("681")


    min_maxx1 = customtkinter.CTkLabel(
        master = main_scr,
        text = text_min_max,
        height = 30,
        font = ("Roboto Slab Bold", 30),
        bg_color="#5DA7B1",
        fg_color="#5DA7B1",
        text_color = "#FFFFFF"
    )
    min_maxx1.place(x = 670, y = 335)

    def go_fon():
        main_scr.destroy()
        import modules.mini4screen as minimum
        
        # minimum.mini4scr = customtkinter.CTkToplevel()
        # minimum.mini4scr.geometry("350x350")
        # minimum.mini4scr.config(bg="#5DA7B1")
        # minimum.mini4scr.resizable(False, False)
        minimum.mini4sr()
    
    button_go_finland = customtkinter.CTkButton(
        master = main_scr,
        text = "Перейти в фоновий режим",
        height = 31,
        font = (m_font.font, 15),    
        bg_color = "#5DA7B1",
        fg_color = "#5DA7B1",
        text_color = "#FFFFFF",
        command = go_fon,
        hover= False
    )
    button_go_finland.place(x = 920, y = 115)
    print("1")
    min_maxx11 = customtkinter.CTkLabel(
        master = main_scr,
        text = min_maxx11_t,
        height = 14,
        font = ("Roboto Slab Bold", 12),
        bg_color = frame1_c,
        fg_color = frame1_c,
        text_color = "#FFFFFF"
    )
    print("2")
    min_maxx2 = customtkinter.CTkLabel(
        master = main_scr,
        text = min_maxx2_t,
        height = 14,
        font = ("Roboto Slab Bold", 12),
        bg_color = frame2_c,
        fg_color = frame2_c,
        text_color = "#FFFFFF"
    )
    print("3")
    min_maxx3 = customtkinter.CTkLabel(
        master = main_scr,
        text = min_maxx3_t,
        height = 14,
        font = ("Roboto Slab Bold", 12),
        bg_color = frame3_c,
        fg_color = frame3_c,
        text_color = "#FFFFFF"
    )
    print("4")
    min_maxx4 = customtkinter.CTkLabel(
        master = main_scr,
        text = min_maxx4_t,
        height = 14,
        font = ("Roboto Slab Bold", 12),
        bg_color = frame4_c,
        fg_color = frame4_c,
        text_color = "#FFFFFF"
    )
    print("5")
    min_maxx5 = customtkinter.CTkLabel(
        master = main_scr,
        text = min_maxx5_t,
        height = 14,
        font = ("Roboto Slab Bold", 12),
        bg_color = frame5_c,
        fg_color = frame5_c,
        text_color = "#FFFFFF"
    )
    print("6")
    min_maxx1 = customtkinter.CTkLabel(
        master = main_scr,
        text = min_maxx6_t,
        height = 14,
        font = ("Roboto Slab Bold", 12),
        bg_color = frame6_c,
        fg_color = frame6_c,
        text_color = "#FFFFFF"
    )

    
    
    
    

    img22_1 = Image.open(os.path.abspath(__file__ + f"/../../images/search.png"))
    img22_2 = customtkinter.CTkImage(dark_image= img22_1, size= [27, 27])
    
    poshyk = customtkinter.CTkButton(
        master= main_scr, 
        width = 27,
        height = 27,
        bg_color = "#096C82",
        fg_color = "#096C82",
        text= "",
        image= img22_2,
        hover= False, command= topi2t
    )




    min_maxx1.place(x = 175, y = 107)
    min_maxx11.place(x = 175, y = 240)
    min_maxx2.place(x = 175, y = 371)
    min_maxx3.place(x = 175, y = 506)
    min_maxx4.place(x = 175, y = 639)
    min_maxx5.place(x = 175, y = 772)

    print("10")
    frame1.place(x = 19, y = 164)
    frame2.place(x = 19, y = 291)
    frame3.place(x = 19, y = 430)
    frame4.place(x = 19, y = 563)
    frame5.place(x = 19, y = 696)
    frame6.place(x= 19 , y =31)

    print("20")
    label1.place(x= 33, y= 172)
    label2.place(x= 33, y= 305)
    label3.place(x= 33, y= 443)
    label4.place(x= 33, y= 576)
    label5.place(x= 33, y= 709)
    label61.place(x= 27,y = 39)
    label6.place(x= 33,y = 66)

    print("30")
            
    ilf1.place(x= 177,y= 176)
    ilf2.place(x= 177,y= 309)
    ilf3.place(x= 177,y= 442)
    ilf4.place(x= 177,y= 575)
    ilf5.place(x= 177,y= 708)
    ilf6.place(x= 177,y= 43)

    print("40")
    weath1.place(x= 33,y=757)
    weath2.place(x= 33,y=235)
    weath3.place(x= 33,y=363)
    weath4.place(x= 33,y=496)
    weath5.place(x= 33,y=624)
    weath6.place(x= 33,y=92)

    search.place(x = 918, y = 31)
    smaller.place(x = 289, y = 524)
    bigger.place(x = 1160, y = 524)
    print("50")

    gradus.place(x = 351, y = 604)
    gradus2.place(x = 445, y = 604)
    gradus3.place(x = 534, y = 604)
    gradus4.place(x = 635, y = 604)
    gradus5.place(x = 731, y = 604)
    gradus6.place(x = 823, y = 604)
    gradus7.place(x = 915, y = 604)
    gradus8.place(x = 1007, y = 604)
    gradus9.place(x = 1099, y = 604)
    print("60")
    
    time11.place(x = 344,y = 485)
    time2.place(x = 441,y = 485)
    time3.place(x = 533,y = 485)
    time4.place(x = 625,y = 485)
    time5.place(x = 717,y = 485)
    time6.place(x = 809,y = 485)
    time7.place(x = 901,y = 485)
    time8.place(x = 993,y = 485)
    time9.place(x = 1085,y = 485)
    print("70")
    
    img3_lbl.place(x = 344, y = 534)
    img4_lbl.place(x = 437, y = 534)
    img5_lbl.place(x = 523, y = 534)
    img6_lbl.place(x = 621, y = 534)
    img7_lbl.place(x = 713, y = 534)
    img8_lbl.place(x = 805, y = 534)
    img9_lbl.place(x = 897, y = 534)
    img10_lbl.place(x = 989, y = 534)
    img11_lbl.place(x = 1081, y = 534)
    print("80")
    # name_and_surname.place(x = 380, y = 39)

    day.place(x= 956, y= 201, anchor="w")
    img2_lbl.place(x = 318, y= 29)
    img1_lbl.place(x= 380, y= 171)
    weather1.place(x=663, y= 284)
    gradus1.place(x = 683, y = 203)
    city_super.place(x = 689, y = 162)
    go_cabinka.place(x= 380,y= 39)
    left_widget.place(x = 0, y = 0)
    where.place(x = 576, y = 101)
    time22.place(x = 974, y = 274)
    date.place(x = 920, y = 227)

    poshyk.place(x= 1080,y= 37)

    main_scr.mainloop()
    print("90")