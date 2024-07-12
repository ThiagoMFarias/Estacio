# tela_cadastro_senha.py

import tkinter as tk
from tkinter import messagebox
import random
import string
from email_utils import enviar_email
import psycopg2
import bcrypt

class NewPassword:
    def __init__(self, root):
        self.root = root
        self.root.title('Solicitação de senha')
        self.root.geometry('300x200')
        
        self.label_cadastro = tk.Label(self.root, text="Preencha o campo abaixo:", font=('Inter', 12, 'bold'))
        self.label_cadastro.pack(pady=10)
        
        self.label_email = tk.Label(self.root, text="E-mail:")
        self.label_email.pack()
        self.entry_email = tk.Entry(self.root, width=30)
        self.entry_email.pack(pady=5)
               
        self.botao_confirmar = tk.Button(self.root, text="Enviar", command=self.send_new_email)
        self.botao_confirmar.pack(pady=10)
    
    def send_new_email(self):
        email_destino = self.entry_email.get()
        nova_senha = self.gerar_senha()
        
        # Criptografar a nova senha
        nova_senha_hashed = self.hash_senha(nova_senha)
        
        # Atualizar a senha no banco de dados
        if self.atualizar_senha_no_banco(email_destino, nova_senha_hashed):
            enviar_email(para=email_destino, assunto='Nova senha gerada', corpo=f"""
            <html>
            <body>
                <p>Olá,</p>
                <p>Sua nova senha é: <strong>{nova_senha}</strong></p>
                <p>Atenciosamente,</p>
                <p>Seu sistema de cadastro</p>
            </body>
            </html>
            """)
            
            messagebox.showinfo('E-mail enviado.', 'Uma nova senha foi enviada para o endereço fornecido.')
            self.root.destroy()
        else:
            messagebox.showerror('Erro', 'Erro ao atualizar a senha no banco.')

    def gerar_senha(self):
        caracteres = string.ascii_letters + string.digits + string.punctuation
        senha = ''.join(random.choices(caracteres, k=8))
        return senha

    def hash_senha(self, senha):
        # Gerar um salt e usar bcrypt para hashear a senha
        salt = bcrypt.gensalt()
        senha_hashed = bcrypt.hashpw(senha.encode('utf-8'), salt)
        return senha_hashed.decode('utf-8')

    def atualizar_senha_no_banco(self, email_usuario, nova_senha_hashed):
        try:
            conn = psycopg2.connect(
                host='localhost',
                database='CADASTRO_USER',
                user='postgres',
                password='postgres',
                port='5432'
            )
            cur = conn.cursor()
            cur.execute("UPDATE cadastro_usuario SET senha = %s WHERE email = %s", (nova_senha_hashed, email_usuario))
            conn.commit()
            cur.close()
            conn.close()
            print(nova_senha_hashed)
            return True
            
        except Exception as e:
            print(f"Erro ao salvar no banco de dados: {e}")
            return False

if __name__ == "__main__":
    root = tk.Tk()
    app = NewPassword(root)
    root.mainloop()
    