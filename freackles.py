import sys
import heapq
def prims(grafo, inicio=0):
    visitado = set()
    mst = []
    total_peso = 0

    
    heap = [(0, inicio, -1)]  

    while heap and len(visitado) < len(grafo):
        peso, actual, anterior = heapq.heappop(heap)

        if actual in visitado:
            continue

        visitado.add(actual)

        if anterior != -1:
            mst.append((anterior, actual, peso))
            total_peso += peso

        for vecino, p in grafo[actual]:
            if vecino not in visitado:
                heapq.heappush(heap, (p, vecino, actual))

    return mst, total_peso
def calcular_distancias(x1,y1,x2,y2):
    return ((x1-x2)**2+(y1-y2)**2)**0.5 
T=int(sys.stdin.readline().strip())
for case in range(T):
    f=int(sys.stdin.readline().strip())
    pecas=[]
    for peca in range(f):
        pecas.append(tuple(map(float,sys.stdin.readline().strip().split())))
    grafo=[[] for i in range(f)]
    print(pecas)
    for i ,peca in enumerate(pecas):
        for j in range(i+1,len(pecas)):
            grafo[i].append((j,calcular_distancias(peca[0],peca[1],pecas[j][0],pecas[j][1])))
            grafo[j].append((i,calcular_distancias(peca[0],peca[1],pecas[j][0],pecas[j][1])))
    print(grafo)
    print(prims(grafo))
