"""
Programa que faz a comparação se compensa para o usuário pegar um ônibus ou ir de uber para o trabalho.

Vamos considerar agora que há uma variação no preço da corrida por um período e o usuário deve esperar um pouco e tentar de novo.

Se o valor da corrida estiver entre 5 e 6 vezes o valor da passagem, o usuário devera aguardar
"""
valor_passagem = 4.30

valor_corrida = input("Digite o valor da corrida: ")

if float(valor_corrida) <= valor_passagem * 5:
    print("Pegue o Uber")
else:
    if float(valor_corrida) <= valor_passagem * 6:
        print("Aguarde um momento, o valor pode baixar...")
    else:
        print("Pegue o Onibus")