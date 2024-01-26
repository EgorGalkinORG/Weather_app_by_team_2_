import os , customtkinter, sqlite3, time
from PIL import Image
import modules.font as m_font
import modules.api as m_api
import modules.icons as m_ico



path = os.path.abspath(__file__ + "/../database")
os.chdir(path)
connect = sqlite3.connect(os.path.abspath(__file__ + "/../database/databas31.db"))
cursor = connect.cursor()
# print('------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
def main_waether(sf: str):

    data = m_api.get_data_weth()['weather'][0]['main']

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

def mini4sr():
    global mini4scr
    mini4scr = customtkinter.CTkToplevel()
    mini4scr.geometry("350x350")
    mini4scr.config(bg="#5DA7B1")
    mini4scr.resizable(False, False)
    mini4scr.title("Mini Screen (Widget)")
    def go_app1():
        mini4scr.destroy()



        cursor.execute("INSERT INTO Signed (backb, signid) VALUES (?, ?)", ("fs", True))

        connect.commit()
        connect.close()
        import modules.main_window as main_app
        main_app.main_scr = customtkinter.CTk()
        main_app.main_scr.geometry("1200x800")
        main_app.main_scr.config(bg="#5DA7B1")
        main_app.main_scr.resizable(False, False)
        
        main_app.app_main()
        main_app.main_scr.mainloop()
    frame14 = customtkinter.CTkButton(
        master= mini4scr,
        height= 350,
        width= 350,
        border_color= "#096C82",
        corner_radius= 20,fg_color= "#5DA7B1", border_width= 5,
        command=go_app1, hover= False, text= ""
    )
    frame14.place(x = 0, y = 0)

    pogoda2 = customtkinter.CTkLabel(
        master = mini4scr,
        text = main_waether("Дніпро"),
        height = 31,
        font = (m_font.font,30),
        bg_color = "#5DA7B1",
        fg_color = "#5DA7B1",
        text_color = "#FFFFFF"
    )

    gradus1 = customtkinter.CTkLabel(
        master = mini4scr,
        text = m_api.temper(m_api.get_data_weth()["main"]['temp']) + "°",
        font = ("Roboto Slab Bold", 80),
        bg_color="#5DA7B1",
        fg_color="#5DA7B1",
        text_color = "#FFFFFF"
    )
    img = m_ico.img
    img1 = customtkinter.CTkImage(dark_image= img, size= [159.59, 142])
    img1_lbl1 = customtkinter.CTkLabel(master= mini4scr,width= 151,height=159,fg_color = "#5DA7B1",bg_color= "#5DA7B1",text="",image= img1)
    wheteere = customtkinter.CTkLabel(master= mini4scr,bg_color= "#5DA7B1",text="Дніпро", font = (m_font.font, 40), text_color="#FFFFFF")

    img11 = Image.open(os.path.abspath(__file__ + "/../../images/captcha.png"))
    img22 = customtkinter.CTkImage(dark_image= img11, size= [25, 25])
    
    button_go_app1 = customtkinter.CTkButton(
        master= mini4scr,
        width= 25,
        height=25,
        fg_color = "#5DA7B1",bg_color= "#5DA7B1",text="",image= img22,
        command= go_app1,
        hover= False

    )
    
    min_maxx1 = customtkinter.CTkLabel(
        master = mini4scr,
        text = "↓ " + m_api.temper(m_api.get_data_weth()["main"]['temp_max']) + "° " + " ↑ " + m_api.temper(m_api.get_data_weth()["main"]['temp_min']) + "°",
        height = 30,
        font = ("Roboto Slab Bold", 30),
        bg_color="#5DA7B1",
        fg_color="#5DA7B1",
        text_color = "#FFFFFF"
    )
    button_go_app1.place(x = 300, y = 20)
    min_maxx1.place(x = 55 , y = 215)
    gradus1.place(x = 245,y = 191)
    wheteere.place(x = 180, y = 274)
    img1_lbl1.place(x = 17, y = 5)
    pogoda2.place(x = 47, y = 162)