import tkinter as tk

class CadastroUsuario:
    def __init__(self, root):
        self.root = root
        self.root.title('Cadastro de Usuário')

        self.frame = tk.Frame(self.root)
        self.frame.pack(padx=300, pady=300)

        self.label_nome = tk.Label(self.frame, text="Nome:")
        self.label_nome.grid(row=0, column=0, padx=5, pady=5)

        self.nome_text = tk.StringVar()
        self.trace_id = self.nome_text.trace_add("write", self.converter_para_maiusculas)

        self.entry_nome = tk.Entry(self.frame, textvariable=self.nome_text, width=50)
        self.entry_nome.grid(row=0, column=1, padx=5, pady=5)
        
        self.label_cpf = tk.Label(self.frame, text="CPF:")
        self.label_cpf.grid(row=1, column=0, padx=5, pady=5)
        
        self.entry_cpf = tk.Entry(self.frame, width=50)
        self.entry_cpf.grid(row=1, column=1, padx=5, pady=5)

    def converter_para_maiusculas(self, *args):
        # Obtém o texto atual
        nome = self.nome_text.get()
        # Converte o texto para maiúsculas
        nome_maiusculas = nome.upper()
        # Desativa o trace temporariamente para evitar loop infinito
        self.nome_text.trace_remove("write", self.trace_id)
        # Atualiza o conteúdo da StringVar com o texto em maiúsculas
        self.nome_text.set(nome_maiusculas)
        # Reativa o trace
        self.trace_id = self.nome_text.trace_add("write", self.converter_para_maiusculas)

        
if __name__ == "__main__":
    root = tk.Tk()      
app = CadastroUsuario(root)
root.mainloop()