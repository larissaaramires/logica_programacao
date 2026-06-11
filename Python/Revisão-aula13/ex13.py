# Exercício
# Crie uma aplicação que pergunte o nome e o ano de nascimento do usuário
# Calcule a idade

import tkinter as tk
from tkinter import messagebox, ttk

# Biblioteca
janela = tk.Tk()
janela.title('Calcular Idade')
janela.geometry('500x500')
janela.configure(bg='grey')

# DEF 
def calcular_idade():
    try:
        nome_usuario = ent_nome_usuario.get()
        idade_usuario = int(ent_idade_usuario.get())
        ano_atual = int(ent_ano_atual.get())
        idade_atual = (ano_atual - idade_usuario)

    except ValueError:
        if nome_usuario == "" or idade_usuario == "" or ano_atual == "":
            messagebox.showwarning('Verificar Dados', 'Verificar os campos')
        else:
            messagebox.showinfo('Bem-vindo', f'Olá usuário {nome_usuario}, você tem {idade_atual} anos')

#Labels
lbl_titulo_janela = tk.Label(janela, text="Olá usuário :)", font=('Arial', 14), fg='black', bg='grey')
lbl_titulo_janela.grid(row=0, column=0, pady=20, padx=20)

lbl_nome_usuario = tk.Label(janela, text="Digite seu nome:", font=('Arial', 12), fg='black', bg='grey')
lbl_nome_usuario.grid(row=1, column=0, pady=20, padx=20)

lbl_idade_usuario = tk.Label(janela, text="Digite o ano que você nasceu:", font=('Arial', 12), fg='black', bg='grey')
lbl_idade_usuario.grid(row=2, column=0, pady=20, padx=20)

lbl_ano_atual = tk.Label(janela, text="Digite o ano atual:", font=('Arial', 12), fg='black', bg='grey')
lbl_ano_atual.grid(row=3, column=0, pady=20, padx=20)

# Entrys 
ent_nome_usuario = tk.Entry(janela, font=('Arial', 12))
ent_nome_usuario.grid(row=1, column=1, pady=20, padx=20)

ent_idade_usuario = tk.Entry(janela, font=('Arial', 12))
ent_idade_usuario.grid(row=2, column=1, pady=20, padx=20)

ent_ano_atual = tk.Entry(janela, font=('Arial', 12))
ent_ano_atual.grid(row=3, column=1, pady=20, padx=20)

# Botões
btn_calcular = tk.Button(janela, text='Calcular idade', width=15, height=2, bg='light grey', command=calcular_idade)
btn_calcular.grid(row=4, column=0, pady=20, padx=20)

btn_fechar = tk.Button(janela, text='Fechar aplicativo', width=15, height=2, bg='light grey', command=janela.destroy)
btn_fechar.grid(row=4, column=1, pady=20, padx=20)

# Mainloop
janela.mainloop()