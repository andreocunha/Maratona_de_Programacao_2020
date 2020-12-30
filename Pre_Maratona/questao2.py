def fatorial(num):
    if(num == 0):
        return 1
    prod = 1
    for i in range(1,num+1):
        prod *= i
    return prod
        
entrada = int(input())
cont = 0
maiorNum = 1
fatorialAnt = 0
while entrada != 0:
    maiorNum = 1
    while maiorNum < 9:
        fatorialAtual = fatorial(maiorNum)
        if fatorialAtual > entrada:
            break
        fatorialAnt = fatorialAtual
        maiorNum += 1
    cont += 1
    entrada -= fatorialAnt
print(cont)

