'''
OPERADORES ARITMETICOS
Fazem operações aritméticas simples:
'''

print('OPERADORES ARITMÉTICOS:\n')
print('+ soma')
print('- subtração')
print('* multiplicacao')
print('/ divisão')
print('// divisão inteira') #não arredonda o resultado da divisão, apenas ignora a parte decimal
print('** potenciação')
print('% resto da divisão\n')

x = 2
y = 5

m = x * y
print('x * y = ',m)
s = x + y
print('x + y = ',s)
sub = x - y
print('x - y = ',sub)
d = x / y
print('y / x = ',d)
di = x // y
print('x // y = ',di)
p = x ** y
print('x ** y = ',p)
rd = x % y
print('x % y = ',rd)

print('--' *30 )

print('OPERADORES LÓGICOS:\n')

print('OR - resultado Verdadeiro se UMA ou AMBAS expressões for verdadeira')
print('AND - resultado Verdadeiro somente se AMBAS as expressões forem verdadeiras')
print('NOT -  inverte o valor lógico de uma expressão (negação)\n')

tem_cafe = True
tem_pao = False

#OR
print(tem_cafe or tem_pao)
print(tem_cafe or tem_cafe)
print(tem_pao or tem_pao)

#AND
print(tem_cafe and tem_pao)
print(tem_cafe and tem_cafe)

#NOT
print(not tem_cafe)
print(not tem_pao)

print('--' *30 )

print('OPERADORES RELACIONAIS:\n')

#O Python possui 6 operadores relacionais

print('Maior que: >')
print('Maior ou Igual: >=')
print('Menor que: <')
print('Menor ou Igual: <=')
print('Igual: ==')
print('Diferente: != \n')

comparador1 = 5
comparador2 = 3

print(comparador1 > comparador2)
print(comparador1 >= comparador2)
print(comparador1 < comparador2)
print(comparador1 <= comparador2)
print(comparador1 == comparador2)
print(comparador1 != comparador2)