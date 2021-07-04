'''
STEPS

Podemos definir um intervalo para retorno da lista
'''
cidades = ['São Paulo', 'Brasilia', 'Curitiba', 'Avaré', 'Florianópolis']
print(cidades)
print('--' * 30)

print('\n Intervalo de valores da lista: ')

print(cidades[::2])

numeros = [1,2,3,4,5]
print(numeros)
print(numeros[::2])

print('--' * 30)

#Pode ser usada para inverter os valores da lista, usando um valor negativo:

print('\n Inverte valores da lista: ')
print(cidades[::-1])
print(numeros[::-1])