'''
Slices/Fatiamento
Permite que a gente atribua ou acesse mais de um elemento da lista por vez
É necessário passar um índicie inicial e um índice final.
OBS: o índice que a gente classifica como final, não é incluído na sublista, veja:
'''

cidades = ['São Paulo', 'Brasilia', 'Curitiba', 'Avaré', 'Florianópolis']
print(cidades)

#recuperando cidades Brasilia e Curitiba
print(cidades[1:3]) #utilizamos o índice 3 para apontar e obter o valor antecessor.

#Caso tivessemos apontado o índice 2 ele somente Brasilia:
print(cidades[1:2])

# Slice também aceita valores negativos, invertendo a ordem da lista
print(cidades[-3:-1])

######OMITINDO ÍNDICES

# Omitir índice final - retorna de um determinado índice até o fim da lista:
print(cidades[2:])

# Omitir índice inicial - retorna do ínicio da lista até um determinado índice específicado:
print(cidades[:3])

#Omitir ambos os campos - inicial e final, ele retornará a lista completa, como se utilizassemos o print normal
print(cidades[:])