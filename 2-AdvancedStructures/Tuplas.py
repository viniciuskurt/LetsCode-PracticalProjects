'''
Tuplas
Também é uma coleção ou sequência ordenada de valores
A ordenação é realizada através da "Indexação de base 0" (começa a armazenar no número 0)
A Tupla é estática, após colocado os valores lá dentro, não é possível acidionar ou modificar valores
A principal diferença entre Lista e Tupla é a flexibilidade do que a gente consegue fazer com cada uma.
A Tupla possui algumas implementações e opções especiais que a Lista não tem
Devido a rigidez(estática) é um pouco menor que a Lista em questão de armazenamento
Podemmos declarar com ou sem parenteses ()
Para acessar um valor, utilizamos a mesma sintaxe das listas:
Podemos gerar uma tupla a partir de uma lista ou uma lista a partir de uma tupla
'''

# Ao invés de colchetes, usamos parênteses para declarar as tuplas:
numeros = (1,2,3,4,5,6)

print(numeros)
print(type(numeros))

# Podemos declarar sem parênteses também:
primos = 2,3,5,7,11
print(primos)
print(type(primos))

#Para acessar um valor, utilizamos a mesma sintaxe das listas:
print(numeros[4])
print(primos[0])

'''
Tuplas são imutáveis: não é possível adicionar ou modificar valores.
Descomentar a linha abaixo provocará erro de execução:
'''
#numeros[4] = 8

# Podemos gerar uma tupla a partir de uma lista...
lista1 = [3, 1, 4, 1, 5, 9, 2, 6, 5]
tupla1 = tuple(lista1)
print(tupla1)

# ...ou uma lista a partir de uma tupla:
tupla2 = [1, 6, 1, 8]
lista2 = list(tupla2)
print(lista2)