# 1. O laço 'for' (Repetições Determinadas)
# Use o 'for' quando você sabe exatamente quantas vezes algo deve acontecer (como ler 10 sensores ou processar uma lista de peças).
# Exemplo: Relatório de Produção Diária
# Imagine que você tem uma meta de produzir 5 lotes e quer numerar cada um:

# Exemplo 1
for lote in range(1, 6):
   print(f"Processando lote número {lote}...")
   print("Qualidade verificada. {OK}")
   print("Produção do dia finalizada!")

# Exemplo 2
# Imagine que você queira atingir uma meta de produção de 5 carros e numera-los
for carros in range(1, 6):
   print(f"Produção de carros diária {carros}...")

# Exemplo 3 
# Contar até 4
for i in range(5):
   print(i)

# Exemplo 4
pecas = ["Engrenagem", "Eixo", "Rolamento", "Parafuso", "Martelo"]
tipo = ["Barra Dentada", "Porca do Eixo", "Anel Externo", "Parafuso phillips", "Martelo cabeça chata"]

for item in pecas:
    print(f"Item em estoque: {item}")
    for n1 in tipo:
     print(f"Os tipos de peças em estoque são: {tipo}")

# Exemplo 5 
# Imagine a seguinte situação: gostaria de ter um menu onde pudesse perguntar qual opção você deseja a partir da seleção ele listar os produtos

pecas = ["Engrenagem", "Eixo", "Rolamento", "Parafuso", "Martelo"]
tipo = ["Barra Dentada", "Porca do Eixo", "Anel Externo", "Parafuso phillips", "Martelo cabeça chata"]

print('Loja de peças da Larissa')
print('Bem-vindo ao nosso sistema')
print('Escolha uma das opções')
print('1- Peças')
print('2- Tipos de peças')
opção = int(input('Digite a opção desejada a partir do número: \n'))

if opção == 1:
   for n1 in pecas:
      print(f"No nosso estoque temos: {n1}")

elif opção == 2:
   for n2 in tipo:
      print(f'Temos em nosso estoque: {n2}')
    
else:
   print("Desculpe mas não temos essa opção.")

# Exercício 1
# 1. Contador de Produto (for)
# Uma esteira processa 10 peças por ciclo. Crie um programa que use um for para contar de 1 a 10 e, para cada número, imprima: "Peça nº X processada com sucesso". No final, exiba "Ciclo de produção concluído"

for ciclo in range(1, 11):
    print(f"Peça nº {ciclo} processada com sucesso...")

print('Ciclo concluído com sucesso!')

# Exercício 2
# Imagine a produção de frutas em uma feira. Desejo apresentar as frutas banana, manga, melancia, abacaxi. Com uma quantidade de 10 bananas, 5 mangas, 10 melancias e 13 abacaxi

print('Bem-vindo a nossa feira!')

for n1 in range(1,11):
    print(f'No nosso estoque temos: {n1} banana')
for n2 in range(1, 6):
    print(f'No nosso estoque temos: {n2} manga')
for n3 in range(1, 11):
    print(f'No nosso estoque temos: {n3} melancia')   
for n4 in range(1, 14):
    print(f'No nosso estoque temos: {n4} abacaxi')

print('Estoque finalizado!')

# Exercício 3
# Montar uma tabuada inicialmente pode ser usado por um valor fixo e depois usar a pergunta

print('Bem-vindo a tabuada online!')
escolha = int(input('Qual tabuada deseja fazer? Fale por número \n'))

if escolha == 1:
    for n1 in range(1, 11):
        total = (escolha * n1)
        print(f'1 x {n1}:',total)

elif escolha == 2:
    for n2 in range(1, 11):
        total = (escolha * n2)
        print(f'2 x {n2}:',total)

elif escolha == 3:
    for n3 in range(1, 11):
        total = (escolha * n3)
        print(f'3 x {n3}:',total)

elif escolha == 4:
    for n4 in range(1, 11):
        total = (escolha * n4)
        print(f'4 x {n4}:',total)

elif escolha == 5:
    for n5 in range(1, 11):
        total = (escolha * n5)
        print(f'5 x {n5}:',total)

elif escolha == 6:
    for n6 in range(1, 11):
        total = (escolha * n6)
        print(f'6 x {n6}:',total)

elif escolha == 7:
    for n7 in range(1, 11):
        total = (escolha * n7)
        print(f'7 x {n7}:',total)

elif escolha == 8:
    for n8 in range(1, 11):
        total = (escolha * n8)
        print(f'8 x {n8}:',total)

elif escolha == 9:
    for n9 in range(1, 11):
        total = (escolha * n9)
        print(f'9 x {n9}:',total)

elif escolha == 10:
    for n10 in range(1, 11):
        total = (escolha * n10)
        print(f'10 x {n10}:',total)

else:
    print('Desculpe mas não podemos te ajudar.')

# 2. O Laço while (Repetições Indeterminadas)
# Use o while quando você não sabe quando vai parar. Ele depende de uma condição (como um sensor de segurança ou um botão de emergência).
# Exemplo: Monitor de Temperatura (Loop Infinito Controlado)

# Repete enquanto a temperatura estiver segura
# Início

import time
temperatura = 25
while temperatura <= 40:
    print(f'Temperatura atual: {temperatura}°C. Sistema operando...')
    time.sleep(1)
    temperatura += 3 # Simulando o aquecimento da máquina 
print('ALERTA! Temperatura atingiu o limite. Desligando motor...')


# Exemplo: Menu Interação
# ! = diferente

opcao = ""
while opcao != "sair" and "SAIR":
    opcao = input("Digite a leitura do sensor ou 'sair' para fechar: ").upper().lower()
    if opcao != "sair" and "SAIR":
        print(f"Dado '{opcao}' registrado no banco de dados.")
print('Sistema encerrando')

# and e or 
# and comparações verdadeiras e iguais
# or comparações vergadeiras e não iguais

# Exercício 5 
# Monitor de Pressão Crítica
# Crie um simulador onde o usuário deve digitar a pressão atual de um compressor.
# Enquanto a pressão for menor que 100 PSI, o programa continua pedindo a nova leitura.
# Assim que o usuário digitar um valor maior ou igual a 100, o loop para e exibe a mensagem: "ALERTA: Pressão crítica atingida! Desligando sistema..."

import time
simulador = int(input('Digite o valor da pressão: '))
while simulador <= 100:
    print(f'Pressão atual: {simulador}PSI. Sistema operando...')
    time.sleep(1)
    simulador = int(input('Digite o valor da pressão: '))
    simulador >= 100 # Simulando o aquecimento da máquina 
print('ALERTA: Pressão crítica atingida! Desligando sistema...')

# Exercício 6
# Criar um menu de opções com 4 itens ex: Escolher Series apresente sua escolha de series das outras três.
# Qualquer opção diferente sair do menu

print('Bem-vindo ao menu de series!')
escolha = str(input("Digite o que quer ver ou 'sair' para encerrar o sistema: "))
while escolha != "sair":
    print('Ótima escolha!')
    escolha = str(input("Digite o que quer ver ou 'sair' para encerrar o sistema: "))
if escolha == "sair":
    print('Estamos encerrando o sistema.')