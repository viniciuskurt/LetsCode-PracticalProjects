# Exemplo básico de validação de senha de acesso

texto = input("Digite a sua entrada: ")

while texto != 'LetsCode':
    texto = input("Senha inválida. Tente novamente\n")

    print('Acesso permitido')