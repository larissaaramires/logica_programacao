# Revisão Tkinter

# Biclioteca
import tkinter as tk
from tkinter import messagebox, ttk

# DEF - Linha de bloco de fução
def cadastrar_usuario():
    # .get em todos os comandos que irão receber informação

    nome_usuario = ent_nome_usuario.get()
    nome_escola = cmb_nome_escola.get()

    if nome_usuario == "" or nome_escola == "":
        messagebox.showwarning('Verificar Dados', 'Verificar os campos')
    else:
        messagebox.showinfo('Bem-vindo', f'Olá usuário {nome_usuario}, você estuda no {nome_escola}')

# 0 Etapas - Janela
janela = tk.Tk()
janela.title('Revisão Tkinder')
janela.geometry('500x500')
janela.configure(bg='grey')

# 1 Etapa - Componentes
# Labels = Rotulos e Textos antigo print
lbl_titulo_aplicacao = tk.Label(janela, text="Revisão Tkinter :)", font=('Arial', 14), fg='black', bg='grey')
lbl_titulo_aplicacao.grid(row=0, column=0, pady=20, padx=20)

lbl_nome_usuario = tk.Label(janela, text="Digite seu nome:", font=('Arial', 12), fg='black', bg='grey')
lbl_nome_usuario.grid(row=1, column=0, pady=20, padx=20)

lbl_nome_escola = tk.Label(janela, text='Escolha sua escola:', font=('Arial', 12), fg='black', bg='grey')
lbl_nome_escola.grid(row=2, column=0, pady=10, padx=10)


# Entrys = Caixa de texto ou antigo input
ent_nome_usuario = tk.Entry(janela, font=('Arial', 12))
ent_nome_usuario.grid(row=1, column=1, pady=20, padx=20)


# Caixa de seleção ou combobox
cmb_nome_escola = ttk.Combobox(janela, values=['SESI 5', 'SESI 408'], state='readonly' ,width=20, height=20)
cmb_nome_escola.grid(row=2, column=1, pady=10, padx=10)


# Botões
btn_enviar_dados = tk.Button(janela, text='Cadastrar Usuário', width=15, height=2, bg='light grey', command=cadastrar_usuario)
btn_enviar_dados.grid(row=3, column=0, pady=20, padx=20)

btn_fechar = tk.Button(janela, text='Fechar aplicativo', width=15, height=2, bg='light grey', command=janela.destroy)
btn_fechar.grid(row=3, column=1, pady=20, padx=20)

# 4 Etapa - Mainloop
janela.mainloop()