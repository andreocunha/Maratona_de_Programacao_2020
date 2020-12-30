class Nome:
  nome = ""
  ehPeculiar = 1

class Concat:
  nomeA = Nome()
  nomeB = Nome()
  texto = ""




nA, nB = input().split(" ")
nA = int(nA)
nB = int(nB)

nomesA = input().split(" ")
nomesB = input().split(" ")
#print("Nomes A:", nomesA)
#print("Nomes B:", nomesB)

nomesConcatenados = []
structNomesA = []
structNomesB = []
#Concatenar nomes
for nomeA in nomesA:
  NomeA = Nome()
  NomeA.nome = nomeA
  structNomesA.append(NomeA)
  for nomeB in nomesB:
    if len(structNomesB) <= nB:
      NomeB = Nome()
      NomeB.nome = nomeB
      structNomesB.append(NomeB)
    else:
      NomeB = Nome()
      NomeB.nome = nomeB
    nomeConcatenado = Concat()
    nomeConcatenado.texto = nomeA+nomeB
    nomeConcatenado.nomeA = NomeA
    nomeConcatenado.nomeB = NomeB
    nomesConcatenados.append(nomeConcatenado)

ia = 0
ib = 1
while ia < len(nomesConcatenados):
  ib = ia + 1
  while(ib < len(nomesConcatenados)):
    #print(f"Comparando {nomesConcatenados[ia].texto} com {nomesConcatenados[ib].texto}")
    if nomesConcatenados[ia].texto == nomesConcatenados[ib].texto:
      #print(f"Não são peculiares: {nomesConcatenados[ia].nomeA.nome} {nomesConcatenados[ia].nomeB.nome} {nomesConcatenados[ib].nomeA.nome} {nomesConcatenados[ib].nomeB.nome}")
      nomesConcatenados[ia].nomeA.ehPeculiar = 0
      #print(nomesConcatenados[ia].nomeA)
      nomesConcatenados[ia].nomeB.ehPeculiar = 0
      #print(nomesConcatenados[ia].nomeB)
      nomesConcatenados[ib].nomeA.ehPeculiar = 0
      #print(nomesConcatenados[ib].nomeA)
      nomesConcatenados[ib].nomeB.ehPeculiar = 0
      #print(nomesConcatenados[ib].nomeB)
    ib += 1
  ia += 1

nPeculiarA = 0
for nomeA in structNomesA:
  nPeculiarA = nPeculiarA + nomeA.ehPeculiar

  
nPeculiarB = 0
for nomeB in structNomesB:
  nPeculiarB = nPeculiarB + nomeB.ehPeculiar

print(nPeculiarA, nPeculiarB)