# Exemplo 1
# Lista de temperaturas lidas pelo sensor por minuto 
# leituras = [70, 75, 82, 98, 110, 85, 80]

# for temp in leituras:
#     if temp > 100:
#         print(f"CRÍTICO: {temp} °C detectada! Acionando parada de emergência.")
#         break # O loop para aqui e NÃO lê os próximos valolres (85 e 80)
#     print(f"Temperatura está em {temp} °C. Operação normal.")

# print("Sistema desligando. Aguardando manutenção.")

# Cenario 2
# Adicionar uma outra condição para temperatura abaixo de 50 e  quando chegar até 10 parar

# leituras = [70, 75, 82, 98, 110, 85, 80]
# numeros = [50, 55, 52, 20, 15, 10]

# for temp in leituras:
#     if temp > 100:
#         print(f"CRÍTICO: {temp} °C detectada! Acionando parada de emergência.")
#         break # O loop para aqui e NÃO lê os próximos valolres (85 e 80)
#     print(f"Temperatura está em {temp}  °C. Operação normal.")
# for temp in numeros:
#     if temp < 50:
#         print(f"CRÍTICO: {temp} °C detectada! Acionando parada de emergência.")
#         break # O loop para aqui e NÃO lê os próximos valolres (15, 10)
#     else:
#         print(f"Temperatura está em {temp}  °C. Operação normal.")
# print("Sistema desligando. Aguardando manutenção.")

# Exemplo 2
# materiais = ["metal", "metal", "plástico", "metal", "vidro", "metal"]
# for pecas in materiais:
#     if pecas != "metal":
#         print(f"Aviso: Peça de {pecas} detectada. Desviando para descarte...")
#         continue # Pula o restante do código abaixo e vai para a próxima peça

#     # Este código só roda se a peça for de metal
#     print(f"Processando peça de {pecas}. Furando e polindo...")

# print("Fim do lote de produção.")

# Exercício 1 
# Tente criar um código que conte 1 a 10, mas use o continue para não imprimir o número 5 (simulando uma falha de sensor específica no item 5).

# from time import sleep
# for n1 in range (1, 11):
#     if n1 == (5):
#         print(f"Falha ao imprimir o número {n1}...")
#         sleep (1)
#         continue
#     sleep (1)
#     print(f"Imprimindo o número {n1}...")
# sleep (1)
# print("Fim da impressão.")

# Exercício 2
# Simule um semáforo com parada para cada cor. Determine um tempo que deseja para que quando mudar para tal cor ele represente uma pausa

# from time import sleep
# semaforo = ["verde", "amarelo", "vermelho"]
# for n1 in semaforo:
#     if n1 == "verde":
#      print(f"O semáforo está {n1}! Podem paasar.")
#     sleep (1)
#     if n1 == "amarelo":   
#      print(f"O semáforo está {n1}! Dessacelerem.")
#     sleep (1)
#     if n1 == "vermelho":
#      print(f"O semáforo está {n1}! Parem!")

# Exercício 3 - Soma de Cargas de Energia (for)
# Uma fábrica tem 5 máquinas. Peça ao usuário (via input dentro do loop) o consumo em kWh de cada uma das 5 máquinas. Ao final do loop, o programa deve exibir o consumo total da fábrica.

# KWh = 0
# print('Olá! Irei calcular o consumo total da fábrica!')
# for n1 in range (1, 6):
#     KWh = KWh + int(input(f'Qual o consumo em KWh da máquina {n1}?\n'))

# print("O consumo total da fábrica é: ",KWh ,"KWh")

# Exercício 4 - Identificador de Peças Defeituosas (for + if)
# Percorra uma lista de medidas de peças: 
# medidas = [50.1, 49.8, 52.0, 50.0, 48.5].
# O padrão de qualidade aceita apenas peças com exatamente 50.0 ou mais.
# Use um for para ler a lista e, para cada peça, diga se ela está "Aprovada" ou "Rejeitada".

from time import sleep
medidas = [50.1, 49.8, 52.0, 50.0, 48.5]
for pecas in medidas:
    if pecas > 50:
        print(f'Peça {pecas}, aprovada!')
        sleep (1)
    else:
        sleep (1)
        print(f'Peça {pecas}, rejeitada!')