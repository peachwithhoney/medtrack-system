import requests
from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
from werkzeug.security import check_password_hash
import auth_services
from db_operations import get_db_connection

class MedicoView:
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
        self.header_image = Image.open('images/headbar_medicos.png')
        self.header_image_resized = self.header_image.resize((1280, 600), Image.LANCZOS) 
        photo = ImageTk.PhotoImage(self.header_image)
        self.header_image_label = Label(self.window, image=photo, bg='#F4F4F4')
        self.header_image_label.image = photo
        self.header_image_label.place(x=0, y=0, width=1366, height=80)

        self.header_line = Canvas(self.window, width=1066, height=1, bg="#000000", highlightthickness=0)
        self.header_line.place(x=300, y=82)

        # ============================Botão de Logout no Header============================
        self.lout_button_image = Image.open('images/Botao_logout.png')
        logout_photo = ImageTk.PhotoImage(self.lout_button_image)

        
        self.lout_button = Button(self.window, image=logout_photo, bg='#EAE9E8', bd=0, cursor='hand2', activebackground='#F4F4F4', command=self.logout)
        self.lout_button.image = logout_photo
        self.lout_button.place(x=1170, y=15)

        # ================== SIDEBAR ===================================================
        self.sidebar = Frame(self.window, bg='#F4F4F4')
        self.sidebar.place(x=0, y=80, width=300, height=750)

        # ============= BODY ==========================================================
        
        # body frame 1
        self.body_frame_1_image = Image.open('images/12.png')
        self.body_frame_1_resized = self.body_frame_1_image.resize((1280, 600), Image.LANCZOS) 
        self.body_frame_1_photo = ImageTk.PhotoImage(self.body_frame_1_resized)
        self.body_frame_1_label = Label(self.window, image=self.body_frame_1_photo, bg='#EAE9E8')
        self.body_frame_1_label.image = self.body_frame_1_photo
        self.body_frame_1_label.place(x=328, y=110, width=600, height=350)

        # body frame 2
        self.body_frame_2_image = Image.open('images/19.png')
        self.body_frame_2_resized = self.body_frame_2_image.resize((1180, 780), Image.LANCZOS)  
        self.body_frame_2_photo = ImageTk.PhotoImage(self.body_frame_2_resized)
        self.body_frame_2_label = Label(self.window, image=self.body_frame_2_photo, bg='#EAE9E8')
        self.body_frame_2_label.image = self.body_frame_2_photo
        self.body_frame_2_label.place(x=1000, y=110, width=310, height=600)

        # body frame 3
        self.body_frame_3_image = Image.open('images/20.png')
        self.body_frame_3_resized = self.body_frame_3_image.resize((1280, 1300), Image.LANCZOS) 
        self.body_frame_3_photo = ImageTk.PhotoImage(self.body_frame_3_resized)
        self.body_frame_3_label = Label(self.window, image=self.body_frame_3_photo, bg='#EAE9E8')
        self.body_frame_3_label.image = self.body_frame_3_photo
        self.body_frame_3_label.place(x=328, y=495, width=600, height=220)

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
    MedicoView(window)
    window.mainloop()

if __name__ == "__main__":
    page()