import tkinter as tk
from tkinter import messagebox



class Dashboard:
    def __init__(self, root, user_role):
        self.root = root
        self.root.geometry('600x400')
        self.root.title('Painel de Controle')
        self.root.resizable(width=False, height=False)
        
        # Exemplo de menu para administrador
        
        if user_role[0] == 'Administrador':
            self.create_admin_menu()
        elif user_role == 'professor':
            self.create_teacher_menu()
        elif user_role == 'aluno':
            self.create_student_menu()

    def create_admin_menu(self):
        menu = tk.Menu(self.root)
        self.root.config(menu=menu)
        
        user_menu = tk.Menu(menu)
        menu.add_cascade(label="Usuários", menu=user_menu)
        user_menu.add_command(label="Adicionar Usuário", command=self.add_user)
        user_menu.add_command(label="Gerenciar Usuários", command=self.manage_users)
        
        class_menu = tk.Menu(menu)
        menu.add_cascade(label="Turmas", menu=class_menu)
        class_menu.add_command(label="Adicionar Turma", command=self.add_class)
        class_menu.add_command(label="Gerenciar Turmas", command=self.manage_classes)
        
        subject_menu = tk.Menu(menu)
        menu.add_cascade(label="Disciplinas", menu=subject_menu)
        subject_menu.add_command(label="Adicionar Disciplina", command=self.add_subject)
        subject_menu.add_command(label="Gerenciar Disciplinas", command=self.manage_subjects)

    def create_teacher_menu(self):
        menu = tk.Menu(self.root)
        self.root.config(menu=menu)
        
        grade_menu = tk.Menu(menu)
        menu.add_cascade(label="Notas", menu=grade_menu)
        grade_menu.add_command(label="Registrar Notas", command=self.record_grades)
        grade_menu.add_command(label="Visualizar Notas", command=self.view_grades)

    def create_student_menu(self):
        menu = tk.Menu(self.root)
        self.root.config(menu=menu)
        
        menu.add_command(label="Minhas Notas", command=self.view_grades)
        menu.add_command(label="Minhas Disciplinas", command=self.view_subjects)

    def add_user(self):
        messagebox.showinfo("Adicionar Usuário", "Funcionalidade de Adicionar Usuário")

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
    app = Dashboard(root, user_role='Administrador')  # Pode ser 'admin', 'teacher', ou 'student'
    root.mainloop()
