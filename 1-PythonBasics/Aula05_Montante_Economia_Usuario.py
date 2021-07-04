# Objetivo: descobrir qual o montante que alguém pode economizar sabendo seu salário e gasto mensal:

print('Calculo Economia Anual')

# 1- Descobrir o salário mensal do usuário e fazer um casting de str para float
salario_mensal = input('Digite o valor do seu salário mensal: ')
salario_mensal = float(salario_mensal)

# 2- Descobrir o gasto mensal do usuário e realizar um casting
gasto_mensal = input('Digite o valor do seu gasto mensal em média: ')
gasto_mensal = float(gasto_mensal)

# 3- Fazer uma projeção anual dos valores
salario_total = salario_mensal * 12
gasto_total = gasto_mensal * 12

# 4- Fazer o cálculo para obter o montante economizado e retornar saída na tela
montante_economizado = salario_total - gasto_total
print('O monetante que você pode economizar ao fim do ano é de ', montante_economizado)
