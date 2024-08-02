import tkinter as tk
from tkinter import messagebox, ttk


class AddNewUser:
    def __init__(self, root):
        self.root = root
        self.root.title("Adicionar Usuário")
        self.root.geometry('400x400')
        self.root.resizable(width=True, height=True)
        
        # Chame o método para criar os frames
        self.frames_da_tela()
    
    def frames_da_tela(self):
        # Crie e posicione o frame dentro da janela
        self.frame_1 = tk.Frame(self.root, bg='#B8D6F0')
        self.frame_1.place(relx=0.05, rely=0.1, relwidth=0.9, relheight=0.8)
        
        
        tk.Label(self.root, text="Nome:").grid(row=0, column=0, padx=10, pady=10, sticky='w')
        self.entry_nome = tk.Entry(self.root)
        self.entry_nome.grid(row=0, column=1, padx=10, pady=10)
        
        """ tk.Label(self.root, text="CPF:").grid(row=1, column=0, padx=10, pady=10, sticky='w')
        self.entry_cpf = tk.Entry(self.root)
        self.entry_cpf.grid(row=1, column=1, padx=10, pady=10)
        
        tk.Label(self.root, text="Tipo de Perfil:").grid(row=2, column=0, padx=10, pady=10, sticky='w')
        self.combo_perfil = ttk.Combobox(self.root, values=["Administrador", "Professor", "Aluno"])
        self.combo_perfil.grid(row=2, column=1, padx=10, pady=10)
        
        tk.Label(self.root, text="Data de Nascimento:").grid(row=3, column=0, padx=10, pady=10, sticky='w')
        self.entry_nascimento = tk.Entry(self.root)
        self.entry_nascimento.grid(row=3, column=1, padx=10, pady=10)
        
        tk.Label(self.root, text="Sexo:").grid(row=4, column=0, padx=10, pady=10, sticky='w')
        self.combo_sexo = ttk.Combobox(self.root, values=["Masculino", "Feminino", "Outro"])
        self.combo_sexo.grid(row=4, column=1, padx=10, pady=10)
        
        tk.Label(self.root, text="Endereço:").grid(row=5, column=0, padx=10, pady=10, sticky='w')
        self.entry_endereco = tk.Entry(self.root)
        self.entry_endereco.grid(row=5, column=1, padx=10, pady=10)
        
        tk.Label(self.root, text="E-mail:").grid(row=6, column=0, padx=10, pady=10, sticky='w')
        self.entry_email = tk.Entry(self.root)
        self.entry_email.grid(row=6, column=1, padx=10, pady=10)
        
        tk.Button(self.root, text="Salvar", command=self.salvar_usuario).grid(row=7, column=0, columnspan=2, pady=20) """
        
    def salvar_usuario(self):
        nome = self.entry_nome.get()
        cpf = self.entry_cpf.get()
        perfil = self.combo_perfil.get()
        nascimento = self.entry_nascimento.get()
        sexo = self.combo_sexo.get()
        endereco = self.entry_endereco.get()
        email = self.entry_email.get()
        
        if not all([nome, cpf, perfil, nascimento, sexo, endereco, email]):
            messagebox.showerror("Erro", "Todos os campos são obrigatórios!")
            return
        
        # Aqui você pode adicionar o código para salvar os dados em um banco de dados ou arquivo
        
        messagebox.showinfo("Sucesso", f"Usuário {nome} cadastrado com sucesso!")
        self.root.destroy()
        
if __name__ == "__main__":
    root = tk.Tk()
    app = AddNewUser(root)
    root.mainloop()
        