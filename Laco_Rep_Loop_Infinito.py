"""
Laço de repetição com loop infinito e utilizando break

NÃO É RECOMENDADO UTILIZAR ESSA FORMA.
"""
contador = 0

# while contador < 10:
while True:  # criando loop infinito
    if contador < 10:  # se a condição passar da condição, é executado tudo de novo
        contador = contador + 1
        if contador == 1:
            print(contador, "item limpo")
        else:
            print(contador, "itens limpos")
    else:
        break  # aqui quebramos o loop mais recente

print("Fim da repetição do bloco while")