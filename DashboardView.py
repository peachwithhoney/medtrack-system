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
        self.dashboard_Image = Image.open('images/Dashboard_Icon.png')
        self.dashboard_Image_resized = self.dashboard_Image.resize((50, 50), Image.LANCZOS) 
        self.dashboard_Image_photo = ImageTk.PhotoImage(self.dashboard_Image_resized)
        self.dashboard = Label(self.sidebar, image=self.dashboard_Image_photo, bg='#F4F4F4')
        self.dashboard.image = self.dashboard_Image_photo  
        self.dashboard.place(x=40, y=15)

        self.dashboard_text = Button(self.sidebar, text="Dashboard", bg='#F4F4F4', font=("", 17, "bold"), bd=0,
                             cursor='hand2', activebackground='#F4F4F4')
        self.dashboard_text.place(x=80, y=20)

        # Pacientes
        self.Paciente_Image = Image.open('images/Icon_Dashboard_Button.png')
        self.Paciente_Image_resized = self.Paciente_Image.resize((50, 50), Image.LANCZOS) 
        self.Paciente_Image_photo = ImageTk.PhotoImage(self.Paciente_Image_resized)
        self.Paciente = Label(self.sidebar, image=self.Paciente_Image_photo, bg='#F4F4F4')
        self.Paciente.image = self.Paciente_Image_photo  
        self.Paciente.place(x=40, y=15)

        self.Paciente_text = Button(self.sidebar, text="Paciente", bg='#F4F4F4', font=("", 17, "bold"), bd=0,
                             cursor='hand2', activebackground='#F4F4F4')
        self.Paciente_text.place(x=80, y=20)
        
        # Consultas
        self.Consultas_Image = Image.open('images/Icon_Dashboard_Button.png')
        self.Consultas_Image_resized = self.Consultas_Image.resize((50, 50), Image.LANCZOS) 
        self.Consultas_Image_photo = ImageTk.PhotoImage(self.Consultas_Image_resized)
        self.Consultas = Label(self.sidebar, image=self.Consultas_Image_photo, bg='#F4F4F4')
        self.Consultas.image = self.Consultas_Image_photo  
        self.Consultas.place(x=40, y=15)

        self.Consultas_text = Button(self.sidebar, text="Consultas", bg='#F4F4F4', font=("", 17, "bold"), bd=0,
                             cursor='hand2', activebackground='#F4F4F4')
        self.Consultas_text.place(x=80, y=20)
        
        # Médicos
        self.Medicos_Image = Image.open('images/Icon_Dashboard_Button.png')
        self.Medicos_Image_resized = self.Medicos_Image.resize((50, 50), Image.LANCZOS) 
        self.Medicos_Image_photo = ImageTk.PhotoImage(self.Medicos_Image_resized)
        self.Medicos = Label(self.sidebar, image=self.Medicos_Image_photo, bg='#F4F4F4')
        self.Medicos.image = self.Medicos_Image_photo  
        self.Medicos.place(x=40, y=15)

        self.Medicos_text = Button(self.sidebar, text="Médicos", bg='#F4F4F4', font=("", 17, "bold"), bd=0,
                             cursor='hand2', activebackground='#F4F4F4')
        self.Medicos_text.place(x=80, y=20)
        
        # Exames
        self.Exames_Image = Image.open('images/Icon_Dashboard_Button.png')
        self.Exames_Image_resized = self.Exames_Image.resize((50, 50), Image.LANCZOS) 
        self.Exames_Image_photo = ImageTk.PhotoImage(self.Exames_Image_resized)
        self.Exames = Label(self.sidebar, image=self.Exames_Image_photo, bg='#F4F4F4')
        self.Exames.image = self.Exames_Image_photo  
        self.Exames.place(x=40, y=15)

        self.Exames_text = Button(self.sidebar, text="Exames", bg='#F4F4F4', font=("", 17, "bold"), bd=0,
                             cursor='hand2', activebackground='#F4F4F4')
        self.Exames_text.place(x=80, y=20)
        
        # Tratamentos
        self.Tratamentos_Image = Image.open('images/Icon_Dashboard_Button.png')
        self.Tratamentos_Image_resized = self.Tratamentos_Image.resize((50, 50), Image.LANCZOS) 
        self.Tratamentos_Image_photo = ImageTk.PhotoImage(self.Tratamentos_Image_resized)
        self.Tratamentos = Label(self.sidebar, image=self.Tratamentos_Image_photo, bg='#F4F4F4')
        self.Tratamentos.image = self.Tratamentos_Image_photo  
        self.Tratamentos.place(x=40, y=15)

        self.Tratamentos_text = Button(self.sidebar, text="Tratamentos", bg='#F4F4F4', font=("", 17, "bold"), bd=0,
                             cursor='hand2', activebackground='#F4F4F4')
        self.Tratamentos_text.place(x=80, y=20)
        
        # Cirurgias
        self.Cirurgias_Image = Image.open('images/Icon_Dashboard_Button.png')
        self.Cirurgias_Image_resized = self.Cirurgias_Image.resize((50, 50), Image.LANCZOS) 
        self.Cirurgias_Image_photo = ImageTk.PhotoImage(self.Cirurgias_Image_resized)
        self.Cirurgias = Label(self.sidebar, image=self.Cirurgias_Image_photo, bg='#F4F4F4')
        self.Cirurgias.image = self.Cirurgias_Image_photo  
        self.Cirurgias.place(x=40, y=15)

        self.Cirurgias_text = Button(self.sidebar, text="Cirurgias", bg='#F4F4F4', font=("", 17, "bold"), bd=0,
                             cursor='hand2', activebackground='#F4F4F4')
        self.Cirurgias_text.place(x=80, y=20)
        
        # Farmácia
        self.Farmacia_Image = Image.open('images/Icon_Dashboard_Button.png')
        self.Farmacia_Image_resized = self.Farmacia_Image.resize((50, 50), Image.LANCZOS) 
        self.Farmacia_Image_photo = ImageTk.PhotoImage(self.Farmacia_Image_resized)
        self.Farmacia = Label(self.sidebar, image=self.Farmacia_Image_photo, bg='#F4F4F4')
        self.Farmacia.image = self.Farmacia_Image_photo  
        self.Farmacia.place(x=40, y=15)

        self.Farmacia_text = Button(self.sidebar, text="Farmacia", bg='#F4F4F4', font=("", 17, "bold"), bd=0,
                             cursor='hand2', activebackground='#F4F4F4')
        self.Farmacia_text.place(x=80, y=20)        

    
    def logout(self):
        messagebox.showinfo("Logout", "Você saiu com sucesso!")
        self.window.destroy()  

def page():
    window = Tk()
    Dashboard(window)
    window.mainloop()

if __name__ == "__main__":
    page()
