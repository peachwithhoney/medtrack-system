from tkinter import *
from tkinter import ttk, simpledialog, messagebox
from PIL import ImageTk, Image
from tkinter import messagebox
from notification_operation import get_notifications
import tkinter as tk
from PatientManager import PacienteManager


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
        self.header_image = Image.open('images/headbar_pacientes.png')
        self.header_image_resized = self.header_image.resize((1366, 600), Image.LANCZOS) 
        photo = ImageTk.PhotoImage(self.header_image)
        self.header_image_label = Label(self.window, image=photo, bg='#F4F4F4')
        self.header_image_label.image = photo
        self.header_image_label.place(x=0, y=0, width=2366, height=80)

        self.header_line = Canvas(self.window, width=2600, height=1, bg="#000000", highlightthickness=0)
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
        self.sidebar.place(x=0, y=85, width=300, height=1000)

        # ============= BODY ==========================================================
        
        # body frame 1
        self.body_frame_1_label = Label(self.window, bg='#EAE9E8')
        self.body_frame_1_label.place(x=328, y=110, width=1000, height=350)

        self.add_button = Button(self.window, text="Adicionar Paciente", command=self.add_paciente, font=("Arial", 12), bg="#4CAF50", fg="white")
        self.add_button.place(x=330, y=470, width=150, height=40)
        
        self.del_button = Button(self.window, text="Excluir Paciente", command=self.del_paciente, font=("Arial", 12), bg="#FF6347", fg="white")
        self.del_button.place(x=500, y=470, width=150, height=40)

        # Pacientes Cadastrados

        self.display_paciente()

        # =====================================SideBar=========================================

        # Dashboard
        self.dashboard_Image = Image.open('images/Dashboard_Icon.png')
        self.dashboard_Image_resized = self.dashboard_Image.resize((50, 50), Image.LANCZOS) 
        self.dashboard_Image_photo = ImageTk.PhotoImage(self.dashboard_Image_resized)
        self.dashboard = Label(self.sidebar, image=self.dashboard_Image_photo, bg='#F4F4F4')
        self.dashboard.image = self.dashboard_Image_photo  
        self.dashboard.place(x=40, y=15)

        self.dashboard_text = Button(self.sidebar, text="Dashboard", bg='#F4F4F4', font=("yu gothic ui", 17, "bold"), bd=0,
                             cursor='hand2', activebackground='#F4F4F4', command=self.open_dashboard)
        self.dashboard_text.place(x=80, y=20)

        # Pacientes
        self.Paciente_Image = Image.open('images/Icon_Dashboard_Button.png')
        self.Paciente_Image_resized = self.Paciente_Image.resize((50, 50), Image.LANCZOS) 
        self.Paciente_Image_photo = ImageTk.PhotoImage(self.Paciente_Image_resized)
        self.Paciente = Label(self.sidebar, image=self.Paciente_Image_photo, bg='#F4F4F4')
        self.Paciente.image = self.Paciente_Image_photo  
        self.Paciente.place(x=70, y=55)

        self.Paciente_text = Button(self.sidebar, text="Paciente", bg='#F4F4F4', font=("yu gothic ui", 17, "bold"), bd=0, fg='#FF914D',
                             cursor='hand2', activebackground='#F4F4F4')
        self.Paciente_text.place(x=110, y=60)
        
        # Consultas
        self.Consultas_Image = Image.open('images/Icon_Dashboard_Button.png')
        self.Consultas_Image_resized = self.Consultas_Image.resize((50, 50), Image.LANCZOS) 
        self.Consultas_Image_photo = ImageTk.PhotoImage(self.Consultas_Image_resized)
        self.Consultas = Label(self.sidebar, image=self.Consultas_Image_photo, bg='#F4F4F4')
        self.Consultas.image = self.Consultas_Image_photo  
        self.Consultas.place(x=40, y=95)

        self.Consultas_text = Button(self.sidebar, text="Consultas", bg='#F4F4F4', font=("yu gothic ui", 17, "bold"), bd=0,
                             cursor='hand2', activebackground='#F4F4F4', command=self.open_consulta)
        self.Consultas_text.place(x=80, y=100)
        
        # Médicos
        self.Medicos_Image = Image.open('images/Icon_Dashboard_Button.png')
        self.Medicos_Image_resized = self.Medicos_Image.resize((50, 50), Image.LANCZOS) 
        self.Medicos_Image_photo = ImageTk.PhotoImage(self.Medicos_Image_resized)
        self.Medicos = Label(self.sidebar, image=self.Medicos_Image_photo, bg='#F4F4F4')
        self.Medicos.image = self.Medicos_Image_photo  
        self.Medicos.place(x=40, y=135)

        self.Medicos_text = Button(self.sidebar, text="Médicos", bg='#F4F4F4', font=("yu gothic ui", 17, "bold"), bd=0,
                             cursor='hand2', activebackground='#F4F4F4', command=self.open_medicos)
        self.Medicos_text.place(x=80, y=140)
        
        # Exames
        self.Exames_Image = Image.open('images/Icon_Dashboard_Button.png')
        self.Exames_Image_resized = self.Exames_Image.resize((50, 50), Image.LANCZOS) 
        self.Exames_Image_photo = ImageTk.PhotoImage(self.Exames_Image_resized)
        self.Exames = Label(self.sidebar, image=self.Exames_Image_photo, bg='#F4F4F4')
        self.Exames.image = self.Exames_Image_photo  
        self.Exames.place(x=40, y=175)

        self.Exames_text = Button(self.sidebar, text="Exames", bg='#F4F4F4', font=("yu gothic ui", 17, "bold"), bd=0,
                             cursor='hand2', activebackground='#F4F4F4', command=self.open_exame)
        self.Exames_text.place(x=80, y=180)
        
        # Tratamentos
        self.Tratamentos_Image = Image.open('images/Icon_Dashboard_Button.png')
        self.Tratamentos_Image_resized = self.Tratamentos_Image.resize((50, 50), Image.LANCZOS) 
        self.Tratamentos_Image_photo = ImageTk.PhotoImage(self.Tratamentos_Image_resized)
        self.Tratamentos = Label(self.sidebar, image=self.Tratamentos_Image_photo, bg='#F4F4F4')
        self.Tratamentos.image = self.Tratamentos_Image_photo  
        self.Tratamentos.place(x=40, y=215)

        self.Tratamentos_text = Button(self.sidebar, text="Tratamentos", bg='#F4F4F4', font=("yu gothic ui", 17, "bold"), bd=0,
                             cursor='hand2', activebackground='#F4F4F4', command=self.open_tratamento)
        self.Tratamentos_text.place(x=80, y=220)
        
        # Cirurgias
        self.Cirurgias_Image = Image.open('images/Icon_Dashboard_Button.png')
        self.Cirurgias_Image_resized = self.Cirurgias_Image.resize((50, 50), Image.LANCZOS) 
        self.Cirurgias_Image_photo = ImageTk.PhotoImage(self.Cirurgias_Image_resized)
        self.Cirurgias = Label(self.sidebar, image=self.Cirurgias_Image_photo, bg='#F4F4F4')
        self.Cirurgias.image = self.Cirurgias_Image_photo  
        self.Cirurgias.place(x=40, y=255)

        self.Cirurgias_text = Button(self.sidebar, text="Cirurgias", bg='#F4F4F4', font=("yu gothic ui", 17, "bold"), bd=0,
                             cursor='hand2', activebackground='#F4F4F4', command=self.open_cirurgia)
        self.Cirurgias_text.place(x=80, y=260)
        
        # Farmácia
        self.Farmacia_Image = Image.open('images/Icon_Dashboard_Button.png')
        self.Farmacia_Image_resized = self.Farmacia_Image.resize((50, 50), Image.LANCZOS) 
        self.Farmacia_Image_photo = ImageTk.PhotoImage(self.Farmacia_Image_resized)
        self.Farmacia = Label(self.sidebar, image=self.Farmacia_Image_photo, bg='#F4F4F4')
        self.Farmacia.image = self.Farmacia_Image_photo  
        self.Farmacia.place(x=40, y=295)

        self.Farmacia_text = Button(self.sidebar, text="Farmacia", bg='#F4F4F4', font=("yu gothic ui", 17, "bold"), bd=0,
                             cursor='hand2', activebackground='#F4F4F4', command=self.open_medicamento)
        self.Farmacia_text.place(x=80, y=300)          

    
    def logout(self):
        messagebox.showinfo("Logout", "Você saiu com sucesso!")
        self.window.destroy()
    
        from LoginView import LoginForm  
        login_window = Tk()
        LoginForm(login_window)
        login_window.mainloop()

    def update_notifications(self):
        notifications = get_notifications()

        if not notifications:
            no_data_label = Label(self.notifications_frame, text="Nenhuma notificação disponível.", bg='#F4F4F4', font=("yu gothic ui", 14))
            no_data_label.pack(pady=20)
            return

        for notification in notifications:
            notification_text = f"Paciente: {notification['paciente_nome']}\n" \
                                f"Mensagem: {notification['mensagem']}\n" \
                                f"Data: {notification['data_hora']}\n" \
                                

            notification_label = Label(self.notifications_frame, text=notification_text, bg='#F4F4F4', font=("yu gothic ui", 12), anchor='w', padx=8, pady=5)
            notification_label.pack(fill=X, padx=8, pady=4)

    def display_paciente(self):
        if hasattr(self, 'paciente_table'):
            self.paciente_table.destroy()

        pacientes = PacienteManager.get_all_pacientes()
        if not pacientes:
            messagebox.showinfo("Informação", "Nenhum paciente encontrado no sistema.")
            return

        columns = ('id', 'nome', 'data_nascimento', 'cpf', 'endereco', 'telefone', 'email')
        self.paciente_table = ttk.Treeview(self.body_frame_1_label, columns=columns, show='headings')
        self.paciente_table.heading('id', text='ID')
        self.paciente_table.heading('nome', text='Nome')
        self.paciente_table.heading('data_nascimento', text='Data Nascimento')
        self.paciente_table.heading('cpf', text='CPF')
        self.paciente_table.heading('endereco', text='Endereco')
        self.paciente_table.heading('telefone', text='Telefone')
        self.paciente_table.heading('email', text='Email')
        self.paciente_table.place(x=20, y=20, width=800, height=300)

        for paciente in pacientes:
            values = (
                paciente.get('id', ''),
                paciente.get('nome', ''),
                paciente.get('data_nascimento', ''),
                paciente.get('cpf', ''),
                paciente.get('endereco', ''),
                paciente.get('telefone', ''),
                paciente.get('email', '')
                )
            self.paciente_table.insert('', 'end', values=values)


    def add_paciente(self):
        add_window = Toplevel(self.window)
        add_window.title("Adicionar Paciente")
        add_window.geometry("400x300")
        add_window.config(background='#EAE9E8')

        Label(add_window, text="Nome", bg='#EAE9E8').place(x=20, y=20)
        nome_entry = Entry(add_window)
        nome_entry.place(x=150, y=20)

        Label(add_window, text="Data de Nascimento", bg='#EAE9E8').place(x=20, y=60)
        data_nascimento_entry = Entry(add_window)
        data_nascimento_entry.place(x=150, y=60)

        Label(add_window, text="CPF", bg='#EAE9E8').place(x=20, y=100)
        cpf_entry = Entry(add_window)
        cpf_entry.place(x=150, y=100)

        Label(add_window, text="Endereço", bg='#EAE9E8').place(x=20, y=140)
        endereco_entry = Entry(add_window)
        endereco_entry.place(x=150, y=140)

        Label(add_window, text="Telefone", bg='#EAE9E8').place(x=20, y=180)
        telefone_entry = Entry(add_window)
        telefone_entry.place(x=150, y=180)

        Label(add_window, text="Email", bg='#EAE9E8').place(x=20, y=220)
        email_entry = Entry(add_window)
        email_entry.place(x=150, y=220)


        def submit_paciente():
            nome = nome_entry.get()
            data_nascimento = data_nascimento_entry.get()
            cpf = cpf_entry.get()
            endereco = endereco_entry.get()
            telefone = telefone_entry.get()
            email = email_entry.get()

            if not nome or not data_nascimento or not cpf or not endereco or not telefone or not email:
                messagebox.showerror("Erro", "Preencha todos os campos.")
            else:
                try:
                    PacienteManager.create_paciente(
                        nome=nome, 
                        data_nascimento=data_nascimento, 
                        cpf=cpf, 
                        endereco=endereco,
                        telefone=telefone,
                        email=email
                    )
                    messagebox.showinfo("Paciente", "Paciente cadastrado com sucesso!")
                    add_window.destroy()
                    self.display_paciente()
                except Exception as e:
                    messagebox.showerror("Erro", f"Erro ao cadastrar paciente: {e}")

        Button(add_window, text="Adicionar", command=submit_paciente, bg="#4CAF50", fg="white").place(x=150, y=260, width=100, height=30)

    def del_paciente(self):
        paciente_id = simpledialog.askinteger("Excluir Paciente", "Digite o ID do paciente a ser excluído:")

        if paciente_id is not None:
                PacienteManager.delete_paciente(paciente_id)
                messagebox.showinfo("Paciente", "Paciente excluído com sucesso!")
                self.display_paciente()
        else:
            messagebox.showinfo("Erro", "Nenhum ID foi fornecido.")

    def open_dashboard(self):
        self.window.destroy()

        from DashboardView import DashboardView
        dashboard_window = Tk()  
        DashboardView(dashboard_window)
        dashboard_window.mainloop()

    def open_pacient(self):
        self.window.destroy()
    
        from PacientView import PacienteView
        pacient_window = Tk()  
        PacienteView(pacient_window)
        pacient_window.mainloop()

    def open_medicamento(self):
        self.window.destroy()

        from pharmacyView import MedicamentoView
        medicamento_window = Tk()
        MedicamentoView(medicamento_window)
        medicamento_window.mainloop()

    def open_consulta(self):
        self.window.destroy()

        from ConsultasView import ConsultasView
        consulta_window = Tk()
        ConsultasView(consulta_window)

    def open_exame(self):
        self.window.destroy()

        from ExamView import ExameView
        exame_window = Tk()
        ExameView(exame_window)

    def open_tratamento(self):
        self.window.destroy()

        from TreatmentView import TratamentoView
        tratamento_window = Tk()
        TratamentoView(tratamento_window)

    def open_cirurgia(self):
        self.window.destroy()

        from surgeriesView import CirurgiaView
        cirurgia_window = Tk()
        CirurgiaView(cirurgia_window)

    def open_medicos(self):
        self.window.destroy()

        from MedicosView import MedicosView
        medicos_window = Tk()
        MedicosView(medicos_window)


def page():
    window = Tk()
    PacienteView(window)
    window.mainloop()

if __name__ == "__main__":
    page()