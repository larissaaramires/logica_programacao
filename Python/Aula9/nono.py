# 1. O Problema da Idade - Errado
idade = input("Digite sua idade: ")
if idade >= 18:
print("Você é maior de idade.")

# 1. O Problema da Idade - Corrigido
idade = int(input("Digite sua idade: "))
if idade >= 18:
    print("Você é maior de idade.")

# 1. O Problema da Idade - Corrigido 2
idade = int(input("Digite sua idade: "))
if idade >= 18:
    print("Você é maior de idade.")
else:
    print("Você é menor de idade")


# 2. A Escrita Fiel - Errado
nome = "Mariana"
print("Seja bem-vinda, nome!")

# 2. A Escrita Fiel - Corrigido
nome = "Mariana"
print("Seja bem-vinda, ",nome,"!")

# 2. A Escrita Fiel - Corrigido 2 
nome = input("Digite seu nome: ")
print("Seja bem-vindo,", nome)


# 3. Falta de Espaço - Errado 
numero = 10
if numero > 5:
print("O número é maior que cinco.")
else:
print("O número é menor ou igual a cinco.")

# 3. Falta de Espaço - Corrigido 
numero = 10
if numero > 5:
    print("O número é maior que cinco.")
else:
    print("O número é menor ou igual a cinco.")


# 3. Falta de Espaço - Corrigido 2
numero = int(input("Digite o número: "))
if numero > 5:
    print("O número é maior que cinco.")
elif numero == 5:
    print("O número é igual a cinco.")
else:
    print("O número é menor que cinco.")


# 4. Esquecimento Fatal - Errado
usuario="aluno123"
if=="aluno123"
    print("Login realizado com sucesso.")

# 4. Esquecimento Fatal - Corrigido
usuario = "aluno123"
if usuario == "aluno123":
    print("Login realizado com sucesso.")

# 4. Esquecimento Fatal - Corrigido 2
usuario = (input("Digite o usuário: "))
if usuario == "aluno123":
    print("Login realizado com sucesso.")
else:
    print("Usuário incorreto!")


# 5. Atribuição vs. Comparação - Errado
clima = "ensolarado" 
if clima = "chuvoso": 
    print("Leve um guarda-chuva!")

# 5. Atribuição vs. Comparação - Corrigido
clima = "ensolarado" 
if clima == "chuvoso": 
    print("Leve um guarda-chuva!")

# 5. Atribuição vs. Comparação - Corrigido 2
clima = input("Qual o clima, ensolarado ou chuvoso? \n")
if clima == "chuvoso": 
    print("Leve um guarda-chuva!")
else:
    print("Aproveite o dia ensolarado!")


# 6. Misturando Alhos com Bugalhos - Errado
pontos = 50 
print("Parabéns! Você fez " + pontos + " pontos.")

# 6. Misturando Alhos com Bugalhos - Corrigido
pontos = 50 
print("Parabéns! Você fez " , pontos , " pontos.")

# 6. Misturando Alhos com Bugalhos - Corrigido 2
pontos = int(input("Digite os pontos: "))
print("Parabéns! Você fez " , pontos , " pontos.")


# 7. A Ordem dos Fatores - Errado 
# O sistema deve dar "Excelente" para notas 9 ou 10. 
nota = 9.5 
if nota >= 7: 
    print("Aprovado") 
elif nota >= 9: 
    print("Excelente!")

# 7. A Ordem dos Fatores - Corrigido 
nota = 9.5 
if nota >= 9: 
    print("Excelente!") 
elif nota >= 7: 
    print("Aprovado")

# 7. A Ordem dos Fatores - Corrigido 2 
nota = int(input("Qual sua nota? \n"))
if nota >= 9: 
    print("Excelente!") 
elif nota >= 7: 
    print("Aprovado")
else:
    print("Você foi reprovado!")


# 8. O Contador de 1 a 5 - Errado
# Objetivo: Mostrar na tela os números 1, 2, 3, 4 e 5. 
for i in range(5): 
    print(i)

# 8. O Contador de 1 a 5 - Corrigido
for i in range(1,6): 
    print(i)


# 9. O Loop Eterno - Errado
tentativas = 1 
while tentativas <= 3: 
    print("Tentando conectar...") 
# O código deveria parar após 3 tentativas

# 9. O Loop Eterno - Corrigido
tentativas = 1
while tentativas <= 3: 
    print("Tentando conectar...")
    tentativas += 1


# 10. A Senha Teimosa - Errado 
# O programa deve pedir a senha até que o usuário digite "python123" 
senha = "" 
while senha == "python123": 
    senha = input("Digite a senha secreta: ") 
print("Acesso concedido!")

# 10. A Senha Teimosa - Corrigido
senha = "" 
while True:
    senha = input("Digite a senha secreta: ") 
    if senha == "python123": 
        print("Acesso concedido!")
        break

# 10. A Senha Teimosa - Corrigido 2
senha = "" 
while True:
    senha = input("Digite a senha secreta: ") 
    if senha == "python123": 
        print("Acesso concedido!")
        break
    else:
        print("Senha incorreta, acesso negado!")
        