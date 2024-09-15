import requests
from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
from werkzeug.security import check_password_hash
import auth_services
from db_operations import get_db_connection

class Dashboard:
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
        self.header_image = Image.open('images/10.png')
        photo = ImageTk.PhotoImage(self.header_image)
        
        
        self.header_image_label = Label(self.window, image=photo, bg='#F4F4F4')
        self.header_image_label.image = photo
        self.header_image_label.place(x=300, y=0, width=1070, height=60)

        self.header_line = Canvas(self.window, width=1070, height=1, bg="#000000", highlightthickness=0)
        self.header_line.place(x=300, y=60)

        # ============================Botão de Logout no Header============================
        self.lout_button_image = Image.open('images/Botao_logout.png')
        logout_photo = ImageTk.PhotoImage(self.lout_button_image)

        
        self.lout_button = Button(self.window, image=logout_photo, bg='#EAE9E8', bd=0, cursor='hand2', activebackground='#F4F4F4', command=self.logout)
        self.lout_button.image = logout_photo
        self.lout_button.place(x=1170, y=15)

        # ================== SIDEBAR ===================================================
        self.sidebar = Frame(self.window, bg='#F4F4F4')
        self.sidebar.place(x=0, y=0, width=300, height=750)

        # ============= BODY ==========================================================
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

        # =====================================SideBar=========================================

        # Dashboard
        self.dashboardImage = ImageTk.PhotoImage(file='images/17.png')
        self.dashboard = Label(self.sidebar, image=self.dashboardImage, bg='#F4F4F4')
        self.dashboard.place(x=35, y=289)

        self.dashboard_text = Button(self.sidebar, text="Dashboard", bg='#F4F4F4', font=("", 13, "bold"), bd=0,
                                     cursor='hand2', activebackground='#F4F4F4')
        self.dashboard_text.place(x=80, y=287)

    
    def logout(self):
        messagebox.showinfo("Logout", "Você saiu com sucesso!")
        self.window.destroy()  

def page():
    window = Tk()
    Dashboard(window)
    window.mainloop()

if __name__ == "__main__":
    page()
