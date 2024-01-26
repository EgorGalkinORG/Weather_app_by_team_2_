import os, sqlite3, customtkinter
import modules.api
# cab_scr = None
import modules.sign_up as m_sign
cabinet_scr = customtkinter.CTk()
cabinet_scr.geometry("460x645")
cabinet_scr.config(bg="#5DA7B1")
cabinet_scr.resizable(False, False)
def go_background():
    connect = sqlite3.connect(os.path.abspath(__file__ + "/../database/databas31.db"))
    cursor = connect.cursor()
    try:
        cursor.execute("ALTER TABLE Signed ADD COLUMN backb TEXT")
    except:
        print("Dublicate columm")
    try:
        cursor.execute("INSERT INTO Signed (backb) VALUES (?)", ("tr"))
    except:
        pass
    connect.commit()
    connect.close()
def get_value(cursor: object, name_table: str, name_column: str = '*'):
    try:
        cursor.execute(f"SELECT {name_column} FROM {name_table}")
        return cursor.fetchall()
    except:
        print("Error Epta")
def quit():
    global cabinet_scr
    cabinet_scr.destroy()
    print("start1")
    import modules.sign_up as m_sing_ips
    print("start2")
    connect = m_sign.connect
    cursor = connect.cursor()
    list_columns = ["country", "city", "name", "lastname"]
    cursor.execute("DROP TABLE Signed")
    cursor.execute("CREATE TABLE Signed (id, INTEGER PRIMARY KEY)")  
    
    for column in list_columns:

        cursor.execute(f'ALTER TABLE Signed ADD COLUMN {column} TEXT')
        # cursor.execute(f'A')
    cursor.execute(f'ALTER TABLE Signed ADD COLUMN signid BOOLEAN')

    m_sing_ips.sign_up_scr = customtkinter.CTk()
    m_sing_ips.sign_up_scr.geometry("460x645")
    m_sing_ips.sign_up_scr.config(bg="#5DA7B1")
    m_sing_ips.sign_up_scr.resizable(False, False)
    
    print("start7")
    
    m_sing_ips.app_reg()
    
    
    m_sing_ips.sign_up_scr.mainloop()

path = os.path.abspath(__file__ + "/../database")
os.chdir(path)
connect = sqlite3.connect("databas31.db")
cursor = connect.cursor()
def create_win_cabinka():
    global connect, cursor, cabinet_scr
    cabinet_scr.title("Main Window")
    cabinet_scr.iconbitmap(os.path.abspath(__file__ + "/../../2.ico"))
    frame14 = customtkinter.CTkFrame(
        master= cabinet_scr,
        height= 645,
        width= 460,
        border_color= "#096C82",
        corner_radius= 20,fg_color= "#5DA7B1", border_width= 5, 
    )
    frame14.place(x = 0, y = 0)


    fontr = 'Roboto Slab Bold'

    country_text = customtkinter.CTkLabel(
        master= cabinet_scr,
        width= 87,
        height= 31,
        fg_color= "#5DA7B1",
        bg_color= "#5DA7B1",
        text="Країна:",
        text_color="#FFFFFF",
        font=(fontr, 22)
    )
    city_text = customtkinter.CTkLabel(
        master= cabinet_scr,
        width= 87,
        height= 31,
        fg_color= "#5DA7B1",
        bg_color= "#5DA7B1",
        text="Місто:",
        text_color="#FFFFFF",
        font=(fontr, 22)
    )
    name_text = customtkinter.CTkLabel(
        master= cabinet_scr,
        width= 87,
        height= 31,
        fg_color= "#5DA7B1",
        bg_color= "#5DA7B1",
        text="Ім'я:",
        text_color="#FFFFFF",
        font=(fontr, 22)
    )
    lastname_text = customtkinter.CTkLabel(

        master= cabinet_scr,
        width= 121,
        height= 31,
        fg_color= "#5DA7B1",
        bg_color= "#5DA7B1",
        text="Призвіще:",
        text_color="#FFFFFF",
        font=(fontr, 22)
    )

    country_info = get_value(cursor, "Signed", "country")[0][0]
    city_info = get_value(cursor, "Signed", "city")[0][0]
    name_info =  get_value(cursor, "Signed", "name")[0][0]
    last_name_info = get_value(cursor, "Signed", "lastname")[0][0]
        
    country_info_text =customtkinter.CTkLabel(
        master= cabinet_scr,
        width= 196,
        height= 31,
        fg_color="#5DA7B1",
        bg_color= "#5DA7B1",
        text_color="#FFFFFF",
        text=country_info,
        font= (fontr, 28)
    )
    city_info_text = customtkinter.CTkLabel(
        master= cabinet_scr,
        width= 196,
        height= 31,
        fg_color="#5DA7B1",
        bg_color= "#5DA7B1",
        text_color="#FFFFFF",
        text=city_info,
        font= (fontr, 28)
    )
    name_info_text = customtkinter.CTkLabel(
        master= cabinet_scr,
        width= 196,
        height= 31,
        fg_color="#5DA7B1",
        bg_color= "#5DA7B1",
        text_color="#FFFFFF",
        text=name_info,
        font= (fontr, 28)
    )
    last_name_info_text = customtkinter.CTkLabel(
        master= cabinet_scr,
        width= 196,
        height= 31,
        fg_color="#5DA7B1",
        bg_color= "#5DA7B1",
        text_color="#FFFFFF",
        text=last_name_info,
        font= (fontr, 28)
    )


    button_left_of_acc = customtkinter.CTkButton(
        master= cabinet_scr,
        width= 36,
        height= 13,
        hover= False,
        fg_color="#5DA7B1",
        bg_color= "#5DA7B1",
        text="Вихід",
        text_color="#FFFFFF",
        font= (fontr, 12),
        command= quit
    )
    header_text = customtkinter.CTkLabel(
    master= cabinet_scr,
    width= 380,
    height= 55,
    fg_color= "#5DA7B1",
    bg_color= "#5DA7B1",
    text="Особистий кабінет",
    text_color= "#FFFFFF",
    font=(fontr, 28)
    )

    def go_app():
        cabinet_scr.destroy()
        go_background()
        import modules.main_window as main_app
        main_app.app_main()



    button_go_app = customtkinter.CTkButton(
    master= cabinet_scr,
    width= 218,
    height=46,
    fg_color="#096C82",
    bg_color="#5DA7B1",
    border_width=3,
    border_color="#FFFFFF",
    text= "Перейти до додатку",
    text_color="#FFFFFF",
    font=(fontr, 18),
    corner_radius=20,
    command=go_app
    )

    country_text.place(x=46,y=108)
    city_text.place(x=46,y=207)
    name_text.place(x=46,y=306)
    lastname_text.place(x=46,y=405)
    country_info_text.place(x=119,y=157)
    city_info_text.place(x=121,y=256)
    name_info_text.place(x=121,y=352)
    last_name_info_text.place(x=119,y=455)

    header_text.place(x=38, y=42)
    button_left_of_acc.place(x=370 ,y=26)
    # text_for_button = "Перейти до додатку"
    button_go_app.place(x=119, y=546)
    # connect.close()

