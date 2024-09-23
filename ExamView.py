from tkinter import *
from tkinter import ttk, simpledialog, messagebox
from PIL import ImageTk, Image
from tkinter import messagebox
from notification_operation import get_notifications
import tkinter as tk
from exam import ExameManager


class ExameView:
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
        self.header_image = Image.open('images/exames_head.png')
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

        self.add_button = Button(self.window, text="Adicionar Exame", command=self.add_exame, font=("Arial", 12), bg="#4CAF50", fg="white")
        self.add_button.place(x=330, y=470, width=150, height=40)
        
        self.del_button = Button(self.window, text="Excluir Exame", command=self.del_exame, font=("Arial", 12), bg="#FF6347", fg="white")
        self.del_button.place(x=500, y=470, width=150, height=40)

        # Exames Cadastrados

        self.display_exame()

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
        self.Paciente_text.place(x=800, y=60)
        
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
        self.Exames.place(x=70, y=175)

        self.Exames_text = Button(self.sidebar, text="Exames", bg='#F4F4F4', font=("yu gothic ui", 17, "bold"), bd=0,
                             cursor='hand2', activebackground='#F4F4F4', command=self.open_exame)
        self.Exames_text.place(x=110, y=180)
        
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


    def display_exame(self):
        if hasattr(self, 'exame_table'):
            self.exame_table.destroy()

        exames = ExameManager.get_all_exames()
        if not exames:
            messagebox.showinfo("Informação", "Nenhum exame encontrado no sistema.")
            return

        columns = ('id', 'paciente_id', 'medico_id', 'enfermeiro_id', 'tipo_exame', 'data_hora', 'resultado', 'observacoes')
        self.exame_table = ttk.Treeview(self.body_frame_1_label, columns=columns, show='headings')
        self.exame_table.heading('id', text='ID')
        self.exame_table.heading('paciente_id', text='Paciente')
        self.exame_table.heading('medico_id', text='Médico')
        self.exame_table.heading('enfermeiro_id', text='Enfermeiro')
        self.exame_table.heading('tipo_exame', text='Tipo de Exame')
        self.exame_table.heading('data_hora', text='Data/Hora')
        self.exame_table.heading('resultado', text='Resultado')
        self.exame_table.heading('observacoes', text='Observações')
        self.exame_table.place(x=20, y=20, width=800, height=300)

        for exame in exames:
            values = (
                exame.get('id', ''),
                exame.get('paciente_id', ''),
                exame.get('medico_id', ''),
                exame.get('enfermeiro_id', ''),
                exame.get('tipo_exame', ''),
                exame.get('data_hora', ''),
                exame.get('resultado', ''),
                exame.get('observacoes', '')
                )
            self.exame_table.insert('', 'end', values=values)


    def add_exame(self):
        add_window = Toplevel(self.window)
        add_window.title("Adicionar Exame")
        add_window.geometry("400x300")
        add_window.config(background='#EAE9E8')

        Label(add_window, text="Paciente", bg='#EAE9E8').place(x=20, y=20)
        paciente_id_entry = Entry(add_window)
        paciente_id_entry.place(x=150, y=20)

        Label(add_window, text="Médico", bg='#EAE9E8').place(x=20, y=60)
        medico_id_entry = Entry(add_window)
        medico_id_entry.place(x=150, y=60)

        Label(add_window, text="Enfermeiro", bg='#EAE9E8').place(x=20, y=100)
        enfermeiro_id_entry = Entry(add_window)
        enfermeiro_id_entry.place(x=150, y=100)

        Label(add_window, text="Tipo de Exame", bg='#EAE9E8').place(x=20, y=140)
        tipo_exame_entry = Entry(add_window)
        tipo_exame_entry.place(x=150, y=140)

        Label(add_window, text="Data/Hora", bg='#EAE9E8').place(x=20, y=180)
        data_hora_entry = Entry(add_window)
        data_hora_entry.place(x=150, y=180)

        Label(add_window, text="Resultado", bg='#EAE9E8').place(x=20, y=220)
        resultado_entry = Entry(add_window)
        resultado_entry.place(x=150, y=220)

        Label(add_window, text="Observações", bg='#EAE9E8').place(x=20, y=260)
        observacoes_entry = Entry(add_window)
        observacoes_entry.place(x=150, y=260)


        def submit_exame():
            paciente_id = paciente_id_entry.get()
            medico_id = medico_id_entry.get()
            enfermeiro_id = enfermeiro_id_entry.get()
            tipo_exame = tipo_exame_entry.get()
            data_hora = data_hora_entry.get()
            resultado = resultado_entry.get()
            observacoes = observacoes_entry.get()

            if not paciente_id or not medico_id or not enfermeiro_id or not tipo_exame or not data_hora or not resultado or not observacoes:
                messagebox.showerror("Erro", "Preencha todos os campos.")
            else:
                try:
                    ExameManager.create_exame(
                        paciente_id=paciente_id, 
                        medico_id=medico_id,
                        enfermeiro_id=enfermeiro_id, 
                        tipo_exame=tipo_exame, 
                        data_hora=data_hora,
                        resultado=resultado,
                        observacoes=observacoes
                    )
                    messagebox.showinfo("Exame", "Exame cadastrado com sucesso!")
                    add_window.destroy()
                    self.display_exame()
                except Exception as e:
                    messagebox.showerror("Erro", f"Erro ao cadastrar exame: {e}")

        Button(add_window, text="Adicionar", command=submit_exame, bg="#4CAF50", fg="white").place(x=150, y=260, width=100, height=30)

    def del_exame(self):
        exame_id = simpledialog.askinteger("Excluir Exame", "Digite o ID do Exame a ser excluído:")

        if exame_id is not None:
                ExameManager.delete_exame(exame_id)
                messagebox.showinfo("Exame", "Exame excluído com sucesso!")
                self.display_exame()
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
    ExameView(window)
    window.mainloop()

if __name__ == "__main__":
    page()