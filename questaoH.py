# N numero de caixas disp
# K num caixas para embarcar

def recursion(pesos,tam, pos, K, som):
    #print(f"entra como {som}")
    if pos + K > tam or K == 0:
        #print(f"sai como 0")
        return 0
    for i in range(pos, pos + K):
        #print(f"somando {int(pesos[i])}")
        som += int(pesos[i])
        som += recursion(pesos,tam, i+1, K - 1, som)
    #print(f"sai como {som}")
    return som

N, K = input().split(" ")
N = int(N)
K = int(K)

pesos = input().split(" ")

# intervalo de peso para o aviao
A, B = input().split(" ")
A = int(A)
B = int(B)

count = 0
som = 0
tam = len(pesos)
for i in range(tam - K + 1):
    som = int(pesos[i])
    som += recursion(pesos, tam, i+1, K - 1, 0)
    print(som)
    if som >= A and som <= B:
        count += 1
print(count)