qtd = int(input())

soma = 100
maiorSoma = 100

while(qtd > 0):
    valor = int(input())
    soma += valor

    if soma > maiorSoma:
        maiorSoma = soma

    qtd -= 1

print(maiorSoma)