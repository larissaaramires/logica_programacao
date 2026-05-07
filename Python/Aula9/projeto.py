# print('Hello world!')

vagas = 500
import time
while vagas >=1:
    print('Bem - vindo ao Shopping Center!')
    tipo_acesso = int(input('Qual o seu tipo de acesso? Escolha um número \n 1- Via Tag \n 2- Via Ticket \n 3- Sair \n'))
    if tipo_acesso == 1:
        hora_entrada_tag = float(input('Qual está sendo o horário da sua entrada? \n'))
        print('Acesso liberado! Boas compras.')
        print("Atenção! Caso houver perda de ticket, o valor a ser pago é de 50 reais!")
        time.sleep(5)
        perca_de_ticket_tag = int(input('Está com seu ticket? \n 1- Sim \n 2- Perdi \n'))
        if perca_de_ticket_tag == 1:
            hora_saida_tag = float(input('Qual está sendo o horário da sua agora? \n'))
            totaltag_horas = hora_saida_tag - hora_entrada_tag
            print(f'Você ficou {totaltag_horas} horas no shopping')
            if totaltag_horas <= 0.25:
                print('Total de horas tolerável, taxa grátis! Obrigada, volte sempre!')
            elif totaltag_horas <=3:
                valor_3horas_tag = 15 * 0.1
                print(f'O valor a ser pago é {15 - valor_3horas_tag} reais. Já com o desconto de 10% por ser tag.')
            elif totaltag_horas > 3:
                horastag_extras = totaltag_horas - 3
                valortag_maior_3_horas = (horastag_extras * 3) + 15
                valortag_maior_3_horas_desconto = valortag_maior_3_horas * 0.1
                print(f'O valor a ser pago é {valortag_maior_3_horas -      valortag_maior_3_horas_desconto} reais. Já com o desconto de 10% por ser tag')
        elif perca_de_ticket_tag == 2:
            print('Como avisado antes, o valor a ser pago é de 50 reais.')
        time.sleep(5)
        saida_tag = int(input('Você pagou seu ticket? \n 1- Sim \n 2- Não \n'))
        if saida_tag == 1:
            print('Saída liberada! Volte sempre!')
        elif saida_tag == 2:
            print('Saída não permitida! Volte e pague seu ticket.')

    elif tipo_acesso == 2:
        print(f'No momento temos {vagas} vagas disponíveis.')
        print('Retire seu ticket e boas compras!')
        print("Atenção! Caso houver perda de ticket, o valor a ser pago é de 50 reais!")
        vagas = vagas - 1
        time.sleep(5)
        print('Você chegou a catraca de saída. Insira seu ticket.')
        perca_de_ticket = int(input('Está com seu ticket? \n 1- Sim \n 2- Perdi \n'))
        if perca_de_ticket == 1:
            hora_entrada_ticket = float(input('Qual foi o horário da sua entrada? \n'))
            hora_saida_ticket = float(input('E que horas são agora? \n'))
            total_horas_ticket = hora_saida_ticket - hora_entrada_ticket
            print(f'Você ficou {total_horas_ticket} horas no shopping')
            if total_horas_ticket <= 0.25:
                print('Total de horas tolerável, taxa grátis! Obrigada, volte sempre!')
            elif total_horas_ticket <=3:
                print(f'O valor a ser pago é {15} reais.')
            elif total_horas_ticket > 3:
                horas_extras_ticket = total_horas_ticket - 3
                valor_maior_3_horas_ticket = (horas_extras_ticket * 3) + 15
                print(f'O valor a ser pago é {valor_maior_3_horas_ticket} reais.')
        elif perca_de_ticket == 2:
            print('Como avisado antes, o valor a ser pago é de 50 reais.')
        time.sleep(5)
        print('Você chegou a catraca de saída. Insira seu ticket.')
        saida_ticket = int(input('Você pagou seu ticket? \n 1- Sim \n 2- Não \n'))
        if saida_ticket == 1:
            print('Saída liberada! Volte sempre!')
        elif saida_ticket == 2:
            print('Saída não permitida! Volte e pague seu ticket.')

    elif tipo_acesso == 3:
        print('Obrigada! Volte sempre.')
        break

    else:
        print('Desculpe, mas não podemos te ajudar.')
        break 