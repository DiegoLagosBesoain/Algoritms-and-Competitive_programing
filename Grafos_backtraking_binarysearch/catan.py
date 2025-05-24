import sys

def dfs(grafo, matriz_usadas, nodo, largo_actual, largo_max, camino_actual, camino_max):
    if largo_actual > largo_max[0]:
        largo_max[0] = largo_actual
        camino_max[0] = camino_actual[:]

    for vecino in grafo[nodo]:
        if not matriz_usadas[nodo][vecino]:
            # Marcar arista como usada
            matriz_usadas[nodo][vecino] = True
            matriz_usadas[vecino][nodo] = True

            camino_actual.append(vecino)
            dfs(grafo, matriz_usadas, vecino, largo_actual + 1, largo_max, camino_actual, camino_max)
            camino_actual.pop()

            # Desmarcar (backtracking)
            matriz_usadas[nodo][vecino] = False
            matriz_usadas[vecino][nodo] = False

# Entrada principal
n, m = map(int, sys.stdin.readline().strip().split())
while n != 0 and m != 0:
    grafo = [[] for _ in range(n)]
    for _ in range(m):
        a, b = map(int, sys.stdin.readline().strip().split())
        grafo[a].append(b)
        grafo[b].append(a)

    largo_maximo = [0]
    camino_maximo = [[]]

    for i in range(n):
        matriz_usadas = [[False]*n for _ in range(n)]
        dfs(grafo, matriz_usadas, i, 0, largo_maximo, [i], camino_maximo)

    print("respuesta:", largo_maximo[0])
    print("camino:", camino_maximo[0])

    n, m = map(int, sys.stdin.readline().strip().split())