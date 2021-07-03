'''
Estruturas Sequenciais

Na estrutura seqüencial os comandos de um algoritmo são executados numa seqüência pré-estabelecida.

Cada comando é executado somente após o término do comando anterior.

Cada linha é executada antes da próxima

OUTPUTS - SAÍDAS

todos os dados que são gerados pelo programa e fornecidos para o usuário

a função print() imprime os valores na tela
'''

print('eu estudo na escola')

escola = 'Lets Code'
print('eu estudo na ', escola)

# Podemos fazer operações dentro do print:

print(1+1, 2*2)
y = 1
x = 2
print (y+1, x**2)

print('--' * 30)

'''
INPUTS - ENTRADAS

São as informações que o usuário possui e deve fornecer ao código
Podemos ler valores do teclado com a função input()
Ela permite que a gente passe uma mensagem para o usuário
'''

idade = input("Informe a sua idade: ")
print(idade)

#FUNÇÃO TYPE - mostra o tipo do dado inserido

print(type,(idade))

print('--' * 30)

#Sempre e independente do que for, o valor “inputado” pelo usuário será mapeado para um tipo STR (string)

'''
CASTING

ato de transformar um dado de entrada digitado através de input pelo usuário e transformar em diferentes tipos
'''
peso = input("Informe a seu peso: ")
print(peso, type(peso))

#realizando o casting
peso = int(peso)
print(peso, type(peso))


