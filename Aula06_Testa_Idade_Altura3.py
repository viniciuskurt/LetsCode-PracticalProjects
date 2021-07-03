#Comparando idade e altura de forma mais aninhada e inserção de opção por usuário

idade = int(input('Digite sua idade:'))
if idade >= 12:
    resposta = input('Você gostaria de entrar nesta montanha russa?\n')
    if (resposta == 'sim'):
        print('Por favor, entre!')
    else:
        print('Ok então')
else:
    print('Você não tem idade suficiente para entrar nesse brinquedo.')