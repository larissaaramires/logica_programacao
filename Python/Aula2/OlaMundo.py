# Tipos de dados
# int
# float

# x = 10 
# y = 5.15

# # Números e valores
# print ('10')
# print (5.15)

# # Textos e string
# print ("Meu nome é Larissa")

# # Concatenar
# print ("Eu gosto de programar\n" + "Python")

# # Contas 
# n1 = 10
# n2 = 5 
# print("Os valores são", n1 + n2)

# Operadores matemáticos 
# + = soma
# - = subtração 
# * = multiplicação 
# / = divisão 
# ^ = expoente

# Exemplo 2 
# n1 = 20
# n2 = 10
# print('Os valores são', n1 * n2)

# # Exemplo 3
# n2 = input('Digite o seu primeiro número: \n')
# print('Seu primeiro número foi: \n', n2)

# Exemplo 4
# nome = input('Qual é seu nome? \n')
# print('Meu nome é: \n', nome) # Aqui mais completo
# print(nome) # Aqui mais simples

# # Exemplo 5
# curso = input('Qual é o seu curso? \n')
# print('Meu curso é: \n', curso)
# idade = input('Qual é sua idade? \n')
# print('Minha idade é: \n', idade, 'anos')

# Exemplo 6
# base = 10 
# altura = 5
# area = (base * altura) / 2
# print(area)

# Exemplo 6b
# Com informações
# base = float (input('Qual é a base? \n'))
# altura = float (input('Qual é a altura? \n'))
# area = (base * altura) / 2
# print('Area é igual:', float(area), 'metros')


# Exercício 1
# # Criar uma calculadora com os operadores soma e subtrair
# print('Bem-vindo a sua calculadora inteligênte!')
# n3 = input('Deseja fazer uma soma, subtração, multiplicação ou divisão? \n')
# n1 = float (input('Qual o primeiro valor da sua conta? \n'))
# n2 = float (input('Estamos quase lá! Qual o segundo valor? \n'))
# soma = (n1 + n2)
# subtração = (n1 - n2)
# multiplicação = (n1 * n2)
# divisão = (n1 / n2)
# print('O resultado da sua conta de soma é:', float(soma))
# print('O resultado da sua conta de subtração é:', float(subtração))
# print('O resultado da sua conta de multiplicação é:', float(multiplicação))
# print('O resultado da sua conta de divisão é:', float(divisão))


# Exercício 2
# print('Bem-vindo a sua calculadora inteligênte!')
# n1 = float (input('Qual o primeiro valor da sua conta? \n'))
# n2 = float (input('Estamos quase lá! Qual o segundo valor? \n'))
# potência = (n1 ** n2)
# divisão = (n1 / n2)
# print('O resultado da sua conta de potência é:', float(potência))
# print('O resultado da sua conta de divisão é:', float(divisão))

# Exercício 3
# print('Bem-vindo a sua calculadora IMC!')
# n1 = float (input('Qual é seu peso? \n'))
# n2 = float (input('Estamos quase lá! Qual é sua altura? \n'))
# n3 = (n2 * n2)
# IMC = (n1 / n3)
# print('O resultado do seu IMC é:', float(IMC))


# Exercício 4
#n1 = str(input('Oi! Qual é seu nome? \n'))
#n2 = int(input('Nome bonito, qual é sua idade? \n'))
#n3 = str(input('Ah sim, e qual seria sua profissão? \n'))
#print('AS suas informações são: \n Seu nome é', str(n1), 'você tem', int(n2), 'anos e atualmente você é',str(n3))

print('Bem-Vindo a sua calculadoa inteligente')
n1 = str(input('Qual conta deseja fazer: soma, subtração, multiplicação ou divisão? \n'))
n2 = int(input('Qual o primeiro valor da sua conta? \n'))
n3 = int(input('E qual seria o segundo valor? \n'))
if n1 == 'soma':
     total = n2 + n3

print('O resultado da sua conta é:', total)