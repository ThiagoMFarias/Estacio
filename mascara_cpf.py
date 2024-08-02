import tkinter as tk
from tkinter import messagebox
import re

# Função para validar o formato do CPF
def validar_cpf(cpf):
    padrao = r'^\d{3}\.\d{3}\.\d{3}-\d{2}$'
    if re.match(padrao, cpf):
        return True
    else:
        return False

# Função para capturar os dados e exibir uma mensagem de confirmação
def cadastrar():
    nome = entry_nome.get()
    cpf = entry_cpf.get()
    email = entry_email.get()
    senha = entry_senha.get()

    if not nome or not cpf or not email or not senha:
        messagebox.showerror("Erro", "Todos os campos são obrigatórios!")
        return

    if not validar_cpf(cpf):
        messagebox.showerror("Erro", "CPF inválido! O formato correto é 000.000.000-00.")
        return

    # Aqui você pode adicionar o código para salvar os dados em um banco de dados ou arquivo
    messagebox.showinfo("Sucesso", f"Usuário {nome} cadastrado com sucesso!")

# Função para limitar a entrada no campo CPF
def limitar_cpf(entry):
    texto = entry.get()
    if not re.match(r'^[\d.-]*$', texto):
        entry.set(texto[:-1])

# Função para formatar o CPF automaticamente
def formatar_cpf(event=None):
    texto = entry_cpf.get()
    texto = re.sub(r'\D', '', texto)  # Remove tudo que não for número
    novo_texto = ''
    
    if len(texto) > 0:
        novo_texto += texto[0:3]
    if len(texto) > 3:
        novo_texto += '.' + texto[3:6]
    if len(texto) > 6:
        novo_texto += '.' + texto[6:9]
    if len(texto) > 9:
        novo_texto += '-' + texto[9:11]

    entry_cpf.delete(0, tk.END)
    entry_cpf.insert(0, novo_texto)

# Criação da janela principal
root = tk.Tk()
root.title("Cadastro de Usuário")

# Nome
tk.Label(root, text="Nome:").grid(row=0, column=0, padx=10, pady=10)
entry_nome = tk.Entry(root)
entry_nome.grid(row=0, column=1, padx=10, pady=10)

# CPF
tk.Label(root, text="CPF:").grid(row=1, column=0, padx=10, pady=10)
cpf_var = tk.StringVar()
entry_cpf = tk.Entry(root, textvariable=cpf_var)
entry_cpf.grid(row=1, column=1, padx=10, pady=10)
entry_cpf.bind('<KeyRelease>', formatar_cpf)

# E-mail
tk.Label(root, text="E-mail:").grid(row=2, column=0, padx=10, pady=10)
entry_email = tk.Entry(root)
entry_email.grid(row=2, column=1, padx=10, pady=10)

# Senha
tk.Label(root, text="Senha:").grid(row=3, column=0, padx=10, pady=10)
entry_senha = tk.Entry(root, show='*')
entry_senha.grid(row=3, column=1, padx=10, pady=10)

# Botão Cadastrar
btn_cadastrar = tk.Button(root, text="Cadastrar", command=cadastrar)
btn_cadastrar.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

# Inicia o loop principal da aplicação
root.mainloop()