'''
REMOVE
Deleta valores de uma lista

- Apresenta erro se o elemento não existir
'''

cidades = ['São Paulo', 'Brasilia', 'Curitiba', 'Avaré', 'Florianópolis']
print(cidades)

cidades.remove('Brasilia')
print(cidades)


#erro:
cidades.remove('Portugal')
print(cidades)
