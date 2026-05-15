# Sistema de Elevador de Prédio
# O predio possui 10 andares, sendo o térreo o andar 0. O elevador pode se mover para cima e para baixo , e tem a capacidade  de transportar até 5 pessoas.
# O elevador começa no andar 0 e pode ser chamado por qualquer pessoa em qualquer andar.
# O elevador deve se mover para o andar onde a pessoa chamou, e depois para o andar destino da pessoa.
# O elevador deve exibir mensagens indicando o andar atual, o número de pessoas no elevador, e as ações realizadas (subindo,descendo,parando). O programa deve continuar rodando até que usúarios decida encerrar

# Levantamento de Requisitos:
# Requisitos Funcionais
# Pode ser chamado por qualquer pessoa e em qualquer lugar
# Tem que se mover para o andar que foi chamado e parar no andar desejado pela pessoa
# Ter número máximo de pessoas
# Pode ser movido para cima e para baixo

# Requisitos Não Funcionais
# Começar no andar 0
# O elevador deve exibir mensagem indicando o andar atual, o número de pessoas no nele e as acões realizadas (subindo, descendo, parando)

def elevador():
    andares = 0
    lotacao = 5
    import time
    while True:
        print(f'Bem-vindo ao elevador! Estamos no {andares} andar.')
        sair = int(input('Deseja continuar com o sistema ligado ou desligar ele? Ecolha o número\n 1- Continuar \n 2- Desligar sistema \n'))
        if sair == 1:
            andar_desejado = int(input('Qual o andar desejado? '))
            pessoas = int(input('Quantas pessoas estão entrando? ')) 
            if pessoas <= 5:
                if andar_desejado > andares and andar_desejado <= 10:
                    print(f'Tem {pessoas} pessoas nesse elevador. Estamos no {andares} andar indo até o {andar_desejado} andar.')
                    print('Portas fechando, elevador subindo!')
                    time.sleep(5)
                    print('Elevador parando, portas abrindo...')
                    saida = int(input('Quantas pessoas estão saindo? '))
                    print('Ok, obrigada.')
                    andares = andar_desejado
                    time.sleep(5)
               
                elif andar_desejado < andares and andar_desejado >= 0 or andar_desejado <= 10:
                    print(f'Tem {pessoas} pessoas nesse elevador. Estamos no {andares} andar indo até o {andar_desejado} andar.')
                    print('Portas fechando, elevador descendo!')
                    time.sleep(5)
                    print('Elevador parando, portas abrindo...')
                    saida = int(input('Quantas pessoas estão saindo? '))
                    print('Ok, obrigada.')
                    andares = andar_desejado
                    time.sleep(5)
                   
                else:
                    print('Desculpe mas não podemos ajudar.')
                    time.sleep(5)
                  

            elif pessoas > 5 and andar_desejado >= 0 or andar_desejado <= 10:
                pessoas_a_mais = pessoas - lotacao
                print('Atingimos a capacidade máxima de cinco pessoas!')
                print(f"Tem {pessoas_a_mais} pessoas além da capacidade. Por favor, se retirem.")
                time.sleep(3)
                pessoas_apos_sair = int(input('Quantas pessoas tem agora? '))
                if pessoas_apos_sair >= 0:
                    if andar_desejado > andares and andar_desejado >= 0 or andar_desejado <= 10:
                        print(f'Tem {pessoas_apos_sair} pessoas nesse elevador. Estamos no {andares} andar indo até o {andar_desejado} andar.')
                        print('Portas fechando, elevador subindo!')
                        time.sleep(5)
                        print('Elevador parando, portas abrindo...')
                        saida = int(input('Quantas pessoas estão saindo? '))
                        print('Ok, obrigada.')
                        andares = andar_desejado
                        time.sleep(5)
                       
                    elif andar_desejado < andares and andar_desejado >= 0 or andar_desejado <= 10:
                        print(f'Tem {pessoas_apos_sair} pessoas nesse elevador. Estamos no {andares} andar indo até o {andar_desejado} andar.')
                        print('Portas fechando, elevador descendo!')
                        time.sleep(5)
                        print('Elevador parando, portas abrindo...')
                        saida = int(input('Quantas pessoas estão saindo? '))
                        print('Ok, obrigada.')
                        andares = andar_desejado
                        time.sleep(5)
                       
                    else:
                        print('Desculpe mas não podemos ajudar.')
                        time.sleep(5)
                       

            else:
                print('Desculpe mas não podemos ajudar.')
                time.sleep(5)
               
            
        elif sair == 2:
            print('Desligando sistema...')
            break
        

        else:
            print('Desculpe mas não podemos ajudar.')
            time.sleep(5)
            
print(elevador())