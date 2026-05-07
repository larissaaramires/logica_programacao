# 1. Registro de Veículo: Peça o modelo do veículo e a placa.
# ○ Exiba: "Veículo [Modelo] de placa [Placa] registrado no sistema. Boa viagem!"

# print('Olá! Bem - vindo ao Registro de Veículos!')
# n1 = (input('Qual o modelo do seu carro? \n'))
# n2 = (input('E qual a placa dele? \n'))
# print('Veículo' , n1, 'de placa', n2, 'registrado no sistema. Boa viagem!')

#################################################################################################################################################################################

# 2. Cálculo de Autonomia: Peça a capacidade do tanque de combustível (em litros) e o consumo médio do caminhão (km/l).
# ○ Calcule e exiba a distância total que o veículo pode percorrer com o tanque cheio.

# print('Olá! Irei realizar o cálculo de autonomia do seu caminhão.')
# n1 = float(input('Quanto de combustível tem no seu tanque em litros? \n'))
# n2 = float(input('E qual seria o consumo médio em Km/1? \n'))
# n3 = n1 / n2
# print('A distância total que o veículo pode percorrer com o tanque como está é:', n3, 'Km')

#################################################################################################################################################################################

# 3. Conversor de Moeda (Frete Internacional): O sistema lê o valor de um frete em Dólar (USD).
# ○ Converta para Real (BRL) considerando a taxa de $1,00~USD \approx 5,00~BRL$ e exiba com duas casas decimais.

# print('Olá! Bem - vindo ao Conversor de Moeda!')
# n1 = float(input('Qual o frete em dólar? \n'))
# n2 = float(input('E quanto está o dólar hoje? \n'))
# n3 = n1 * n2
# print('O frete convertido é de', n3, 'reais.')

#################################################################################################################################################################################

# 4. Média de Entrega: Peça o tempo de entrega (em horas) de 3 rotas diferentes realizadas por um motorista.
# ○ Exiba a média aritmética simples do tempo dessas entregas.

# print('Olá! Irei fazer a média de entrega.')
# n1 = float(input('Qual o tempo de entrega em minutos da primeira rota de entrega? \n'))
# n4 = float(input('Qual o tempo de entrega em minutos da segunda rota de entrega? \n'))
# n5 = float(input('Qual o tempo de entrega em minutos da terceira rota de entrega? \n'))
# n3 = (n1 + n4 + n5) / 60
# n2 = n3 / 3
# print('O tempo de entrega está sendo de aproximadamente', n2, 'horas')

#################################################################################################################################################################################

# 5. Monitor de Carga: Peça o peso atual de um caminhão em toneladas.
# ○ Abaixo de 10t: "Carga Leve".
# ○ Entre 10t e 25t: "Carga padrão".
# ○ Acima de 25t: "ALERTA: Excesso de Peso!".

# print('Olá! Bem - vindo ao Monitor de Carga!')
# n1 = float(input('Qual a carga do seu caminhão em toneladas? \n'))
# if n1 <= 10:
#     print('Sua carga está leve!')
# elif 10 < n1 <= 25:
#     print('Sua carga está padrão!')
# else:
#     print('ALERTA: sua carga está com excesso de peso!')

#################################################################################################################################################################################

# 6. Classificador de Destino: O usuário insere o código da carga. Se começar com "N", exiba "Região Norte". Se começar com "S", "Região Sul". Para qualquer outro, "Região Internacional".

# print('Olá! Bem - vindo ao Classificador de Destino.')
# n1 = (input('Qual o código da carga? \n'))
# if n1 == 'n':
#     print('Região Norte.')
# elif n1 == 's':
#     print('Região Sul.')
# else:
#     print('Região Internacional.')

#################################################################################################################################################################################

# 7. Liberação de Saída: O caminhão só pode sair se o checklist == "concluído" E o motorista_identificado == "sim". 
# ○ Peça esses dois inputs e informe se o veículo está autorizado a iniciar a rota.

# print('Olá! Sua liberação de saída só ocorrerá se você se identifico e fez o checklist!')
# n1 = float(input('Você se identificou? Escolha o número da opção. \n 1. Sim \n 2. Não \n'))
# n2 = float(input('Você fez o checklist? Escolha o número da opção. \n 1. Eu fiz \n 2. Eu ainda não fiz \n'))
# if n1 and n2 == 1:
#     print('Você está liberado!')
# else:
#     print('Não é possível prosseguir com sua liberação.')

#################################################################################################################################################################################

# 8. Cálculo de Atrasos: Peça o total de entregas agendadas e o total de entregas realizadas com atraso.
# ○ Se o índice de atraso for maior que 10% do total, exiba "Necessário Otimizar Rotas", caso contrário, "Logística Eficiente".

# print('Olá! Irei fazer um cálculo de atraso.')
# n1 = float(input('Qual o total de peças agendadas? \n'))
# n2 = float(input('E qual o total de peças entregues com atraso? \n'))
# n3 = n2 * 0.1
# if n2 < n3:
#     print('Necessário otimizar rotas!')
# else:
#     print('Logística eficiente!')

#################################################################################################################################################################################

# 9. Validação de Calibragem: Um pneu de carga deve ter pressão entre 100 PSI e 110 PSI.
# ○ Peça a medida e diga se está dentro do padrão, acima ou abaixo do recomendado.

# print('Olá! Bem - vindo a Validação de Calibragem.')
# n1 = float(input('Qual a medida da pressão? (PSI) \n'))
# if n1 < 100:
#     print('A pressão está abaixo do recomendado!')
# elif n1 > 110:
#     print('A pressão está acima do recomendado!')
# else:
#     print('A pressão está dentro do padrão!')

#################################################################################################################################################################################

# 10.Contagem de Embarque: Use um for para fazer uma contagem regressiva de 5 até 1 para o fechamento do portão de embarque e finalize com "Portão Trancado!".

# print('Contagem regressiva para o fechamento do portão:')
# for n2 in range (5,0,-1):
#     print(f'{n2}')
# print('Portão Trancado!')

#################################################################################################################################################################################

# 11. Somatório de Fretes (Acumulador): Use um while para pedir o valor do frete de vários pedidos.
# ○ O loop para quando o usuário digitar 0. No fim, mostre o faturamento total acumulado.

# frete = 0
# while True:
#    valor =float(input('Qual o valor do frete? Digite 0 para encerrar. \n'))
#    if valor == 0:
#     break
#    frete += valor
# print(f'Faturamento total: {frete} reais')

#################################################################################################################################################################################

# 12.Monitoramento de Frota: Use um for para pedir a quilometragem de 5 veículos diferentes.
# ○ Ao final, mostre qual foi a maior quilometragem registrada.

# print('Olá! Bem - vindo ao monitoriamento de frota. Irá ser utilizado 5 veículos diferentes.')
# n2 = float(input('Qual a maior quilometragem? \n'))
# for n1 in range (1,5):
#     n1 = float(input('Qual a quilometragem do outro veículo? \n'))
# print('A maior quilometragem é:', n2)

#################################################################################################################################################################################

# 13.Sistema de Rastreio: Crie um while que peça o código de acesso do rastreador ("track99").
# ○ Enquanto o usuário errar, diga "Acesso Negado". Ele tem 3 tentativas. Se esgotar, exiba "Rastreamento Bloqueado".


# for n3 in range (1,4):
#     while n3 < 4:
#         codigo = (input('Qual o código de rastreio? \n'))
#         if codigo == 'track99':
#             print('Acesso liberado!')
#             break
# if codigo != 'track99':
#     print('Acesso negado!')
# else:
#     print('Rastreamento bloqueado!')
    

#################################################################################################################################################################################

# 14.Gerenciador de Combustível: Comece com um tanque de 500 litros. Crie um menu (while) onde o usuário pode: (1) Abastecer o tanque da base, (2) Retirar combustível para um caminhão ou (3) Sair. ○ Se o tanque da base ficar abaixo de 50 litros, avise: "Reserva Crítica!".



# 15.Relatório de Inspeção de Pneus: Use um for para processar 5 pneus. Para cada um, peça a profundidade do sulco (em mm). ○ Se o pneu for aprovado (maior ou igual a 1.6mm), conte-o.
# ○ No final do loop, exiba o total de pneus aprovados e a porcentagem de conformidade da frota.