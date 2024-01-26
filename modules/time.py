import customtkinter, time

def crttm(text1):
    import modules.main_window as m_main
    # time.struct_time(tm_year=2023, tm_mon=12, tm_mday=29, tm_hour=22, tm_min=3, tm_sec=16, tm_wday=4, tm_yday=363, tm_isdst=0)
    timed = customtkinter.CTkLabel(
        master= m_main.main_scr,
        text = text1,
        height = 31,
        font = ("Roboto Slab Bold", 18),
        bg_color="#5DA7B1",
        fg_color="#5DA7B1",
        text_color = "#FFFFFF"
    )
    return timed