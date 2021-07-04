'''
Lista de Animais

Algoritmo combina while e lista.
Regra de Negócio:
1- Enquanto usuário responder condição, poderá inserir um novo animal a Lista, caso contrário programa deve ser encerrado e mostrado animais inseridos
'''

animais = []

resposta = 's'

while resposta == 's' or resposta == 'S':
    resposta = input('Deseja adicionar um animal à lista (s/n)? ')
    if (resposta == 's' or resposta == 'S'):
        animal = input('Digite o nome do animal: ')
        animais.append(animal) # adiciona o novo animal à lista
print(animais)