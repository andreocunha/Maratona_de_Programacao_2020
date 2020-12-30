
def nomeAConstroi(nomeA, nomeConcatenado, nomesB):
  i = 0
  for letraA in nomeA:
    if letraA != nomeConcatenado[i]:
      return 0
    i = i+1
  
  #verifica se tem algum nome b que forma nomeCOncatenado com A
  for nomeB in nomesB:
    if nomeA+nomeB == nomeConcatenado:
      return 1
  return 0


def nomeBConstroi(nomeB, nomeConcatenado, nomesA):
  j = len(nomeConcatenado)-1
  i = len(nomeB) - 1
  #print(f"nomeBConstroi: Comparando o {nomeB} com o {nomeConcatenado} // {j}")
  while i>=0:
    #print(i, j)
    if nomeB[i] != nomeConcatenado[j]:
      return 0
    j = j-1
    i = i-1
  
  #verifica se tem algum nome b que forma nomeCOncatenado com A
  for nomeA in nomesA:
    if nomeA+nomeB == nomeConcatenado:
      #print(f"{nomeB} compões {nomeConcatenado}")
      return 1
  return 0




nA, nB = input().split(" ")
nA = int(nA)
nB = int(nB)

nomesA = input().split(" ")
nomesB = input().split(" ")
#print("Nomes A:", nomesA)
#print("Nomes B:", nomesB)

nomesConcatenados = []
#Concatenar nomes
for nomeA in nomesA:
  for nomeB in nomesB:
    nomeConcatenado = nomeA+nomeB
    nomesConcatenados.append(nomeConcatenado)
#print(nomesConcatenados)

#Para cada nome do time A, verificar se está contido nos nomes concatenados
#Se estiver contido em mais nomes do que nB, não é peculiar (diminui um contador)
nPeculiarA = nA
for nomeA in nomesA:
  contVezes = 0
  for nomeConcatenado in nomesConcatenados:
    if nomeAConstroi(nomeA, nomeConcatenado, nomesB):
      contVezes = contVezes + 1
      if contVezes > nB:
        nPeculiarA = nPeculiarA - 1
        break

#Para cada nome do time B, verificar se está contido nos nomes concatenados
#Se estiver contido em mais nomes do que nA, não é peculiar (diminui um contador)
nPeculiarB = nB
#print(nomesConcatenados)
for nomeB in nomesB:
  contVezes = 0
  for nomeConcatenado in nomesConcatenados:
    if nomeBConstroi(nomeB, nomeConcatenado, nomesA):
      contVezes = contVezes + 1
      if contVezes > nA:
        nPeculiarB = nPeculiarB - 1
        break

print(nPeculiarA, nPeculiarB)
