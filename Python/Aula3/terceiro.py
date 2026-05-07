# Exemplo 1
#print('Verificar Maioridade')
#idade = int(input('Digite sua idade \n'))

#if idade >= 18:
   # print('Você é adulto')
#elif idade >= 16:
    # print('Você não é adulto, mas pode votar')
#else:
   # print('Você é adolencente')

#Sinais de > Maior e >= Maior igual
#Sinais de < Menor e <= Menor igual
#Sinais de == Igual

# Exemplo 2
#print('Loja')
#print('Bem-Vindo ao Sistema da Larissa')
#print('Opções:')
#print('1- Sapatos')
#print('3- Perfumes')

#escolha = int(input('Digite sua escolha pelo número da opção desejada: \n' ))
#if escolha == 1:
    #print('Você escolheu sapatos')
    #v1 = float(input('Digite o valor do produto: \n'))
    #qt1 = int(input('Digite a quantidade desejada: \n'))
    #total = v1 * qt1
    #print('Sua compra de sapatos deu um total de: ', total)

#elif escolha == 2:
    #print('Você escolheu roupas')
    #v1 = float(input('Digite o valor do produto: \n'))
    #qt1 = int(input('Digite a quantidade desejada: \n'))
    #total = v1 * qt1
    #print('Sua compra de roupas deu um total de: ', total)

#elif escolha == 3:
    #print('Você escolheu perfumes')
    #v1 = float(input('Digite o valor do produto: \n'))
    #qt1 = int(input('Digite a quantidade desejada: \n'))
    #total = v1 * qt1
   #print('Sua compra de perfumes deu um total de: ', total)

#else:
    #print('Obrigada por utilizar o Sistema da Larissa')

#Exemplo 3
#print('Escolha uma opção para iniciar o sistema')
#print('Séries = S')
#print('Filmes = F')
#categoria = input('Digite sua escolha \n')
#if categoria == 'S':
    #print('Você escolheu séries')

#elif categoria == 'F':
    #print('Você escolheu filmes')

#else:
    #print('Você não escolheu nenhuma das opções acima, estamos encerrando o sistema por agora.')



#Exercícios


#Exercício 1
#Crie um algoritimo que simule uma calculadora e que por opção de escolha permita calcular os operadores
#Ex: Ao escolher a opção 1, ele irá calcula a soma e assim por diante

print('Bem-Vindo a sua calculadora inteligente!')
print('Essas são as opções de contas:')
print('1- Soma')
print('2- Subtração')
print('3- Divisão')
print('4- Multiplicação')
conta = int(input('Qual a conta que deseja fazer? Escolha pelo seu número \n' ))

if conta == 1:
    n1 = float(input('Qual o primeiro valor da sua conta? \n'))
    n2 = float(input('E qual o segundo valor? \n'))
    total = n1 + n2
    print('O resultado da sua conta é: ', total)

elif conta == 2:
    n3 = float(input('Qual o primeiro valor da sua conta? \n'))
    n4 = float(input('E qual o segundo valor? \n'))
    total = n3 - n4
    print('O resultado da sua conta é: ', total)

elif conta == 3:
    n5 = float(input('Qual o primeiro valor da sua conta? \n'))
    n6 = float(input('E qual o segundo valor? \n'))
    total = n5 / n6
    print('O resultado da sua conta é: ', total)

elif conta == 4:
    n7 = float(input('Qual o primeiro valor da sua conta? \n'))
    n8 = float(input('E qual o segundo valor? \n'))
    total = n7 * n8
    print('O resultado da sua conta é: ', total)

else:
    print('Sintimos muito que nosso sistema não tenha o ajudado.')

#Exercício 2 
#Calculo de idade: Deve apresentar o nome, curso, data de nascimento (ano) e apresentar a idade sua no final

n1 = str(input('Olá! Qual é seu nome? \n'))
n2 = str(input('Nome bonito, e qual curso você está fazendo? \n'))
n3 = float(input('Ah sim, vou calcular sua idade. Qual o ano que você nasceu? \n'))
n4 = float(input('E qual o ano que está? \n'))
idade = n4 - n3 
print('Olá', n1,', que está no curso de', n2, ', você tem', idade, 'anos.')

#Exercício 3 
#Calcular gorjetas receba o valor da conta de um restaurante e retorne o valor da gorjeta (considerando 10% do valor da conta).
#Atendimento em mesa com garçom 10%
#Atendimento em mesa sem garçom 5%

n2 = float (input('Olá, qual o valor que deu sua conta? \n'))
print ('Tem duas opções de gorjeta:')
print('1- Com garçom: 10%')
print('2- Sem garçom: 5%')
n1 = float (input('Qual das opções você deseja? Fale em número. \n'))

if n1 == 1:
    print('Ok, vou calcular a gorjeta.')
    n6 = n2 * (10 / 100)
    total = n2 + n6 
    print('O total da sua conta é ', total)

elif n1 == 2:
    print('Ok, vou calcular a gorjeta.')
    n7 = n2 * (5 / 100)
    total = n2 + n7
    print('O total da sua conta é ', total)

else:
    print("Desculpe mas você tem que escolher uma das opções acima.")

#Exercício 4 
#Criar um sistema para calcular o sucessor e antessesor de um valor

n1 = float (input('Olá, qual o valor que você deseja calcular o sucessor e antecessor? \n'))
n2 = n1 - 1
n3 = n1 + 1
print ('O sucessor do seu número é ', n3, 'e o antecessor é ', n2)

#Exercício 5 
#Criar um algoritimo para calcular a venda de livros e que toda venda apresenta um desconto fixo de 5%

print ('Olá, bem-vindo a livraria Moon! Estamos com um desconto de 5% em qualquer compra!')
n1 = float(input('Qual o valor da soma dos seus produtos? \n'))
n3 = n1 * (5 / 100)
n2 = n1 - n3
print('O valor da sua compra é de ', n2)
