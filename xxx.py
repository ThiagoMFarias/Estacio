import tkinter as tk
import Root_cadastro

class TelaLogin:
    def __init__(self, root):
        self.root = root
        self.root.geometry('300x330')
        self.root.title('EduManage')
        self.root['bg']='#B8D6F0'
        
        self.root.resizable(width=False, height=False)
                       
        self.frame = tk.Frame(self.root, bg='#B8D6F0')
        self.frame.pack(padx=10, pady=10)
        
        label_font = ('Inter', 10, 'bold')
        label_font1= ('Inter', 15, 'bold')
        label_font_descricao= ('Inter', 9)
        
        self.label_login1 = tk.Label(self.frame, text='Login', bg='#B8D6F0', font=label_font1)
        self.label_login1.grid(row=0, column=1, sticky='w', pady=10)
        
        self.label_descricao = tk.Label(self.frame, text='Digite os seus dados de acesso no campo abaixo.', bg='#B8D6F0', font=label_font_descricao)
        self.label_descricao.grid(row=1, column=1, sticky='w', pady=10)
        
        self.label_login = tk.Label(self.frame, text="CPF:", bg='#B8D6F0', font=label_font)
        self.label_login.grid(row=3, column=1, sticky='w', pady=5)
                                
        self.entry_login = tk.Entry(self.frame, width=50, bg='white')
        self.entry_login.grid(row=4, column=1, pady=5)
        
        self.label_senha = tk.Label(self.frame, text="Senha:", bg='#B8D6F0', font=label_font)
        self.label_senha.grid(row=5, column=1, sticky='w', pady=10)
        
        self.entry_senha = tk.Entry(self.frame, width=50, bg='white')  
        self.entry_senha.grid(row=6, column=1)
        
        self.label_esqueci_senha= tk.Label(self.frame, text='Esqueci minha senha', font=label_font, bg='#B8D6F0', fg='blue', cursor='hand2')
        self.label_esqueci_senha.grid(row=7, column=1, pady=10, sticky='w')
        self.label_esqueci_senha.bind("<Button-1>", self.abrir_janela_cadastro)
    
    def abrir_janela_cadastro(self, event):
        # Função para abrir a janela de cadastro
        self.janela_cadastro = tk.Toplevel(self.root)
        app_cadastro = JanelaCadastro(self.janela_cadastro)
        
        
        

root = tk.Tk()
        
app = TelaLogin(root)
root.mainloop()


