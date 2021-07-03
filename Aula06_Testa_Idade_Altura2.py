# Testa idade e altura simultaneamente com comparador lógico e relacional

idade = int(input('Digite sua idade:'))
altura = float(input('Digite sua altura, em metros:'))
if idade >= 12 and altura >= 1.60:
    print('Você pode entrar na montanha russa.')
else:
    print('Você não pode entrar na montanha russa.')
print('Obrigado por participar.')