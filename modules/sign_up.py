import os, sqlite3, customtkinter

import modules.font as m_font
sign_up_scr = customtkinter.CTk()
sign_up_scr.geometry("460x645")
sign_up_scr.config(bg="#5DA7B1")
sign_up_scr.resizable(False, False)

def get_value(cursor: object, name_table='Signed', name_column='*'):
    cursor.execute(f"SELECT {name_column} FROM {name_table}")
    return cursor.fetchall()
path = os.path.abspath(__file__ + "/../database")
os.chdir(path)
connect = sqlite3.connect(os.path.abspath(__file__ + "/../database/databas31.db"))
cursor = connect.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS Signed (id, INTEGER PRIMARY KEY)")
try:                
    cursor.execute("ALTER TABLE Signed ADD COLUMN signid BOOLEAN")
                 # ALTER TABLE Users ADD COLUMN place TEXT
    
except:
    pass
def app_reg():
    global sign_up_scr, connect, cursor
   



    text_for_header = "Реєстрація Користувача"
    text_for_button = "Зберегти"

    fontr = m_font.font

    country_text = customtkinter.CTkLabel(
        master= sign_up_scr,
        width= 87,
        height= 31,
        fg_color= "#5DA7B1",
        bg_color= "#5DA7B1",
        text="Країна:",
        text_color="#FFFFFF",
        font=(fontr, 22)
    )
    city_text = customtkinter.CTkLabel(
        master= sign_up_scr,
        width= 87,
        height= 31,
        fg_color= "#5DA7B1",
        bg_color= "#5DA7B1",
        text="Місто:",
        text_color="#FFFFFF",
        font=(fontr, 22)
    )
    name_text = customtkinter.CTkLabel(
        master= sign_up_scr,
        width= 87,
        height= 31,
        fg_color= "#5DA7B1",
        bg_color= "#5DA7B1",
        text="Ім'я:",
        text_color="#FFFFFF",
        font=(fontr, 22)
    )
    lastname_text = customtkinter.CTkLabel(

        master= sign_up_scr,
        width= 121,
        height= 31,
        fg_color= "#5DA7B1",
        bg_color= "#5DA7B1",
        text="Призвіще:",
        text_color="#FFFFFF",
        font=(fontr, 22)
    )

    def commandbutton():
        try:
            cursor.execute("ALTER TABLE Signed ADD COLUMN country TEXT")    
        except:
            pass
        try:
            cursor.execute("ALTER TABLE Signed ADD COLUMN city TEXT")
        except:
            pass
        try:
            cursor.execute("ALTER TABLE Signed ADD COLUMN name TEXT")
        except:
            pass
        try:
            cursor.execute("ALTER TABLE Signed ADD COLUMN lastname TEXT")
        except:
            pass

        cursor.execute(f"INSERT INTO Signed (country, city, name, lastname, signid) VALUES (?, ?, ?, ?, ?)", (country_entry.get(), city_entry.get(), name_entry.get(), lastname_entry.get(), True))
        connect.commit()
        print(get_value(cursor),'execute')
        # 
        print(country_entry.get(), city_entry.get(), name_entry.get(), lastname_entry.get())
        sign_up_scr.destroy()
        import modules.cabinet as m_cab
        m_cab.cabinet_scr = customtkinter.CTk()
        m_cab.cabinet_scr.geometry("460x645")
        m_cab.cabinet_scr.config(bg="#5DA7B1")
        m_cab.cabinet_scr.resizable(False, False)
        m_cab.create_win_cabinka()
        m_cab.cabinet_scr.mainloop()
        


    # d = commandbutton
    # d()

    header_text = customtkinter.CTkLabel(
    master= sign_up_scr,
    width= 380,
    height= 55,
    fg_color= "#5DA7B1",
    bg_color= "#5DA7B1",
    text="Реєстрація користувача",
    text_color= "#FFFFFF",
    font=(fontr, 28)
    )

    button_save = customtkinter.CTkButton(
    master= sign_up_scr,
    width= 218,
    height=46,
    fg_color="#096C82",
    bg_color="#5DA7B1",
    border_width=3,
    border_color="#FFFFFF",
    text= "Зберегти",
    text_color="#FFFFFF",
    font=(fontr, 18),
    corner_radius=20,
    command=commandbutton
    )
    country_entry = customtkinter.CTkEntry(
        master= sign_up_scr,
        width= 218,
        height= 46,
        fg_color= "#096C82",
        bg_color="#5DA7B1",
        border_color= "#FFFFFF",
        border_width= 3,
        corner_radius= 20,
        font = (fontr, 22),
        text_color="#FFFFFF"
    )
    city_entry = customtkinter.CTkEntry(
        master= sign_up_scr,
        width= 218,
        height= 46,
        fg_color= "#096C82",
        bg_color="#5DA7B1",
        border_color= "#FFFFFF",
        border_width= 3,
        corner_radius= 20,
        font = (fontr, 22),
        text_color="#FFFFFF"
    )
    name_entry = customtkinter.CTkEntry(
        master= sign_up_scr,
        width= 295,
        height= 46,
        fg_color= "#096C82",
        bg_color="#5DA7B1",
        border_color= "#FFFFFF",
        border_width= 3,
        corner_radius= 20,
        font = (fontr, 22),
        text_color="#FFFFFF"
    )
    lastname_entry = customtkinter.CTkEntry(
        master= sign_up_scr,
        width= 295,
        height= 46,
        fg_color= "#096C82",
        bg_color="#5DA7B1",
        border_color= "#FFFFFF",
        border_width= 3,
        corner_radius= 20,
        font = (fontr, 22),
        text_color="#FFFFFF"
    )
    country_text.place(x=46,y=108)
    city_text.place(x=46,y=207)
    name_text.place(x=46,y=306)
    lastname_text.place(x=46,y=405)
    header_text.place(x=38, y=42)
    country_entry.place(x=38,y=150)
    city_entry.place(x=38,y=249)
    name_entry.place(x=38,y=348)
    lastname_entry.place(x=38,y=447)
    button_save.place(x=119, y=546)
    # connect.close()
print(get_value(cursor))
if bool(get_value(cursor, "Signed", "signid")) != True:
    app_reg()
else:
    import modules.cabinet as m_cab
    m_cab.cabinet_scr = customtkinter.CTk()
    m_cab.cabinet_scr.geometry("460x645")
    m_cab.cabinet_scr.config(bg="#5DA7B1")
    m_cab.cabinet_scr.resizable(False, False)
    m_cab.create_win_cabinka()
    m_cab.cabinet_scr.mainloop()