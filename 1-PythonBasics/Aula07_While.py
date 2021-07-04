# Programa recebe um valor de repetição e repete o total de vezes inserido

# Declaramos um contador como 0:
contador = 0

# Definimos o número de repetições:
numero = int(input('Digite um numero: '))

# Rodamos o while até o contador se igualar ao número de repetições:
while contador < numero:
    print(contador)
    contador = contador + 1