# o exemplo abaixo não aceita um salário menor do que o mínimo atual, entrando num loop até que seja inserido um salário maior


salario = float(input('Digite seu salario: '))
while salario < 998.0:
    salario = float(input('Entre com um salario MAIOR DO QUE 998.0: '))
else:
    print('O salario que você entrou foi: ', salario)