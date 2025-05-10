import sys


def dijkstra(grafo, inicio):
    distancias = {nodo: float('inf') for nodo in grafo}
    distancias[inicio] = 0
    visitados = set()
    while len(visitados) < len(grafo):
        nodo_actual = min((nodo for nodo in grafo if nodo not in visitados), key=lambda x: distancias[x])
        visitados.add(nodo_actual)
        for vecino, peso in grafo[nodo_actual]:
            if vecino not in visitados:
                nueva_distancia = distancias[nodo_actual] + peso
                if nueva_distancia < distancias[vecino]:
                    distancias[vecino] = nueva_distancia
    return distancias
T = int(sys.stdin.readline().strip())
for caso in range(T):
    filas=int(sys.stdin.readline().strip())
    columnas=int(sys.stdin.readline().strip())
    matriz=[]
    for fila in range(filas):
        matriz.append(list(map(int,sys.stdin.readline().strip().split())))
    print(matriz)
    grafo={}
    for fila in range(filas):
        for columna in range(columnas):
            if not f"{fila,columna}" in grafo:
                grafo[f"{fila},{columna}"]=[]
            if columna-1>=0:
                grafo[f"{fila},{columna}"].append((f"{fila},{columna-1}",matriz[fila][columna-1]))
            if columna+1<columnas:
                grafo[f"{fila},{columna}"].append((f"{fila},{columna+1}",matriz[fila][columna+1]))
            if fila-1>=0:
                grafo[f"{fila},{columna}"].append((f"{fila-1},{columna}",matriz[fila-1][columna]))
            if fila+1<filas:
                grafo[f"{fila},{columna}"].append((f"{fila+1},{columna}",matriz[fila+1][columna]))
    print(grafo)
    print()
    print(dijkstra(grafo,"0,0"))