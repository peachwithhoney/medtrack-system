from tkinter import *
from tkinter import ttk, simpledialog, messagebox
from PIL import ImageTk, Image
from tkinter import messagebox
from notification_operation import get_notifications
import tkinter as tk
from pharmacy import MedicamentoManager


class MedicamentoView:
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
        self.header_image = Image.open('images/farmacia_head.png')
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

        self.add_button = Button(self.window, text="Adicionar Medicamento", command=self.add_medicamento, font=("Arial", 12), bg="#4CAF50", fg="white")
        self.add_button.place(x=330, y=470, width=150, height=40)
        
        self.del_button = Button(self.window, text="Excluir Medicamento", command=self.del_medicamento, font=("Arial", 12), bg="#FF6347", fg="white")
        self.del_button.place(x=500, y=470, width=150, height=40)

        # Medicamentos Cadastrados

        self.display_medicamento()

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
        self.Paciente.place(x=40, y=55)

        self.Paciente_text = Button(self.sidebar, text="Paciente", bg='#F4F4F4', font=("yu gothic ui", 17, "bold"), bd=0,
                             cursor='hand2', activebackground='#F4F4F4')
        self.Paciente_text.place(x=80, y=60)
        
        # Consultas
        self.Consultas_Image = Image.open('images/Icon_Dashboard_Button.png')
        self.Consultas_Image_resized = self.Consultas_Image.resize((50, 50), Image.LANCZOS) 
        self.Consultas_Image_photo = ImageTk.PhotoImage(self.Consultas_Image_resized)
        self.Consultas = Label(self.sidebar, image=self.Consultas_Image_photo, bg='#F4F4F4')
        self.Consultas.image = self.Consultas_Image_photo  
        self.Consultas.place(x=40, y=95)

        self.Consultas_text = Button(self.sidebar, text="Consultas", bg='#F4F4F4', font=("yu gothic ui", 17, "bold"), 
                             cursor='hand2', activebackground='#F4F4F4', command=self.open_consulta)
        self.Consultas_text.place(x=80, y=100)
        
        # Médicos
        self.Medicos_Image = Image.open('images/Icon_Dashboard_Button.png')
        self.Medicos_Image_resized = self.Medicos_Image.resize((50, 50), Image.LANCZOS) 
        self.Medicos_Image_photo = ImageTk.PhotoImage(self.Medicos_Image_resized)
        self.Medicos = Label(self.sidebar, image=self.Medicos_Image_photo, bg='#F4F4F4')
        self.Medicos.image = self.Medicos_Image_photo  
        self.Medicos.place(x=40, y=135)

        self.Medicos_text = Button(self.sidebar, text="Médicos", bg='#F4F4F4', font=("yu gothic ui", 17, "bold"), bd=0,fg='#FF914D',
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
        self.Farmacia.place(x=70, y=295)

        self.Farmacia_text = Button(self.sidebar, text="Farmacia", bg='#F4F4F4', font=("yu gothic ui", 17, "bold"), bd=0,
                             cursor='hand2', activebackground='#F4F4F4', command=self.open_medicamento)
        self.Farmacia_text.place(x=110, y=300)         

    
    def logout(self):
        messagebox.showinfo("Logout", "Você saiu com sucesso!")
        self.window.destroy()
    
        from LoginView import LoginForm  
        login_window = Tk()
        LoginForm(login_window)
        login_window.mainloop()


    def display_medicamento(self):
        if hasattr(self, 'medicamento_table'):
            self.medicamento_table.destroy()

        medicamentos = MedicamentoManager.get_all_medicamentos()
        if not medicamentos:
            messagebox.showinfo("Informação", "Nenhum medicamento encontrado no sistema.")
            return

        columns = ('id', 'nome', 'descricao', 'estoque')
        self.medicamento_table = ttk.Treeview(self.body_frame_1_label, columns=columns, show='headings')
        self.medicamento_table.heading('id', text='ID')
        self.medicamento_table.heading('nome', text='Nome')
        self.medicamento_table.heading('descricao', text='Descrição')
        self.medicamento_table.heading('estoque', text='Estoque')
        self.medicamento_table.place(x=20, y=20, width=800, height=300)

        for medicamento in medicamentos:
            values = (
                medicamento.get('id', ''),
                medicamento.get('nome', ''),
                medicamento.get('descricao', ''),
                medicamento.get('estoque', '')
                )
            self.medicamento_table.insert('', 'end', values=values)


    def add_medicamento(self):
        add_window = Toplevel(self.window)
        add_window.title("Adicionar Medicamentos")
        add_window.geometry("400x300")
        add_window.config(background='#EAE9E8')

        Label(add_window, text="Nome", bg='#EAE9E8').place(x=20, y=20)
        nome_entry = Entry(add_window)
        nome_entry.place(x=150, y=20)

        Label(add_window, text="Descrição", bg='#EAE9E8').place(x=20, y=60)
        descricao_entry = Entry(add_window)
        descricao_entry.place(x=150, y=60)

        Label(add_window, text="Estoque", bg='#EAE9E8').place(x=20, y=100)
        estoque_entry = Entry(add_window)
        estoque_entry.place(x=150, y=100)


        def submit_medicamento():
            nome = nome_entry.get()
            descricao = descricao_entry.get()
            estoque = estoque_entry.get()

            if not nome or not descricao or not estoque :
                messagebox.showerror("Erro", "Preencha todos os campos.")
            else:
                try:
                    MedicamentoManager.create_medicamento(
                        nome=nome,
                        descricao=descricao,
                        estoque=estoque 
                    )
                    messagebox.showinfo("Medicamento", "Medicamento cadastrado com sucesso!")
                    add_window.destroy()
                    self.display_medicamento()
                except Exception as e:
                    messagebox.showerror("Erro", f"Erro ao cadastrar medicamento: {e}")

        Button(add_window, text="Adicionar", command=submit_medicamento, bg="#4CAF50", fg="white").place(x=150, y=260, width=100, height=30)

    def del_medicamento(self):
        medicamento_id = simpledialog.askinteger("Excluir Medicamento", "Digite o ID do Medicamento a ser excluído:")

        if medicamento_id is not None:
                MedicamentoManager.delete_medicamento(medicamento_id)
                messagebox.showinfo("Medicamento", "Medicamento excluído com sucesso!")
                self.display_medicamento()
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
    MedicamentoView(window)
    window.mainloop()

if __name__ == "__main__":
    page()