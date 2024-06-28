import tkinter as tk
from tkinter import messagebox
import psycopg2

class CadastroUsuario:
    def __init__(self, root):
        self.root = root
        self.root.title("Cadastro de Usuário")

        self.frame = tk.Frame(self.root)
        self.frame.pack(padx=20, pady=20)

        self.label_nome = tk.Label(self.frame, text="Nome:")
        self.label_nome.grid(row=0, column=0, padx=5, pady=5)

        self.entry_nome = tk.Entry(self.frame)
        self.entry_nome.grid(row=0, column=1, padx=5, pady=5)

        self.label_cpf = tk.Label(self.frame, text="CPF:")
        self.label_cpf.grid(row=1, column=0, padx=5, pady=5)

        self.cpf_var = tk.StringVar()
        self.entry_cpf = tk.Entry(self.frame, textvariable=self.cpf_var)
        self.entry_cpf.grid(row=1, column=1, padx=5, pady=5)
       

        self.label_email = tk.Label(self.frame, text="Email:")
        self.label_email.grid(row=2, column=0, padx=5, pady=5)

        self.entry_email = tk.Entry(self.frame)
        self.entry_email.grid(row=2, column=1, padx=5, pady=5)

        self.label_senha = tk.Label(self.frame, text="Senha:")
        self.label_senha.grid(row=3, column=0, padx=5, pady=5)

        self.entry_senha = tk.Entry(self.frame, show="*")
        self.entry_senha.grid(row=3, column=1, padx=5, pady=5)

        self.btn_cadastrar = tk.Button(self.frame, text="Cadastrar", command=self.cadastrar_usuario)
        self.btn_cadastrar.grid(row=4, columnspan=2, padx=5, pady=5)

    
    def cadastrar_usuario(self):
        nome = self.entry_nome.get()
        cpf = self.entry_cpf.get().replace('.', '').replace('-', '')
        email = self.entry_email.get()
        senha = self.entry_senha.get()

        if not nome or not cpf or not email or not senha:
            messagebox.showerror("Erro", "Todos os campos devem ser preenchidos.")
            return

        try:
            # Conexão com o banco de dados PostgreSQL
            connection = psycopg2.connect(
                host="localhost",
                database="CADASTRO_USER",
                user="postgres",
                password="postgres",
                port="5432"
            )

            cursor = connection.cursor()

            # Verificação se o usuário já está cadastrado
            cursor.execute("SELECT cpf FROM cadastro_usuario WHERE cpf = %s", (cpf,))
            if cursor.fetchone():
                messagebox.showinfo("Usuário Existente", "Usuário já cadastrado com este CPF.")
                cursor.close()
                connection.close()
                return

            # Inserção dos dados do usuário no banco de dados
            cursor.execute("INSERT INTO cadastro_usuario (nome, cpf, email, senha) VALUES (%s, %s, %s, %s)", (nome, cpf, email, senha))
            connection.commit()

            messagebox.showinfo("Cadastro Efetuado", "Usuário cadastrado com sucesso!")

            # Fechar a conexão com o banco de dados
            cursor.close()
            connection.close()

        except (Exception, psycopg2.Error) as error:
            messagebox.showerror("Erro", f"Erro ao cadastrar usuário: {error}")

        self.limpar_campos()

    def limpar_campos(self):
        self.entry_nome.delete(0, tk.END)
        self.entry_cpf.delete(0, tk.END)
        self.entry_email.delete(0, tk.END)
        self.entry_senha.delete(0, tk.END)


if __name__ == "__main__":
    root = tk.Tk()

    # Cria a tabela "cadastro_usuario" no banco de dados se ela não existir
    try:
        connection = psycopg2.connect(
            host="localhost",
            database="CADASTRO_USER",
            user="postgres",
            password="postgres",
            port="5432"
        )

        cursor = connection.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS cadastro_usuario (
                id SERIAL PRIMARY KEY,
                nome VARCHAR(100) NOT NULL,
                cpf VARCHAR(11) NOT NULL UNIQUE,
                email VARCHAR(100) NOT NULL UNIQUE,
                senha VARCHAR(100) NOT NULL
            )
        """)

        connection.commit()

        cursor.close()
        connection.close()

    except (Exception, psycopg2.Error) as error:
        messagebox.showerror("Erro", f"Erro ao conectar ao banco de dados: {error}")

    # Executa a aplicação
    app = CadastroUsuario(root)
    root.mainloop()
