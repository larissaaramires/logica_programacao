# Atividade 1: Mensagem de Boas-Vindas
# Crie um script que use a função print() para exibir a mensagem "Bem-vindo ao mundo da programação em Python!".

print("Bem-vindo ao mundo da programação em Python!")

# Atividade 2: Informações Pessoais 
# Escreva um programa que imprima seu nome completo em uma linha e sua idade em outra linha.

print("Olá! Meu nome é Larissa Ramires de Souza \nEu tenho 16 anos" )

# Atividade 3: Calculadora de Soma e Subtração  
# Crie um script que exiba o resultado da soma de 135 com 246 e o resultado da subtração de 512 por 128. Cada resultado deve ser exibido em uma linha separada. 

print("Os valores são:")
print(135+246)
print(512-128)

print("Olá! Bem-vindo a sua calculadora inteligente!")
print("Você pode fazer as seguintes contas:")
print("1- soma")
print("2- subtração")
n4 = int(input("Qual deseja fazer? Escolha pelo número. \n"))

if n4 == 1:
    n1 = int(input("Ok, qual o primeiro valor da sua conta? \n"))
    n2 = int(input("E qual o segundo valor? \n"))
    total = n1 + n2
    print("O resultado da sua conta de soma é ", total)
elif n4 == 2:
    n1 = int(input("Ok, qual o primeiro valor da sua conta? \n"))
    n2 = int(input("E qual o segundo valor? \n"))
    total = n1 - n2
    print("O resultado da sua conta de subtração é ", total)
else:
    print("Desculpe mas não podemos te ajudar no momento.")

# Atividade 4: Multiplicação e Divisão  
# Escreva um programa que mostre o resultado da multiplicação de 15 por 8 e o resultado da divisão de 78 por 3.

print("Os valores são:")
print(15*8)
print(78/3)

# Atividade 5: Potenciação 
# Calcule e exiba o resultado de "5 elevado à 3ª potência" (5³). 

print("O valor é:")
print(5**3)

# Atividade 6: Concatenando Palavras 
# Crie um script que declare o seu primeiro nome em uma string e seu sobrenome em outra. Use o operador + para concatenar (juntar) as duas strings e exibir seu nome completo. 

print("Meu nome é:")
print("Larissa" + " " + "Ramires")

# Atividade 7: Cálculo de Eficiência (OEE) 
# Peça a quantidade de peças produzidas e a quantidade de peças defeituosas. Calcule e exiba a taxa de aproveitamento (peças boas / total).

print("Olá, irei fazer um cálculo de eficiência!")
n1 = int(input("Qual a quantidade de peças produzidas? \n"))
n2 = int(input("E qual a quantidade de peças defeituosas? \n"))
n3 = n1 - n2
total = n3 / n1
n5 = total*100
print("A taxa de aproveitamento é de ", n5)

# Atividade 8: Descrição com Cálculos 
# Crie um script que exiba a seguinte frase, substituindo os cálculos pelos seus resultados: "Eu tenho 25 anos e, em 10 anos, terei 35 anos."

n1 = int(input("Oi! qual a a sua idade? \n"))
print("Então você tem", n1 ,"anos e, em 10 anos, você terá", n1 + 10 ,"anos.")

# Atividade 9:  Orçamento de Viagem (Cálculo com float) 
# Imagine que você está planejando uma viagem. O custo do hotel é de R$ 250.50 por noite e o custo da passagem é R$ 412.00. Calcule e exiba o custo total para uma viagem por noites.

n1 = int(input("Olá, irei fazer seu orçamento. Estamos cobrando 250.50 por noite, quantas deseja ficar? \n"))
total = (250.50*n1) + 412
print("Seu orçamento já somado com sua passagem é", total)

# Atividade 10: Desafio - Mini Relatório  
# Crie um script que imprima um pequeno relatório. Use print() várias vezes para formatar a saída de forma organizada.

n1 = str(input("Qual o produto que deseja fazer o relatório de vendas? \n"))
n2 = int(input("Qual a quantidade vendida? \n"))
n3 = int(input("Qual o valor de cada produto? \n"))
n4 = n3 * n2 
print("Relatório de Vendas!")
print("Produto:", n1)
print("Quantidade vendida:", n2)
print("Preço unitário: R$" , n3)
print("Total de vendas: R$" , n4)