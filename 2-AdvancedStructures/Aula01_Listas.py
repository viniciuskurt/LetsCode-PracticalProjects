'''
Listas
-Listas são coleções de objetos em Python
-Coleção ou sequência ordenada de valores
-A ordenação é realizada através da "Indexação de base 0" (começa a armazenar no número 0)
-São mutáveis, podemos alterar o valor de seus itens
-Podemos gerar uma lista a partir de uma tupla ou uma tupla a partir de uma lista
-Ao invés de declarar 1 variável para cada valor que gostaríamos de armazenar,
podemos criar uma lista para armazenar vários valores.
'''

# Criando uma lista vazia.
listavazia = []

# Criando uma lista com alguns valores.
numeros = [1, 3, 7, 8, 9]

# Listas podem mesclar diferentes tipos de valores.
listamista = [14, "let's code", 0.1, True]

print(listavazia)
print(numeros)
print(listamista)

# Acessamos cada elemento da lista através de um índice entre colchetes.
print('\nAcessando elementos dentro da lista:')
print(numeros[1])
print(numeros[2])
print(listamista[1])
print(listamista[3])

#Verificamos o tamanho da lista com a função LEN()
print('\n Verificando Tamanho da Lista Mista:')
print(len(listamista))

#Verificamos o tipo da lista com a função type()
print('\n Verificando Tipo da Lista Mista:')
print(type(listamista))

# IN - Checando a existencia de determinado elemento dentro da lista. Se encontrado, será retornado resultado booleano True.
print('\nChecando existencia de valor: ')
print("Brasil" in listamista)
print(14 in listamista)

# IN NOT -
print("Canada" not in listamista)
print(14 not in listamista)