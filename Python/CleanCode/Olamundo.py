# 1. Perfil de Gamer: Peça o nick (nome) do jogador e o nível atual. Exiba: "O jogador [nick] está no nível [nível] e pronto para a partida!"

print('Olá! Bem-vindo ao Perfil de Gamer!')
nick = input('Qual o seu nick name? \n')
nivel = input('E qual seu nível atual no jogo? \n')
print('O jogador' , (nick),'está no nível', (nivel),'e pronto para a partida!')

# 2. Calculadora de Mesada: Peça o valor que o aluno ganha por semana e multiplique por 4 para mostrar quanto ele terá no final do mês.

print('Olá! Irei calcular sua mesada.')
mesada = int(input('Qual o valor que você ganha por semana? \n'))
valor = (mesada * 4)
print('Sua mesada mensal é de', (valor), 'reais')