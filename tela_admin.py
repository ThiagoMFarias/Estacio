import tkinter as tk
from tkinter import messagebox
from cadastro_novo_usuario_v02 import AddNewUser

class Dashboard:
    def __init__(self, root, user_role):
        self.root = root
        self.root.title('Painel de Controle')
        self.root.resizable(width=False, height=False)
             
        # Adicionar evento de fechamento personalizado
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)   
        
        # Centralizar janela na tela
        self.centralizar_janela(300, 200)
        
        # Exemplo de menu para administrador        
        if user_role[0] == 'Administrador':
            self.create_admin_menu()
            
    def centralizar_janela(self, largura, altura):
        largura_tela = self.root.winfo_screenwidth()
        altura_tela = self.root.winfo_screenheight()   
        x = (largura_tela - largura) //2
        y = (altura_tela - altura) // 2
        self.root.geometry(f'{largura}x{altura}+{x}+{y}')
            
    def on_closing(self):
        if messagebox.askokcancel("Sair", "Você tem certeza que deseja sair?"):
            self.root.destroy()
            self.root.quit()
        
    def create_admin_menu(self):
        menu = tk.Menu(self.root)
        self.root.config(menu=menu)
                
        user_menu = tk.Menu(menu, tearoff = False)
        menu.add_cascade(label="Usuários", menu=user_menu)
        user_menu.add_command(label="Adicionar Usuário", command=self.add_user)
        user_menu.add_command(label="Gerenciar Usuários", command=self.manage_users)
        
        class_menu = tk.Menu(menu, tearoff = False)
        menu.add_cascade(label="Turmas", menu=class_menu)
        class_menu.add_command(label="Adicionar Turma", command=self.add_class)
        class_menu.add_command(label="Gerenciar Turmas", command=self.manage_classes)
        
        subject_menu = tk.Menu(menu, tearoff = False)
        menu.add_cascade(label="Disciplinas", menu=subject_menu)
        subject_menu.add_command(label="Adicionar Disciplina", command=self.add_subject)
        subject_menu.add_command(label="Gerenciar Disciplinas", command=self.manage_subjects)
        
    def add_user(self):
        AddNewUser(self.root)

    def manage_users(self):
        messagebox.showinfo("Gerenciar Usuários", "Funcionalidade de Gerenciar Usuários")

    def add_class(self):
        messagebox.showinfo("Adicionar Turma", "Funcionalidade de Adicionar Turma")

    def manage_classes(self):
        messagebox.showinfo("Gerenciar Turmas", "Funcionalidade de Gerenciar Turmas")

    def add_subject(self):
        messagebox.showinfo("Adicionar Disciplina", "Funcionalidade de Adicionar Disciplina")

    def manage_subjects(self):
        messagebox.showinfo("Gerenciar Disciplinas", "Funcionalidade de Gerenciar Disciplinas")

    def record_grades(self):
        messagebox.showinfo("Registrar Notas", "Funcionalidade de Registrar Notas")

    def view_grades(self):
        messagebox.showinfo("Visualizar Notas", "Funcionalidade de Visualizar Notas")

    def view_subjects(self):
        messagebox.showinfo("Minhas Disciplinas", "Funcionalidade de Visualizar Minhas Disciplinas")

if __name__ == "__main__":
    root = tk.Tk()
    #user_role = ['Administrador']  # Tenho que excluir essa linha quando for colocar para produção.
    app = Dashboard(root, user_role= 'Administrador')  # Tenho que alterar isso para 'Administrador' quando for colocar em produção
    root.mainloop()
