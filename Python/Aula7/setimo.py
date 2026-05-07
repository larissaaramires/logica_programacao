# Correção de prova
# 1
# print('Olá! Bem - vindo ao Registro de Veículos!')
# modelo_veiculo = (input('Qual o modelo do seu veículo? \n'))
# placa_veiculo = (input('E qual a placa dele? \n'))
# print(f'Veículo {modelo_veiculo} de placa {placa_veiculo} registrado no sistema. Boa viagem!')

# 2
# print('Olá! Irei realizar o cálculo de autonomia do seu caminhão.')
# quantidade_conbustivel = float(input('Quanto de combustível tem no seu tanque em litros? \n'))
# consumo_porKm = float(input('E qual seria o consumo médio em Km/1? \n'))
# total = quantidade_conbustivel * consumo_porKm
# print(f'A distância total que o veículo pode percorrer com o tanque como está é: {total} Km')

# 3
# print('Olá! Bem - vindo ao Conversor de Moeda!')
# frete_dolar = float(input('Qual o frete em dólar? \n'))
# valor_dolar = float(input('E quanto está o dólar hoje? \n'))
# frete_reais = frete_dolar * valor_dolar
# print(f'O frete convertido é de {frete_reais:.2f} reais.')
#:.2f para exibir com duas casas decimais

# 4
# print('Olá! Irei fazer a média de entrega.')
# entrega1 = float(input('Qual o tempo de entrega em minutos da primeira rota de entrega? \n'))
# entrega2 = float(input('Qual o tempo de entrega em minutos da segunda rota de entrega? \n'))
# entrega3 = float(input('Qual o tempo de entrega em minutos da terceira rota de entrega? \n'))
# media_rota = (entrega1 + entrega2 + entrega3) / 60
# medica_rota2 =  media_rota / 3
# print(f'O tempo de entrega está sendo de aproximadamente {media_rota2} horas')

# 5
# print('Olá! Bem - vindo ao Monitor de Carga!')
# peso_caminhao = float(input('Qual a carga do seu caminhão em toneladas? \n'))
# if peso_caminhao <= 10:
#     print('Sua carga está leve!')
# elif peso_caminhao < 25:
#     print('Sua carga está padrão!')
# elif peso_caminhao >= 25:
#     print('ALERTA: sua carga está com excesso de peso!')
# else:
#     print('Digite outro valor...')
 
# 6
# print('Olá! Bem - vindo ao Classificador de Destino.')
# codigo_carga = (input('Qual o código da carga? (Em letra maíuscula) N - Norte, S -Sul e Outros internacionais \n'))
# if codigo_carga == 'N':
#     print('Região Norte.') 
# elif codigo_carga == 'S':
#     print('Região Sul.')
# else:
#     print('Região Internacional.')

# 7
# print('Olá! Sua liberação de saída só ocorrerá se você se identifico e fez o checklist!')
# identificacao = float(input('Você se identificou? Escolha o número da opção. \n 1. Sim \n 2. Não \n'))
# checklist = float(input('Você fez o checklist? Escolha o número da opção. \n 1. Eu fiz \n 2. Eu ainda não fiz \n'))
# if identificacao and checklist == 1:
#     print('Você está liberado!')
# else:
#    print('Não é possível prosseguir com sua liberação.')

# 8
# print('Olá! Irei fazer um cálculo de atraso.')
# pecas_agendadas = int(input('Qual o total de peças agendadas? \n'))
# pecas_entregues = int(input('E qual o total de peças entregues com atraso? \n'))
# total_atraso = pecas_entregues / pecas_agendadas
# if total_atraso > 0.1:
#     print('Necessário otimizar rotas!')
# else:
#     print('Logística eficiente!')

# 9
# print('Olá! Bem - vindo a Validação de Calibragem.')
# medida_pressao = float(input('Qual a medida da pressão? (PSI) \n'))
# if medida_pressao < 100:
#     print('A pressão está abaixo do recomendado!')
# elif medida_pressao > 110:
#     print('A pressão está acima do recomendado!')
# else:
#     print('A pressão está dentro do padrão!')

# 10
# import time
# print('Contagem regressiva para o fechamento do portão:')
# for fechamento in range (5,0,-1):
#     time.sleep(1)
#     print(f'{fechamento}')
# print('Portão Trancado!')

# 11
# print('Somatório de Frete')
# frete = 0
# while True:
#    valor = float(input('Qual o valor do frete? Digite 0 para encerrar. \n'))
#    if valor == 0:
#     break
#    frete += valor
# print(f'Faturamento total: {frete} reais')

# 12
# print('Olá! Bem - vindo ao monitoriamento de frota. Irá ser utilizado 5 veículos diferentes.')
# quilometragem_maior = int(input('Qual a maior quilometragem? \n'))
# for quilometragem in range (1,5):
#     quilometragem = int(input('Qual a quilometragem do outro veículo? \n'))
# print('A maior quilometragem é:', quilometragem_maior)

# 13
# print('Sistema de Rastreio')
# erros = 0
# tentativas = 3

# while erros != 3:
#     codigo = input('Insira o código de acesso \n')
#     if codigo != "track99":
#         erros = erros + 1
#         tentativas = tentativas - 1
#         print(f'Código incorreto, você possui {tentativas} tentativas')
#     else:
#         break
# if erros == 3:
#         print('Rastreamento bloqueado!')
# else:
#         print('Acesso liberado!')

# 14
# print('Gerenciador de Combustível')
# tanque = 500
# while True:
#     print('1 - Abastecer')
#     print('2 - Retirar')
#     print('3 - Sair')
#     opcao = input('Selecione o número de deseja \n')
#     if opcao == "1":
#         valor = float(input('Quantidade a abastecer'))
#         tanque += valor
#         print(f'Tanque atual: {tanque}')
#     elif opcao == "2":
#         valor = float(input('Quantidade a retirar'))
#         if valor > tanque:
#             print('Quantidade indisponivel')
#         else:
#             tanque -= valor
#             print(f'Tanque atual: {tanque}')
#     elif opcao == "3":
#         print('Encerrando o sistema')
#         break
#     else:
#         print('Opção inválida')
#         if tanque < 50:
#             print('Reserva critíca')

# 15
print('Relatório de Inspeção de Pneus')
contagem = 0
total = 5
for pneu in range(1,6):
    medida = float(input(f'Medida do sulco do pneu {pneu}; em mm \n '))
    if medida >= 1.6:
        contagem = contagem + 1
        print('Pneu aprovado e adicionado a contagem')
    else:
        print('Pneu fora das medidas regulares, não foi adicionado a contagem')
        pass
    porcentagem = (contagem / total) * 100
    print(f'Tiveram {contagem} pneus aprovados hoje com uma taxa de {porcentagem}% de conformidade')