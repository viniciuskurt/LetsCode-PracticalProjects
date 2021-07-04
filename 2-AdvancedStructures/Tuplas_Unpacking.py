'''
UNPACKING - Desempacotar
Faz somente na Tupla (não faz na Lista)

Pega vários valores de uma tupla e coloca cada um desses valores em uma variável diferente
'''

numeros = (1,2,3,4,5,6)

print(numeros)

a, b, c, d, e, f = numeros # "desempacota" a tupla numeros
print("O primeiro vale:", a, "e o ultimo vale:", f)

print("--" * 30)

nomes_paises = 'Brasil', 'Argentina', 'China', 'Alemanha', 'Japão'
print(nomes_paises)
print(type(nomes_paises))

#criar e atribuir as variáveis a tupla:
pais0, pais1, pais2, pais3, pais4 = nomes_paises

print(pais2)
print(pais2, pais4)

print("--" * 30)

# A Função UNPACKING também pode ser usada como parâmetros de funções
print("Usando Unpacking como parâmetros de função:")

print(nomes_paises) #imprimindo tupla normal

print(*nomes_paises) # passando como parâmetro de função