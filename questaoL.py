# Funcao para descobrir se eh anagrama
def ehAnagrama(s1,s2):
    lista1 = list(s1)
    lista2 = list(s2)

    lista1.sort()
    lista2.sort()

    pos = 0
    iguais = True

    while pos < len(s1) and iguais:
        if lista1[pos]==lista2[pos]:
            pos = pos + 1
        else:
            iguais = False

    return iguais


L, C = input().split(" ")

L = int(L)
C = int(C)

# Le as linhas da matriz
matriz = []
for i in range(0, L):
    palavra = str(input())
    matriz.insert(i, palavra)

# Le as palavras
palavras = []
qtdPalavras = int(input())
for i in range(0, qtdPalavras):
    palavra = str(input())
    palavras.insert(i, palavra)


# Criar matriz vazia
matrizVazia = []
for i in range(0, L):
    linha = '-'*C
    matrizVazia.append(linha)

# print(matrizVazia)

# Loop para detectar os anagramas na matriz na horizontal
num = 0
tamPalavra = 0
qtdPalavrasComAqueleTam = 0
palavraTemporaria = ''
numLinha = 0
for i in palavras: # percorre cada palavra
    tamPalavra = len(i) # tamanho da palavra

    for j in matriz: # vai percorrer as linhas da matriz
        qtdPalavrasComAqueleTam = C - tamPalavra + 1

        for k in range(0, qtdPalavrasComAqueleTam): # vai mandar cada possibilidade de palavra pra funcao do anagrama
            for l in range(k, tamPalavra + k):
                palavraTemporaria += j[l] # cria uma possibilidade de palavra

                """elem[i+tam*i]"""
            
            if ehAnagrama(i, palavraTemporaria):
                #matrizVazia[numLinha] = matrizVazia[numLinha][:k] + palavraTemporaria + matrizVazia[numLinha][k+tamPalavra:] # adiciona a palavra na matriz vazia
                print("Achou um anagrama")
            # print(palavraTemporaria)
            palavraTemporaria = ''
    
        numLinha += 1

print("\n")


# print(matriz)
# print(palavras)
# print(matrizVazia)
