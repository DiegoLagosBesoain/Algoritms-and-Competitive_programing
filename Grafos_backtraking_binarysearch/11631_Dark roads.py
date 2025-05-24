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
n,m = map(int, sys.stdin.readline().strip().split())
while n != 0 and m != 0:
    grafos = [[] for _ in range(n)]
    costo_total=0
    for i in range(m):
        a, b, c = map(int, sys.stdin.readline().strip().split())
        grafos[a].append((b, c))
        grafos[b].append((a, c))
        costo_total+=c
    print(grafos)
    print(prims(grafos),costo_total)
    n,m = map(int, sys.stdin.readline().strip().split())