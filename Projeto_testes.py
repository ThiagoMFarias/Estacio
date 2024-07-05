import tkinter as tk
from tkinter import messagebox

class JanelaCadastro:
    def __init__(self, root):
        self.root = root
        self.root.title('Cadastro de Usuário')
        self.root.geometry('300x200')
        
        self.label_cadastro = tk.Label(self.root, text="Preencha os campos abaixo para cadastrar sua senha:", font=('Inter', 12))
        self.label_cadastro.pack(pady=10)
        
        self.label_usuario = tk.Label(self.root, text="Usuário:")
        self.label_usuario.pack()
        self.entry_usuario = tk.Entry(self.root, width=30)
        self.entry_usuario.pack(pady=5)
        
        self.label_nova_senha = tk.Label(self.root, text="Nova Senha:")
        self.label_nova_senha.pack()
        self.entry_nova_senha = tk.Entry(self.root, width=30, show='*')
        self.entry_nova_senha.pack(pady=5)
        
        self.botao_confirmar = tk.Button(self.root, text="Confirmar", command=self.confirmar_cadastro)
        self.botao_confirmar.pack(pady=10)
    
    def confirmar_cadastro(self):
        # Aqui você poderia implementar a lógica para confirmar o cadastro
        usuario = self.entry_usuario.get()
        senha = self.entry_nova_senha.get()
        messagebox.showinfo("Cadastro Confirmado", f"Usuário '{usuario}' cadastrado com sucesso!")

class TelaLogin:
    def __init__(self, root):
        self.root = root
        self.root.geometry('300x350')
        self.root.title('Login')
        self.root['bg'] = '#B8D6F0'
        
        self.root.resizable(width=False, height=False)
                       
        self.frame = tk.Frame(self.root, bg='#B8D6F0')
        self.frame.pack(padx=10, pady=50)  # Ajustei pady para mover widgets para cima
        
        label_font = ('Inter', 10, 'bold')
        label_font1 = ('Inter', 15, 'bold')
        label_font2 = ('Inter', 10, 'underline')
        
        self.label_login = tk.Label(self.frame, text="CPF:", bg='#B8D6F0', font=label_font)
        self.label_login.grid(row=3, column=1, sticky='w', pady=5)
                                
        self.entry_login = tk.Entry(self.frame, width=50, bg='white')
        self.entry_login.grid(row=4, column=1, pady=5)
        
        self.label_senha = tk.Label(self.frame, text="Senha:", bg='#B8D6F0', font=label_font)
        self.label_senha.grid(row=5, column=1, sticky='w', pady=10)
        
        self.entry_senha = tk.Entry(self.frame, width=50, bg='white', show='*')  
        self.entry_senha.grid(row=6, column=1)
        
        self.label_esqueci_senha = tk.Label(self.frame, text="Esqueci minha senha", font=label_font2, bg='#B8D6F0', fg='blue', cursor='hand2')
        self.label_esqueci_senha.grid(row=7, column=1, pady=10, sticky='w')
        self.label_esqueci_senha.bind("<Button-1>", self.abrir_janela_cadastro)
        
        self.label_esqueci_senha= tk.Button(self.frame, text='Acessar', font=label_font, bg='#f72585', fg='white', cursor='hand2')
        self.label_esqueci_senha.grid(row=8, column=1, pady=10, sticky='ew')
        self.label_esqueci_senha.bind("<Button-1>", self.abrir_janela_cadastro)

    def abrir_janela_cadastro(self, event):
        # Função para abrir a janela de cadastro
        self.janela_cadastro = tk.Toplevel(self.root)
        app_cadastro = JanelaCadastro(self.janela_cadastro)

root = tk.Tk()
app = TelaLogin(root)
root.mainloop()
