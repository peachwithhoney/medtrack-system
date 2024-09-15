import requests
from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
from werkzeug.security import check_password_hash
import auth_services
from db_operations import get_db_connection

class PacienteView:
    def __init__(self, window):
        self.window = window
        self.window.title("Medtrack")
        self.window.geometry("1366x768")
        self.window.resizable(0, 0)
        self.window.state('zoomed')
        self.window.config(background='#EAE9E8')
        
        # ============================Window Icon============================
        icon = PhotoImage(file='images/image_logo_1.png')
        self.window.iconphoto(True, icon)

        # ============================Header============================
        self.header = Frame(self.window, bg='#F4F4F4')
        self.header.place(x=300, y=0, width=1070, height=60)
        self.header_line = Canvas(self.window, width=1070, height=2, bg="#000000", highlightthickness=0)
        self.header_line.place(x=300, y=60)

        self.logout_text = Button(self.header, text="Logout", bg='#72E8D2', font=("", 13, "bold"), bd=0, fg='black',
                                  cursor='hand2', activebackground='#72E8D2')
        self.logout_text.place(x=950, y=15)


        # ==============================================================================
        # ================== SIDEBAR ===================================================
        # ==============================================================================
        self.sidebar = Frame(self.window, bg='#F4F4F4')
        self.sidebar.place(x=0, y=0, width=300, height=750)

        # =============================================================================
        # ============= BODY ==========================================================
        # =============================================================================
        self.heading = Label(self.window, text='Dashboard', font=("", 15, "bold"), fg='#0064d3', bg='#eff5f6')
        self.heading.place(x=325, y=70)

        # body frame 1
        self.bodyFrame1 = Frame(self.window, bg='#ffffff')
        self.bodyFrame1.place(x=328, y=110, width=1040, height=350)

        # body frame 2
        self.bodyFrame2 = Frame(self.window, bg='#009aa5')
        self.bodyFrame2.place(x=328, y=495, width=310, height=220)

        # body frame 3
        self.bodyFrame3 = Frame(self.window, bg='#e21f26')
        self.bodyFrame3.place(x=680, y=495, width=310, height=220)

        # body frame 4
        self.bodyFrame4 = Frame(self.window, bg='#ffcb1f')
        self.bodyFrame4.place(x=1030, y=495, width=310, height=220)

        # ==============================================================================
        # ================== SIDEBAR ===================================================
        # ==============================================================================

def page():
    window = Tk()
    PacienteView(window)
    window.mainloop()

if __name__ == "__main__":
    page()