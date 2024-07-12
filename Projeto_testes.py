import tkinter as tk
from tkinter import messagebox
from tela_cadastro_senha import NewPassword
import psycopg2
import bcrypt
import random
import string
from email_utils import enviar_email

class TelaLogin:
    def __init__(self, root):
        # Estabele os parâmetros da janela principal
        self.root = root
        self.root.geometry('300x350')
        self.root.title('EduManege')
        self.root['bg'] = '#B8D6F0'
        
        # Impossibilita o usuário de aumentar ou diminuir a tela
        self.root.resizable(width=False, height=False)
                       
        self.frame = tk.Frame(self.root, bg='#B8D6F0')
        self.frame.pack(padx=10, pady=50)
        
        # Fontes usadas no projeto
        label_font = ('Inter', 10, 'bold')
        label_font2 = ('Inter', 10, 'underline')
        
        # Criação da label CPF
        self.label_login = tk.Label(self.frame, text="CPF:", bg='#B8D6F0', font=label_font)
        self.label_login.grid(row=3, column=1, sticky='w', pady=5)
        
        # Criação da entry CPF                     
        self.entry_login = tk.Entry(self.frame, width=50, bg='white')
        self.entry_login.grid(row=4, column=1, pady=5)
        
        # Criação da label Senha
        self.label_senha = tk.Label(self.frame, text="Senha:", bg='#B8D6F0', font=label_font)
        self.label_senha.grid(row=5, column=1, sticky='w', pady=10)
        
        # Criação da entry Senha
        self.entry_senha = tk.Entry(self.frame, width=50, bg='white', show='*')
        self.entry_senha.grid(row=6, column=1)
        
        # Criação da label esqueci minha senha
        self.label_esqueci_senha = tk.Label(self.frame, text="Esqueci minha senha", font=label_font2, bg='#B8D6F0', fg='blue', cursor='hand2')
        self.label_esqueci_senha.grid(row=7, column=1, pady=10, sticky='w')
        self.label_esqueci_senha.bind("<Button-1>", self.abrir_tela_cadastro_senha) #ação da label esqueci minha senha
        
        # Criação e ação do botão Acessar
        self.botao_acessar = tk.Button(self.frame, text='Acessar', font=label_font, bg='#f72585', fg='white', cursor='hand2', command=self.validar_login)
        self.botao_acessar.grid(row=8, column=1, pady=10, sticky='ew')

    # Criação de uma nova janela ao apertar na label esqueci minha senha
    def abrir_tela_cadastro_senha(self, event=None):
        self.cad_senha = tk.Toplevel(self.root)
        app_cadastro = NewPassword(self.cad_senha)
        
        # Trava a janela 
        self.cad_senha.transient(self.root)  # Faz a nova janela modal em relação à janela principal
        self.cad_senha.grab_set()  # Captura todos os eventos de entrada para a nova janela
        self.root.wait_window(self.cad_senha)  # Espera até que a nova janela seja fechada
        
    def validar_login(self):
        cpf = self.entry_login.get()
        senha = self.entry_senha.get()
        
        user_id = self.obter_usuario_id(cpf)
        if user_id is None:
            messagebox.showerror("Login", "CPF não cadastrado!")
            return

        tentativas = self.registrar_tentativa(user_id)

        if tentativas >= 3:
            self.bloquear_usuario(user_id)
            messagebox.showerror("Login", "Usuário bloqueado. Uma nova senha foi enviada ao seu email.")
        elif self.verificar_usuario(cpf, senha):
            self.resetar_tentativas(user_id)
            messagebox.showinfo("Login", "Login realizado com sucesso!")
        else:
            messagebox.showerror("Login", "CPF ou senha incorretos!")

    def obter_usuario_id(self, cpf):
        try:
            conn = psycopg2.connect(
                host="localhost",
                database="CADASTRO_USER",
                user="postgres",
                password="postgres",
                port="5432"
            )
            cur = conn.cursor()
            cur.execute("SELECT id FROM cadastro_usuario WHERE cpf = %s", (cpf,))
            row = cur.fetchone()
            cur.close()
            conn.close()
            if row:
                return row[0]
            return None
        except Exception as e:
            print(f"Erro ao conectar ao banco de dados: {e}")
            return None

    def registrar_tentativa(self, cpf):
        try:
            conn = psycopg2.connect(
                host="localhost",
                database="CADASTRO_USER",
                user="postgres",
                password="postgres",
                port="5432"
            )
            cur = conn.cursor()
            cur.execute("SELECT tentativas FROM log_sessao WHERE id_usuario = %s ORDER BY data_login DESC LIMIT 1", (cpf,))
            row = cur.fetchone()
            
            if row:
                tentativas = row[0] + 1
            else: 
                tentativas = 1
            
            cur.execute("INSERT INTO log_sessao (tentativas, id_usuario) VALUES (%s, %s)", (tentativas, cpf))
            conn.commit()
            cur.close()
            conn.close()
            return tentativas
        
        except Exception as e:
            print(f"Erro ao conectar ao banco de dados: {e}")
            return 0

    def resetar_tentativas(self, user_id):
        try:
            conn = psycopg2.connect(
                host="localhost",
                database="CADASTRO_USER",
                user="postgres",
                password="postgres",
                port="5432"
            )
            cur = conn.cursor()
            cur.execute("INSERT INTO log_sessao (tentativas, id_usuario) VALUES (%s, %s)", (0, user_id))
            conn.commit()
            cur.close()
            conn.close()
            
        except Exception as e:
            print(f"Erro ao conectar ao banco de dados: {e}")

    def bloquear_usuario(self, user_id):
        nova_senha = self.gerar_senha()
        nova_senha_hashed = self.hash_senha(nova_senha)
        self.atualizar_senha_no_banco(user_id, nova_senha_hashed)
        email_usuario = self.obter_email_usuario(user_id)
        enviar_email(para=email_usuario, assunto='Nova senha gerada', corpo=f"""
        <html>
        <body>
            <p>Olá,</p>
            <p>Você foi bloqueado após três tentativas de login incorretas.</p>
            <p>Sua nova senha é: <strong>{nova_senha}</strong></p>
            <p>Atenciosamente,</p>
            <p>Seu sistema de cadastro</p>
        </body>
        </html>
        """)
        
        self.resetar_tentativas(user_id)

    def gerar_senha(self):
        caracteres = string.ascii_letters + string.digits + string.punctuation
        senha = ''.join(random.choices(caracteres, k=8))
        return senha

    def hash_senha(self, senha):
        salt = bcrypt.gensalt()
        senha_hashed = bcrypt.hashpw(senha.encode('utf-8'), salt)
        return senha_hashed.decode('utf-8')

    def atualizar_senha_no_banco(self, user_id, nova_senha_hashed):
        try:
            conn = psycopg2.connect(
                host="localhost",
                database="CADASTRO_USER",
                user="postgres",
                password="postgres",
                port="5432"
            )
            cur = conn.cursor()
            cur.execute("UPDATE cadastro_usuario SET senha = %s WHERE id = %s", (nova_senha_hashed, user_id))
            conn.commit()
            cur.close()
            conn.close()
        except Exception as e:
            print(f"Erro ao conectar ao banco de dados: {e}")

    def obter_email_usuario(self, user_id):
        try:
            conn = psycopg2.connect(
                host="localhost",
                database="CADASTRO_USER",
                user="postgres",
                password="postgres",
                port="5432"
            )
            cur = conn.cursor()
            cur.execute("SELECT email FROM cadastro_usuario WHERE id = %s", (user_id,))
            row = cur.fetchone()
            cur.close()
            conn.close()
            if row:
                return row[0]
            return None
        except Exception as e:
            print(f"Erro ao conectar ao banco de dados: {e}")
            return None

    def verificar_usuario(self, cpf, senha):
        try:
            conn = psycopg2.connect(
                host= "localhost",
                database= "CADASTRO_USER",
                user= "postgres",
                password= "postgres",
                port="5432"
            )
            cur = conn.cursor()
            cur.execute("SELECT senha FROM cadastro_usuario WHERE cpf = %s", (cpf,))
            senha_hashed = cur.fetchone()[0]
            cur.close()
            conn.close()
            
            # Verifica se a senha fornecida corresponde à senha criptografada
            if bcrypt.checkpw(senha.encode('utf-8'), senha_hashed.encode('utf-8')):
                return True      
            
            return False
        
        except Exception as e:
            print(f"Erro ao conectar ao banco de dados: {e}")
            return False

if __name__ == "__main__":
    root = tk.Tk()
    app = TelaLogin(root)
    root.mainloop()
