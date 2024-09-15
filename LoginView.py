import requests
from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
from werkzeug.security import check_password_hash
import auth_services
from db_operations import get_db_connection

class LoginForm:
    def __init__(self, window):
        self.window = window
        self.window.geometry("1166x718")
        self.window.state('zoomed')

        # ============================background image============================
        self.bg_frame = Image.open('images/background_1.png')
        photo = ImageTk.PhotoImage(self.bg_frame)
        self.bg_panel = Label(self.window, image=photo)
        self.bg_panel.image = photo
        self.bg_panel.pack(fill='both', expand='yes')

        # ============================Login Frame============================
        self.lgn_frame = Frame(self.window, bg='#EAE9E8', width=950, height=600)
        self.lgn_frame.place(x=200, y=70)

        # ============================Right Side Image============================
        self.side_image = Image.open('images/image_login_1.png')
        photo = ImageTk.PhotoImage(self.side_image)
        self.side_image_label = Label(self.window, image=photo, bg='#EAE9E8')
        self.side_image_label.image = photo
        self.side_image_label.place(x=650, y=150)

        # ============================Logo Image============================
        self.Sign_in_image = Image.open('images/image_login_logo.png')
        photo = ImageTk.PhotoImage(self.Sign_in_image)
        self.Sign_in_image_label = Label(self.window, image=photo, bg='#EAE9E8')
        self.Sign_in_image_label.image = photo
        self.Sign_in_image_label.place(x=450, y=168)

        self.Sign_in = Label(self.window, text="MedTrack", fg="black", font=("yu gothic ui", 27, "bold"))
        self.Sign_in.place(x=450, y=250)
        self.Sign_in_subtitle = Label(self.window, text="Coloque as suas informações de login", bg="#EAE9E8", fg="black", font=("yu gothic ui", 13))
        self.Sign_in_subtitle.place(x=385, y=300)

        # ============================Username============================
        self.username_label = Label(self.window, text="Usuário", bg="#EAE9E8", fg="#4f4e4d", font=("yu gothic ui", 20, "bold"))
        self.username_label.place(x=350, y=350)

        self.username_entry = Entry(self.window, highlightthickness=0, relief=FLAT, bg="#EAE9E8", fg="#6b5a69", font=("yu gothic ui", 18, "bold"))
        self.username_entry.place(x=350, y=400, width=450, height=50)

        self.username_line = Canvas(self.window, width=500, height=2, bg="#bdb9b1", highlightthickness=0)
        self.username_line.place(x=350, y=450)

        # ============================Password============================
        self.password_label = Label(self.window, text="Senha", bg="#EAE9E8", fg="#4f4e4d", font=("yu gothic ui", 20, "bold"))
        self.password_label.place(x=350, y=500)

        self.password_entry = Entry(self.window, highlightthickness=0, relief=FLAT, bg="#EAE9E8", fg="#6b5a69", font=("yu gothic ui", 18, "bold"), show="*")
        self.password_entry.place(x=350, y=550, width=450, height=50)

        self.password_line = Canvas(self.window, width=500, height=2, bg="#bdb9b1", highlightthickness=0)
        self.password_line.place(x=350, y=600)

        # ============================Login Button============================
        self.lgn_button_image = Image.open('images/Button_1.png')
        photo = ImageTk.PhotoImage(self.lgn_button_image)
        self.lgn_button = Button(self.window, image=photo, width=500, bg='#EAE9E8', bd=0, cursor='hand2', activebackground='#EAE9E8', command=self.login)
        self.lgn_button.image = photo
        self.lgn_button.place(x=350, y=650)

    def login(self):
        email = self.username_entry.get()
        password = self.password_entry.get()

        if not email or not password:
            messagebox.showerror("Erro", "Email e senha são obrigatórios")
            return

        try:
            
            with get_db_connection() as db:
                query = "SELECT * FROM usuarios WHERE email = %s"
                result = db.query(query, (email,))
                user = result[0] if result else None

            if not user:
                messagebox.showerror("Erro", "Usuário não encontrado")
                return

            if not check_password_hash(user['senha'], password):
                messagebox.showerror("Erro", "Senha incorreta")
                return

            messagebox.showinfo("Sucesso", f"Bem-vindo {user['nome']}!")
        
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao conectar ao banco de dados: {e}")

def page():
    window = Tk()
    LoginForm(window)
    window.mainloop()

if __name__ == "__main__":
    page()