import requests
from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox, ttk
from werkzeug.security import check_password_hash
import auth_services
from db_operations import get_db_connection
from feedbacks import contar_feedbacks
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from notification_operation import get_notifications
from pharmacy import get_medicamentos

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
        self.header_image_resized = self.header_image.resize((1366, 600), Image.LANCZOS) 
        photo = ImageTk.PhotoImage(self.header_image)
        self.header_image_label = Label(self.window, image=photo, bg='#F4F4F4')
        self.header_image_label.image = photo
        self.header_image_label.place(x=0, y=0, width=1366, height=80)

        self.header_line = Canvas(self.window, width=1366, height=1, bg="#000000", highlightthickness=0)
        self.header_line.place(x=0, y=82)

        # ============================Botão de Logout no Header============================
        self.lout_button_image = Image.open('images/button_logout.png')
        self.lout_button_resized = self.lout_button_image.resize((200, 170), Image.LANCZOS)
        logout_photo = ImageTk.PhotoImage(self.lout_button_resized)
        
        self.lout_button = Button(self.window, image=logout_photo, bg='#F4F4F4', bd=0, cursor='hand2', activebackground='#F4F4F4', command=self.logout)
        self.lout_button.image = logout_photo
        self.lout_button.place(x=1170, y=15, width=100, height=50)

        # ================== SIDEBAR ===================================================
        self.sidebar = Frame(self.window, bg='#F4F4F4')
        self.sidebar.place(x=0, y=85, width=300, height=750)

        # ============= BODY ==========================================================
        
         # body frame 1
        self.body_frame_1_label = Label(self.window, bg='#EDEDEB')
        self.body_frame_1_label.place(x=328, y=110, width=600, height=350)

        self.body_frame_1_image = Image.open('images/12.png')
        self.body_frame_1_resized = self.body_frame_1_image.resize((600, 350), Image.LANCZOS) 
        self.body_frame_1_photo = ImageTk.PhotoImage(self.body_frame_1_resized)
        self.body_frame_1_label.config(image=self.body_frame_1_photo)
        self.body_frame_1_label.image = self.body_frame_1_photo

        # Adicionar o gráfico de estoque no Label
        self.create_estoque_chart()

        # body frame 2
        self.body_frame_2_image = Image.open('images/19.png')
        self.body_frame_2_resized = self.body_frame_2_image.resize((1180, 780), Image.LANCZOS)  
        self.body_frame_2_photo = ImageTk.PhotoImage(self.body_frame_2_resized)
        self.body_frame_2_label = Label(self.window, image=self.body_frame_2_photo, bg='#EDEDEB')
        self.body_frame_2_label.image = self.body_frame_2_photo
        self.body_frame_2_label.place(x=1000, y=110, width=310, height=600)


        # Adicionar a estatística de feedbacks no body_frame_2
        self.feedbacks_label = Label(self.body_frame_2_label, text="", bg='#EDEDEB', font=("yu gothic ui", 16, "bold"))
        self.feedbacks_label.pack(pady=20)
        
        self.atualizar_feedbacks()
        
        # body frame 3
        self.body_frame_3_image = Image.open('images/20.png')
        self.body_frame_3_resized = self.body_frame_3_image.resize((1280, 1300), Image.LANCZOS) 
        self.body_frame_3_photo = ImageTk.PhotoImage(self.body_frame_3_resized)
        self.body_frame_3_label = Label(self.window, image=self.body_frame_3_photo, bg='#EAE9E8')
        self.body_frame_3_label.image = self.body_frame_3_photo
        self.body_frame_3_label.place(x=328, y=495, width=600, height=220)

        self.body_layout_3 = Frame(self.window, bg='#EAE9E8')
        self.body_layout_3.place(x=328, y=495, width=600, height=220)

        self.notification_tree = ttk.Treeview(self.body_layout_3, columns=("Autor", "Mensagem"), show='headings')
        self.notification_tree.heading("Autor", text="Autor")
        self.notification_tree.heading("Mensagem", text="Mensagem")
        self.notification_tree.pack(fill="both", expand=True)

        self.update_notifications()

        # =====================================SideBar=========================================

        # Dashboard
        self.dashboard_Image = Image.open('images/Dashboard_Icon.png')
        self.dashboard_Image_resized = self.dashboard_Image.resize((50, 50), Image.LANCZOS) 
        self.dashboard_Image_photo = ImageTk.PhotoImage(self.dashboard_Image_resized)
        self.dashboard = Label(self.sidebar, image=self.dashboard_Image_photo, bg='#F4F4F4')
        self.dashboard.image = self.dashboard_Image_photo  
        self.dashboard.place(x=70, y=20)

        self.dashboard_text = Button(self.sidebar, text="Dashboard", bg='#F4F4F4', font=("yu gothic ui", 17, "bold"), fg='#FF914D', bd=0,
                             cursor='hand2', activebackground='#F4F4F4', command=self.open_dashboard)
        self.dashboard_text.place(x=110, y=20)

        # Pacientes
        self.Paciente_Image = Image.open('images/Icon_Dashboard_Button.png')
        self.Paciente_Image_resized = self.Paciente_Image.resize((50, 50), Image.LANCZOS) 
        self.Paciente_Image_photo = ImageTk.PhotoImage(self.Paciente_Image_resized)
        self.Paciente = Label(self.sidebar, image=self.Paciente_Image_photo, bg='#F4F4F4')
        self.Paciente.image = self.Paciente_Image_photo  
        self.Paciente.place(x=40, y=55)

        self.Paciente_text = Button(self.sidebar, text="Paciente", bg='#F4F4F4', font=("yu gothic ui", 17, "bold"), bd=0,
                             cursor='hand2', activebackground='#F4F4F4', command=self.open_pacient)
        self.Paciente_text.place(x=80, y=60)
        
        # Consultas
        self.Consultas_Image = Image.open('images/Icon_Dashboard_Button.png')
        self.Consultas_Image_resized = self.Consultas_Image.resize((50, 50), Image.LANCZOS) 
        self.Consultas_Image_photo = ImageTk.PhotoImage(self.Consultas_Image_resized)
        self.Consultas = Label(self.sidebar, image=self.Consultas_Image_photo, bg='#F4F4F4')
        self.Consultas.image = self.Consultas_Image_photo  
        self.Consultas.place(x=40, y=95)

        self.Consultas_text = Button(self.sidebar, text="Consultas", bg='#F4F4F4', font=("yu gothic ui", 17, "bold"), bd=0,
                             cursor='hand2', activebackground='#F4F4F4')
        self.Consultas_text.place(x=80, y=100)
        
        # Médicos
        self.Medicos_Image = Image.open('images/Icon_Dashboard_Button.png')
        self.Medicos_Image_resized = self.Medicos_Image.resize((50, 50), Image.LANCZOS) 
        self.Medicos_Image_photo = ImageTk.PhotoImage(self.Medicos_Image_resized)
        self.Medicos = Label(self.sidebar, image=self.Medicos_Image_photo, bg='#F4F4F4')
        self.Medicos.image = self.Medicos_Image_photo  
        self.Medicos.place(x=40, y=135)

        self.Medicos_text = Button(self.sidebar, text="Médicos", bg='#F4F4F4', font=("yu gothic ui", 17, "bold"), bd=0,
                             cursor='hand2', activebackground='#F4F4F4')
        self.Medicos_text.place(x=80, y=140)
        
        # Exames
        self.Exames_Image = Image.open('images/Icon_Dashboard_Button.png')
        self.Exames_Image_resized = self.Exames_Image.resize((50, 50), Image.LANCZOS) 
        self.Exames_Image_photo = ImageTk.PhotoImage(self.Exames_Image_resized)
        self.Exames = Label(self.sidebar, image=self.Exames_Image_photo, bg='#F4F4F4')
        self.Exames.image = self.Exames_Image_photo  
        self.Exames.place(x=40, y=175)

        self.Exames_text = Button(self.sidebar, text="Exames", bg='#F4F4F4', font=("yu gothic ui", 17, "bold"), bd=0,
                             cursor='hand2', activebackground='#F4F4F4')
        self.Exames_text.place(x=80, y=180)
        
        # Tratamentos
        self.Tratamentos_Image = Image.open('images/Icon_Dashboard_Button.png')
        self.Tratamentos_Image_resized = self.Tratamentos_Image.resize((50, 50), Image.LANCZOS) 
        self.Tratamentos_Image_photo = ImageTk.PhotoImage(self.Tratamentos_Image_resized)
        self.Tratamentos = Label(self.sidebar, image=self.Tratamentos_Image_photo, bg='#F4F4F4')
        self.Tratamentos.image = self.Tratamentos_Image_photo  
        self.Tratamentos.place(x=40, y=215)

        self.Tratamentos_text = Button(self.sidebar, text="Tratamentos", bg='#F4F4F4', font=("yu gothic ui", 17, "bold"), bd=0,
                             cursor='hand2', activebackground='#F4F4F4')
        self.Tratamentos_text.place(x=80, y=220)
        
        # Cirurgias
        self.Cirurgias_Image = Image.open('images/Icon_Dashboard_Button.png')
        self.Cirurgias_Image_resized = self.Cirurgias_Image.resize((50, 50), Image.LANCZOS) 
        self.Cirurgias_Image_photo = ImageTk.PhotoImage(self.Cirurgias_Image_resized)
        self.Cirurgias = Label(self.sidebar, image=self.Cirurgias_Image_photo, bg='#F4F4F4')
        self.Cirurgias.image = self.Cirurgias_Image_photo  
        self.Cirurgias.place(x=40, y=255)

        self.Cirurgias_text = Button(self.sidebar, text="Cirurgias", bg='#F4F4F4', font=("yu gothic ui", 17, "bold"), bd=0,
                             cursor='hand2', activebackground='#F4F4F4')
        self.Cirurgias_text.place(x=80, y=260)
        
        # Farmácia
        self.Farmacia_Image = Image.open('images/Icon_Dashboard_Button.png')
        self.Farmacia_Image_resized = self.Farmacia_Image.resize((50, 50), Image.LANCZOS) 
        self.Farmacia_Image_photo = ImageTk.PhotoImage(self.Farmacia_Image_resized)
        self.Farmacia = Label(self.sidebar, image=self.Farmacia_Image_photo, bg='#F4F4F4')
        self.Farmacia.image = self.Farmacia_Image_photo  
        self.Farmacia.place(x=40, y=295)

        self.Farmacia_text = Button(self.sidebar, text="Farmacia", bg='#F4F4F4', font=("yu gothic ui", 17, "bold"), bd=0,
                             cursor='hand2', activebackground='#F4F4F4')
        self.Farmacia_text.place(x=80, y=300)        

    def create_estoque_chart(self):
        
        medicamentos = get_medicamentos()

        
        if medicamentos is None or len(medicamentos) == 0:
            print("Nenhum medicamento encontrado ou erro na consulta.")
            return

       
        names = [med["nome"] for med in medicamentos]
        quantities = [med["estoque"] for med in medicamentos]
        colors = ['#BC1823' if qtd < 10 else '#BA4345' if qtd < 20 else '#72A2C0' for qtd in quantities]

        
        fig, ax = plt.subplots()
        ax.bar(names, quantities, color=colors)
        ax.set_title('Estoque de Medicamentos')
        ax.set_xlabel('Medicamentos')
        ax.set_ylabel('Quantidade em Estoque')
        plt.xticks(rotation=45, ha='right')

        if not hasattr(self, 'body_frame_1_label') or self.body_frame_1_label is None:
            print("Frame 'body_frame_1_label' não encontrado ou não configurado.")
            return

        canvas = FigureCanvasTkAgg(fig, master=self.body_frame_1_label)
        canvas.draw()
        canvas.get_tk_widget().pack(fill='both', expand=True)

        
        self.body_frame_1_label.update_idletasks()


    def obter_estatistica_feedbacks(self):
        return contar_feedbacks()

    def atualizar_feedbacks(self):
        categorias = ['Positivos', 'Negativos', 'Neutros']
        valores = [10, 5, 2]  
    
        fig, ax = plt.subplots(figsize=(5, 5), subplot_kw=dict(aspect="equal"))
        fig.patch.set_facecolor('#EDEDEB')
        ax.set_facecolor('#EDEDEB')
        
        wedges, texts, autotexts = ax.pie(valores, labels=categorias, autopct='%1.1f%%', startangle=140, colors=['#FF914D', '#FFBD59', '#72E8D2'])
        ax.set_title('Distribuição de Feedbacks')
    
        for text in texts:
            text.set_color('black')
        for autotext in autotexts:
            autotext.set_color('black')
    
        canvas = FigureCanvasTkAgg(fig, master=self.body_frame_2_label)
        canvas.draw()
        canvas.get_tk_widget().pack(pady=20)

    def update_notifications(self):
        
        notifications = get_notifications() 
        
        self.notification_tree = ttk.Treeview(self.body_layout_3, columns=("autor", "mensagem", "data_hora"), show='headings')
        self.notification_tree.heading("autor", text="Autor")
        self.notification_tree.heading("mensagem", text="Mensagem")
        self.notification_tree.heading("data_hora", text="Data/Hora")
        
        for notification in notifications:
            autor = notification['medico_nome'] if notification['medico_nome'] else notification['paciente_nome'] 
            mensagem = notification['mensagem']
            data_hora = notification['data_hora']
            self.notification_tree.insert("", "end", values=(autor, mensagem, data_hora))
        
        self.notification_tree.pack(expand=True, fill='both', padx=10, pady=10)

    def logout(self):
        messagebox.showinfo("Logout", "Você saiu com sucesso!")
        self.window.destroy()
    
        from LoginView import LoginForm  
        login_window = Tk()
        LoginForm(login_window)
        login_window.mainloop()

    def open_dashboard(self):
        self.window.destroy()
        Dashboard()

    def open_pacient(self):
        self.window.destroy()
    
        from PacientView import PacienteView
        pacient_window = Tk()  
        PacienteView(pacient_window)
        pacient_window.mainloop()

    

def page():
    window = Tk()
    Dashboard(window)
    window.mainloop()

if __name__ == "__main__":
    page()
