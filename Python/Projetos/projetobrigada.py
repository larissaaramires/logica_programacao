# Contexto: O Serviço Especializado em Engenharia de Segurança e em Medicina do Trabalho (SESMT) precisa automatizar o controle de treinamentos obrigatórios (como CIPA, Brigada de Incêndio e NR-35) e a entrega de Equipamentos de Proteção Individual (EPIs).
# Objetivo: Desenvolva um programa em Python que gerencie o status de conformidade dos funcionários de uma empresa.

# Levantamento de Requisitos
# Requisitos Funcionais:
# RF01 – Cadastro de Funcionários: o sistema deve permitir o cadastro de funcionários com nome, setor e status dos treinamentos (NR-10, NR-35 e Brigada).
# RF02 – Verificação de EPI (NR-6): o sistema deve receber o setor do funcionário e verificar os EPIs obrigatórios.
# Para o setor Elétrica: luvas de alta tensão e botas dielétricas.
# Para o setor Trabalho em Altura: cinturão de segurança e talabarte.
# RF03 – Alerta de Reciclagem: o sistema deve verificar o ano do último treinamento da Brigada de Incêndio.
# Se o treinamento tiver mais de 2 anos: exibir, “Treinamento Vencido! Encaminhar para reciclagem.”
# Caso contrário: exibir, “Treinamento Válido.”
# RF04 – Relatório Geral o sistema deve exibir total de funcionários cadastrados e quantidade de funcionários com treinamentos em dia.

# Requisitos não Funcionais:
# RNF01 – Exibição de Informações: o sistema deve exibir mensagens de status dos treinamentos e EPIs na tela.
# RNF02 – Processamento das Verificações: o sistema deve realizar automaticamente as verificações de EPIs e validade dos treinamentos conforme os dados informados.