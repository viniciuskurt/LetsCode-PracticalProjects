"""
Programa que faz a comparação se compensa para o usuário pegar um ônibus ou ir de uber para o trabalho.

Como regra de negócio, se o valor da corrida for menor ou igual até 5 vezes o valor da passagem
"""

valor_passagem = 4.30

valor_corrida = input("Digite o valor da corrida: ")

if float(valor_corrida) <= valor_passagem * 5:
    print("Pegue o Uber")
if float(valor_corrida) > valor_passagem * 5:
    print("Pegue o Onibus")