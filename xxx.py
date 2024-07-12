# xxx.py

import tkinter as tk
from tkinter import messagebox
from tela_cadastro_senha import NewPassword
import psycopg2
import bcrypt

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
        
        if self.verificar_usuario(cpf, senha):
            messagebox.showinfo("Login", "Login realizado com sucesso!")
        else:
            messagebox.showerror("Login", "CPF ou senha incorretos!")
            
    # Verificando se login e senha bate com o do banco
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
    