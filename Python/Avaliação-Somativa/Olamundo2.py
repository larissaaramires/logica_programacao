# Avaliação Somativa
# 1. Registro de Operador: Peça o nome do operador e o turno (A, B ou C). Exiba: "Operador [Nome] registrado no Turno [Turno]. Boa jornada!"

import tkinter as tk
from tkinter import messagebox, ttk

# janela = tk.Tk()
# janela.title('Registro de Operador')
# janela.geometry('500x500')
# janela.configure(bg='grey')

# def registrar_operador():
#     nome_operador = ent_nome_operador.get()
#     turno_operador= cmb_turno_operador.get()
#     if nome_operador == "" or turno_operador == "":
#         messagebox.showwarning('Verificar Dados', 'Verificar os campos')
#     else:
#         messagebox.showinfo('Bem-vindo!', f'Operador {nome_operador}, registrado no {turno_operador}. Boa jornada!')

# lbl_titulo_aplicacao = tk.Label(janela, text=('Olá operdor :)'),  font=('Arial', 14), bg='grey', fg='black')
# lbl_titulo_aplicacao.grid(row=0, column=0, pady=20, padx=20)
# lbl_nome_operador = tk.Label(janela, text=('Digite seu nome:'), font=('Arial', 12), bg='grey', fg='black')
# lbl_nome_operador.grid(row=1, column=0, pady=20, padx=20)
# lbl_turno_operador = tk.Label(janela, text=('Escolha seu turno:'), font=('Arial', 12), bg='grey', fg='black')
# lbl_turno_operador.grid(row=2, column=0, pady=20, padx=20)

# ent_nome_operador = tk.Entry(janela, font=('Arial', 12))
# ent_nome_operador.grid(row=1, column=1, pady=20, padx=20)

# cmb_turno_operador = ttk.Combobox(janela, values=['Turno A', 'Turno B', 'Turno C'], state='readonly', width=20, height=20)
# cmb_turno_operador.grid(row=2, column=1, pady=20, padx=20)

# btn_registro_operador = tk.Button(janela, text='Registrar operador', width=15, height=2, bg='light grey', command=registrar_operador)
# btn_registro_operador.grid(row=3, column=0, pady=20, padx=20)
# btn_fechar = tk.Button(janela, text='Fechar aplicativo', width=15, height=2, bg='light grey', command=janela.destroy)
# btn_fechar.grid(row=3, column=1, pady=20, padx=20)

# janela.mainloop()

############################################################################################################################################

# 2. Cálculo de Produção: Peça a quantidade de peças produzidas em 1 hora. Calcule e exiba quantas peças serão produzidas em um turno de 8 horas.

# janela = tk.Tk()
# janela.title('Cálculo de produção')
# janela.geometry('650x500')
# janela.configure(bg='grey')

# def calcular_pecas():
#     pecas_1hora = int(ent_pecas_1hora.get())
#     pecas_8horas = (pecas_1hora) * 8
#     if pecas_1hora == "":
#         messagebox.showwarning('Verificar Dados', 'Verificar os campos')
#     else:
#         messagebox.showinfo('Quantidade', f'Serão produzidas {pecas_8horas} peças, em um turno de 8 horas.')

# lbl_titulo_aplicacao = tk.Label(janela, text=('Calculador de podrução de 8 horas :)'), font=('Arial', 14), bg='grey', fg='black')
# lbl_titulo_aplicacao.grid(row=0, column=0, pady=20, padx=20)
# lbl_pecas_1hora = tk.Label(janela, text=('Digite a quantidade de peças produzidas em 1 hora:'), font=('Arial', 12), bg='grey', fg='black')
# lbl_pecas_1hora.grid(row=1, column=0, pady=20, padx=20)

# ent_pecas_1hora = tk.Entry(janela, font=('Arial', 12))
# ent_pecas_1hora.grid(row=1, column=1, pady=20, padx=20)

# btn_pecas_8horas = tk.Button(janela, text='Calcular produção', width=28, height=3, bg='light grey', command=calcular_pecas)
# btn_pecas_8horas.grid(row=3, column=0, pady=20, padx=20)
# btn_fechar = tk.Button(janela, text='Fechar aplicativo', width=28, height=3, bg='light grey', command=janela.destroy)
# btn_fechar.grid(row=3, column=1, pady=20, padx=20)

# janela.mainloop()

############################################################################################################################################

# 3. Conversor de Unidade: O sistema lê uma pressão em Bar. Converta para PSI (1 Bar ≈ 14.5 PSI) e exiba com duas casas decimais.

# janela = tk.Tk()
# janela.title('Conversor de unidade')
# janela.geometry('650x500')
# janela.configure(bg='grey')

# def converter_pressao():
#     pressao = float(ent_pressao.get())
#     pressao_convertida = pressao * 14.5
#     if pressao == "":
#         messagebox.showwarning('Verificar Dados', 'Verificar os campos')
#     else:
#         messagebox.showinfo('Pressão convertida', f'A pressão convertida é de {pressao_convertida:.2f} PSI.')

# lbl_titulo_aplicacao = tk.Label(janela, text=('Convertendo pressão para PSI :)'), font=('Arial', 14), bg='grey', fg='black')
# lbl_titulo_aplicacao.grid(row=0, column=0, pady=20, padx=20)
# lbl_pressao = tk.Label(janela, text=('Digite a pressão:'), font=('Arial', 12), bg='grey', fg='black')
# lbl_pressao.grid(row=1, column=0, pady=20, padx=20)

# ent_pressao = tk.Entry(janela, font=('Arial', 12))
# ent_pressao.grid(row=1, column=1, pady=20, padx=20)

# btn_pressao_convertida = tk.Button(janela, text='Converter pressão', width=28, height=3, bg='light grey', command=converter_pressao)
# btn_pressao_convertida.grid(row=3, column=0, pady=20, padx=20)
# btn_fechar = tk.Button(janela, text='Fechar aplicativo', width=28, height=3, bg='light grey', command=janela.destroy)
# btn_fechar.grid(row=3, column=1, pady=20, padx=20)

# janela.mainloop()

############################################################################################################################################

# 4. Média de Qualidade: Peça 3 notas de inspeção de uma peça (0 a 10). Exiba a média aritmética simples delas.

# janela = tk.Tk()
# janela.title('Média de qualidade')
# janela.geometry('600x500')
# janela.configure(bg='grey')

# def calcular_media():
#     nota1 = float(ent_nota1.get())
#     nota2 = float(ent_nota2.get())
#     nota3 = float(ent_nota3.get())
#     notas1e2 = nota1 + nota2
#     total_notas = notas1e2 + nota3
#     media = total_notas / 3
#     if nota1 == "" or nota2 == "" or nota3 == "":
#         messagebox.showwarning('Verificar Dados', 'Verificar os campos')
#     else:
#         messagebox.showinfo('Média Aritmétrica', f'A média aritmétrica simples das notas é {media}.')

# lbl_titulo_aplicacao = tk.Label(janela, text=('Calculador de média aritmétrica :)'), font=('Arial', 14), bg='grey', fg='black')
# lbl_titulo_aplicacao.grid(row=0, column=0, pady=20, padx=20)
# lbl_nota1 = tk.Label(janela, text=('Digite a primeira nota:'), font=('Arial', 12), bg='grey', fg='black')
# lbl_nota1.grid(row=1, column=0, pady=20, padx=20)
# lbl_nota2 = tk.Label(janela, text=('Digite a segunda nota:'), font=('Arial', 12), bg='grey', fg='black')
# lbl_nota2.grid(row=2, column=0, pady=20, padx=20)
# lbl_nota3 = tk.Label(janela, text=('Digite a terceira nota:'), font=('Arial', 12), bg='grey', fg='black')
# lbl_nota3.grid(row=3, column=0, pady=20, padx=20)

# ent_nota1 = tk.Entry(janela, font=('Arial', 12))
# ent_nota1.grid(row=1, column=1, pady=20, padx=20)
# ent_nota2 = tk.Entry(janela, font=('Arial', 12))
# ent_nota2.grid(row=2, column=1, pady=20, padx=20)
# ent_nota3 = tk.Entry(janela, font=('Arial', 12))
# ent_nota3.grid(row=3, column=1, pady=20, padx=20)

# btn_calcular_media = tk.Button(janela, text='Calcular Média', width=28, height=3, bg='light grey', command=calcular_media)
# btn_calcular_media.grid(row=4, column=0, pady=20, padx=20)
# btn_fechar = tk.Button(janela, text='Fechar aplicativo', width=28, height=3, bg='light grey', command=janela.destroy)
# btn_fechar.grid(row=4, column=1, pady=20, padx=20)

# janela.mainloop()

############################################################################################################################################

# 5. Termostato Inteligente: Peça a temperatura de um motor.
# ● Abaixo de 40°C: "Baixa carga".
# ● Entre 40°C e 70°C: "Normal".
# ● Acima de 70°C: "ALERTA: Resfriamento Ativado!".

# janela = tk.Tk()
# janela.title('Termostato Inteligente')
# janela.geometry('500x500')
# janela.configure(bg='grey')

# def ver_status():
#     temperatura = float(ent_temperatura_motor.get())
#     if temperatura > 70:
#         messagebox.showwarning('Temperatura do motor', 'ALERTA: Resfriamento Ativado!')
#     elif temperatura < 40:
#         messagebox.showinfo('Temperatura do motor', 'Status da tempetatura: Baixa carga')
#     elif temperatura >= 40:
#         messagebox.showinfo('Temperatura do motor', 'Status da tempetatura: Normal')
#     else:
#         messagebox.showwarning('Verificar Dados', 'Verificar os campos')

# lbl_titulo_aplicacao = tk.Label(janela, text=('Temperatura do motor :)'), font=('Arial', 14), bg='grey', fg='black')
# lbl_titulo_aplicacao.grid(row=0, column=0, pady=20, padx=20)
# lbl_temperatura_motor = tk.Label(janela, text=('Digite a temperatura:'), font=('Arial', 12), bg='grey', fg='black')
# lbl_temperatura_motor.grid(row=1, column=0, pady=20, padx=20)

# ent_temperatura_motor = tk.Entry(janela, font=('Arial', 12))
# ent_temperatura_motor.grid(row=1, column=1, pady=20, padx=20)

# btn_status_temperatura = tk.Button(janela, text='Status da temperatura', width=28, height=3, bg='light grey', command=ver_status)
# btn_status_temperatura.grid(row=2, column=0, pady=20, padx=20)
# btn_fechar = tk.Button(janela, text='Fechar aplicativo', width=28, height=3, bg='light grey', command=janela.destroy)
# btn_fechar.grid(row=2, column=1, pady=20, padx=20)

# janela.mainloop()

############################################################################################################################################

# 6. Classificador de Lotes: O usuário insere o código do produto. Se começar com "A", exiba "Alimentos". Se "E", "Eletrônicos". Para qualquer outro, "Desconhecido".

# janela = tk.Tk()
# janela.title('Classificador de Lotes')
# janela.geometry('650x500')
# janela.configure(bg='grey')

# def ver_produto():
#     codigo_produto = cmb_codigo_produto.get()
#     if codigo_produto == 'Outra':
#         messagebox.showinfo('Código do produto', 'Esse produto é desconhecido')
#     elif codigo_produto == 'Letra A':
#         messagebox.showinfo('Código do produto', 'Esse produto se classifica como: Alimentos')
#     elif codigo_produto == 'Letra E':
#         messagebox.showinfo('Código do produto', 'Esse produto se classifica como: Eletrônicos')
#     else:
#         messagebox.showwarning('Verificar Dados', 'Verificar os campos')

# lbl_titulo_aplicacao = tk.Label(janela, text=('Classificando lotes :)'), font=('Arial', 14), bg='grey', fg='black')
# lbl_titulo_aplicacao.grid(row=0, column=0, pady=20, padx=20)
# lbl_codigo_produto = tk.Label(janela, text=('Escolha a letra que o código do produto começa:'), font=('Arial', 12), bg='grey', fg='black')
# lbl_codigo_produto.grid(row=1, column=0, pady=20, padx=20)

# cmb_codigo_produto = ttk.Combobox(janela, values=['Letra A', 'Letra E', 'Outra'], state='readonly', width=20, height=20)
# cmb_codigo_produto.grid(row=1, column=1, pady=20, padx=20)

# btn_ver_produto = tk.Button(janela, text='Ver produto', width=28, height=3, bg='light grey', command=ver_produto)
# btn_ver_produto.grid(row=2, column=0, pady=20, padx=20)
# btn_fechar = tk.Button(janela, text='Fechar aplicativo', width=28, height=3, bg='light grey', command=janela.destroy)
# btn_fechar.grid(row=2, column=1, pady=20, padx=20)

# janela.mainloop()

############################################################################################################################################

# 7. Segurança de Operação: A máquina só liga se o sensor_porta == "fechada" E o botao_emergencia == "desligado". Peça esses dois inputs e diga se a máquina pode iniciar.

# janela = tk.Tk()
# janela.title('Segurança de Operação')
# janela.geometry('650x500')
# janela.configure(bg='grey')

# def ver_seguranca():
#     porta = cmb_sensor_porta.get()
#     botao_emergencia = cmb_botao_emergencia.get()
#     if porta == "" or botao_emergencia == "":
#         messagebox.showwarning('Verificar Dados', 'Verificar os campos')
#     elif porta == 'Aberta' and botao_emergencia == 'Desligado':
#         messagebox.showwarning('Verificar segurança', 'Fechar a porta para que a máquina possa iniciar!')
#     elif porta == 'Fechada' and botao_emergencia == 'Ligado':
#         messagebox.showwarning('Verificar segurança', 'Desligar o botão de emergência para que a máquina possa iniciar!')
#     elif porta == 'Aberta' and botao_emergencia == 'Ligado':
#         messagebox.showwarning('Verificar segurança', 'Fechar a porta e desligar o botão de emergência para que a máquina possa iniciar!')
#     else:
#         messagebox.showinfo('Verificar segurança', 'Tudo certo, a máquina pode iniciar.')


# lbl_titulo_aplicacao = tk.Label(janela, text=('Segurança de Operação :)'), font=('Arial', 14), bg='grey', fg='black')
# lbl_titulo_aplicacao.grid(row=0, column=0, pady=20, padx=20)
# lbl_sensor_porta = tk.Label(janela, text=('Como a porta está:'), font=('Arial', 12), bg='grey', fg='black')
# lbl_sensor_porta.grid(row=1, column=0, pady=20, padx=20)
# lbl_botao_emergencia = tk.Label(janela, text=('Como o botão de emergência está:'), font=('Arial', 12), bg='grey', fg='black')
# lbl_botao_emergencia.grid(row=2, column=0, pady=20, padx=20)

# cmb_sensor_porta = ttk.Combobox(janela, values=['Aberta', 'Fechada'], state='readonly', width=20, height=20)
# cmb_sensor_porta.grid(row=1, column=1, pady=20, padx=20)
# cmb_botao_emergencia = ttk.Combobox(janela, values=['Ligado', 'Desligado'], state='readonly', width=20, height=20)
# cmb_botao_emergencia.grid(row=2, column=1, pady=20, padx=20)

# btn_ver_seguranca = tk.Button(janela, text='Ver segurança', width=28, height=3, bg='light grey', command=ver_seguranca)
# btn_ver_seguranca.grid(row=3, column=0, pady=20, padx=20)
# btn_fechar = tk.Button(janela, text='Fechar aplicativo', width=28, height=3, bg='light grey', command=janela.destroy)
# btn_fechar.grid(row=3, column=1, pady=20, padx=20)

# janela.mainloop()

############################################################################################################################################

# 8. Cálculo de Descarte: Peça o total de peças produzidas e o total de defeituosas. Se o descarte for maior que 5% do total, exiba "Revisar Processo", caso contrário, "Processo Otimizado".

# janela = tk.Tk()
# janela.title('Cálculo de Descarte')
# janela.geometry('650x500')
# janela.configure(bg='grey')

# def calcular_descarte():
#     pecas_produzidas = int(ent_pecas_produzidas.get())
#     pecas_defeituosas = int(ent_pecas_defeituosas.get())
#     total_pecas_defeituosas = (pecas_defeituosas * pecas_produzidas) / 100
#     if  pecas_produzidas == "" or pecas_defeituosas == "":
#         messagebox.showwarning('Verificar Dados', 'Verificar os campos')
#     elif total_pecas_defeituosas > 5:
#         messagebox.showwarning('Calcular descarte', 'O descarte foi maior do que 5%. Revisar Processo')
#     else:
#         messagebox.showinfo('Calcular descarte', 'O descarte foi menor do que 5%. Processo Otimizado')


# lbl_titulo_aplicacao = tk.Label(janela, text=('Peças defeituosas :)'), font=('Arial', 14), bg='grey', fg='black')
# lbl_titulo_aplicacao.grid(row=0, column=0, pady=20, padx=20)
# lbl_pecas_produzidas = tk.Label(janela, text=('Digite o total de peças produzidas:'), font=('Arial', 12), bg='grey', fg='black')
# lbl_pecas_produzidas.grid(row=1, column=0, pady=20, padx=20)
# lbl_pecas_defeituosas = tk.Label(janela, text=('Digite o total de defeituosas:'), font=('Arial', 12), bg='grey', fg='black')
# lbl_pecas_defeituosas.grid(row=2, column=0, pady=20, padx=20)

# ent_pecas_produzidas = tk.Entry(janela, font=('Arial', 12))
# ent_pecas_produzidas.grid(row=1, column=1, pady=20, padx=20)
# ent_pecas_defeituosas = tk.Entry(janela, font=('Arial', 12))
# ent_pecas_defeituosas.grid(row=2, column=1, pady=20, padx=20)

# btn_calcular_descarte = tk.Button(janela, text='Calcular descarte', width=28, height=3, bg='light grey', command=calcular_descarte)
# btn_calcular_descarte.grid(row=3, column=0, pady=20, padx=20)
# btn_fechar = tk.Button(janela, text='Fechar aplicativo', width=28, height=3, bg='light grey', command=janela.destroy)
# btn_fechar.grid(row=3, column=1, pady=20, padx=20)

# janela.mainloop()

############################################################################################################################################

# 9. Validação de Medida: Uma peça deve ter entre 9.8mm e 10.2mm. Peça a medida e diga se está dentro da tolerância, acima ou abaixo.

# janela = tk.Tk()
# janela.title('Validação de Medida')
# janela.geometry('600x500')
# janela.configure(bg='grey')

# def validando_medida():
#     medida = float(ent_medida_pecas.get())
#     if medida == "":
#         messagebox.showwarning('Verificar Dados', 'Verificar os campos')
#     elif medida >= 9.8 and medida <= 10.2:
#         messagebox.showinfo("Validando medida", 'A medida está dentro da tolerância')
#     elif medida < 9.8:
#         messagebox.showwarning('Validando medida', 'A medida está abaixo da tolerância')
#     else:
#         messagebox.showwarning('Validando medida', 'A medida está acima da tolerância')


# lbl_titulo_aplicacao = tk.Label(janela, text=('Medidas :)'), font=('Arial', 14), bg='grey', fg='black')
# lbl_titulo_aplicacao.grid(row=0, column=0, pady=20, padx=20)
# lbl_medida_pecas = tk.Label(janela, text=('Digite a medida da peça em mm:'), font=('Arial', 12), bg='grey', fg='black')
# lbl_medida_pecas.grid(row=1, column=0, pady=20, padx=20)

# ent_medida_pecas = tk.Entry(janela, font=('Arial', 12))
# ent_medida_pecas.grid(row=1, column=1, pady=20, padx=20)

# btn_validando_medida = tk.Button(janela, text='Validando medida', width=28, height=3, bg='light grey', command=validando_medida)
# btn_validando_medida.grid(row=3, column=0, pady=20, padx=20)
# btn_fechar = tk.Button(janela, text='Fechar aplicativo', width=28, height=3, bg='light grey', command=janela.destroy)
# btn_fechar.grid(row=3, column=1, pady=20, padx=20)

# janela.mainloop()

############################################################################################################################################

# 10. Contagem Regressiva de Setup: Use um for para fazer uma contagem regressiva de 10 até 1 para o início de uma prensa, e finalize com "Prensa Ativada!".

def contagem_regressiva():
    for i in range (10, 0, -1):
        messagebox.showinfo("Contagem regressiva", (i))

janela = tk.Tk()
janela.title('Contagem Regressiva de Setup')
janela.geometry('600x500')
janela.configure(bg='grey')

lbl_titulo_aplicacao = tk.Label(janela, text=('Contagem regressiva :)'), font=('Arial', 14), bg='grey', fg='black')
lbl_titulo_aplicacao.grid(row=0, column=0, pady=20, padx=20)

btn_contagem_regressiva = tk.Button(janela, text='Fazer contagem', width=28, height=3, bg='light grey', command=contagem_regressiva)
btn_contagem_regressiva.grid(row=3, column=0, pady=20, padx=20)
btn_fechar = tk.Button(janela, text='Fechar aplicativo', width=28, height=3, bg='light grey', command=janela.destroy)
btn_fechar.grid(row=3, column=1, pady=20, padx=20)

janela.mainloop()