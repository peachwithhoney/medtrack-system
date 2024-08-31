import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import mysql.connector
from mysql.connector import Error

# Funções de conexão e CRUD
def create_connection():
    return mysql.connector.connect(
        host='localhost',
        user='root',
        password='yourpassword',
        database='hospital'
    )

def add_paciente(nome, idade, endereco):
    try:
        conn = create_connection()
        cursor = conn.cursor()
        cursor.execute('''
        INSERT INTO pacientes (nome, idade, endereco)
        VALUES (%s, %s, %s)
        ''', (nome, idade, endereco))
        conn.commit()
    except Error as e:
        print(f'Error: {e}')
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()

def get_pacientes():
    try:
        conn = create_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM pacientes')
        return cursor.fetchall()
    except Error as e:
        print(f'Error: {e}')
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()

def delete_paciente(id):
    try:
        conn = create_connection()
        cursor = conn.cursor()
        cursor.execute('DELETE FROM pacientes WHERE id = %s', (id,))
        conn.commit()
    except Error as e:
        print(f'Error: {e}')
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()

def update_paciente(id, nome, idade, endereco):
    try:
        conn = create_connection()
        cursor = conn.cursor()
        cursor.execute('''
        UPDATE pacientes
        SET nome = %s, idade = %s, endereco = %s
        WHERE id = %s
        ''', (nome, idade, endereco, id))
        conn.commit()
    except Error as e:
        print(f'Error: {e}')
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()

# Repita o padrão acima para medicos, enfermeiros, cirurgias e departamentos

# Classe para a interface gráfica
class HospitalApp:
    def __init__(self, root):
        self.root = root
        self.root.title('Sistema de Cadastro Hospitalar')
        
        # Configuração do notebook para abas
        self.notebook = ttk.Notebook(root)
        self.notebook.pack(fill='both', expand=True)
        
        # Adicionando abas
        self.add_pacientes_tab()
        self.add_medicos_tab()
        self.add_enfermeiros_tab()
        self.add_cirurgias_tab()
        self.add_departamentos_tab()
        
    def add_pacientes_tab(self):
        tab = ttk.Frame(self.notebook)
        self.notebook.add(tab, text='Pacientes')
        
        tk.Label(tab, text='Cadastro de Pacientes').pack()
        tk.Label(tab, text='Nome').pack()
        self.paciente_nome_entry = tk.Entry(tab)
        self.paciente_nome_entry.pack()
        
        tk.Label(tab, text='Idade').pack()
        self.paciente_idade_entry = tk.Entry(tab)
        self.paciente_idade_entry.pack()
        
        tk.Label(tab, text='Endereço').pack()
        self.paciente_endereco_entry = tk.Entry(tab)
        self.paciente_endereco_entry.pack()
        
        tk.Button(tab, text='Adicionar Paciente', command=self.add_paciente).pack()
        
        self.paciente_listbox = tk.Listbox(tab)
        self.paciente_listbox.pack(fill='both', expand=True)
        self.update_paciente_list()
        
        tk.Button(tab, text='Excluir Paciente', command=self.delete_paciente).pack()
        tk.Button(tab, text='Atualizar Paciente', command=self.update_paciente).pack()

    # Adicione métodos para Médicos, Enfermeiros, Cirurgias e Departamentos conforme mostrado anteriormente.

    def add_paciente(self):
        nome = self.paciente_nome_entry.get()
        idade = int(self.paciente_idade_entry.get())
        endereco = self.paciente_endereco_entry.get()
        add_paciente(nome, idade, endereco)
        self.update_paciente_list()
        messagebox.showinfo('Sucesso', 'Paciente adicionado com sucesso!')

    def update_paciente_list(self):
        self.paciente_listbox.delete(0, tk.END)
        pacientes = get_pacientes()
        for paciente in pacientes:
            self.paciente_listbox.insert(tk.END, f'{paciente[0]} - {paciente[1]} - {paciente[2]} anos - {paciente[3]}')

    def delete_paciente(self):
        selected = self.paciente_listbox.curselection()
        if not selected:
            messagebox.showwarning('Aviso', 'Selecione um paciente para excluir.')
            return
        paciente_id = self.paciente_listbox.get(selected[0]).split(' - ')[0]
        delete_paciente(paciente_id)
        self.update_paciente_list()
        messagebox.showinfo('Sucesso', 'Paciente excluído com sucesso!')

    def update_paciente(self):
        selected = self.paciente_listbox.curselection()
        if not selected:
            messagebox.showwarning('Aviso', 'Selecione um paciente para atualizar.')
            return
        paciente_id = self.paciente_listbox.get(selected[0]).split(' - ')[0]
        nome = self.paciente_nome_entry.get()
        idade = int(self.paciente_idade_entry.get())
        endereco = self.paciente_endereco_entry.get()
        update_paciente(paciente_id, nome, idade, endereco)
        self.update_paciente_list()
        messagebox.showinfo('Sucesso', 'Paciente atualizado com sucesso!')

    # Métodos para Médicos, Enfermeiros, Cirurgias e Departamentos seguem o mesmo padrão

# Criação da janela principal
root = tk.Tk()
app = HospitalApp(root)
root.mainloop()
