'''
POP
Deleta um valor da lista a partir da sua posição de índice:

- Com esse método também é possível retornar o valor removido:
'''

cidades = ['São Paulo', 'Brasilia', 'Curitiba', 'Avaré', 'Florianópolis']
print(cidades)

cidades.pop(2)
print(cidades)

removido = cidades.pop(1)
print(cidades, removido)

#Apresenta erro se range não existir
cidades.pop(8)
print(cidades)