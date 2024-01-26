import modules.sign_up as m_sign_up
# import modules.main_window as m_win
from PIL import Image
import os

# m_sign_up.sign_up_scr.iconphoto('2.ico')

m_sign_up.sign_up_scr.iconbitmap(os.path.abspath(__file__ + "/../2.ico"))
# m_win.main_scr.mainloop()
m_sign_up.sign_up_scr.mainloop()
m_sign_up.connect.commit()
m_sign_up.connect.close()