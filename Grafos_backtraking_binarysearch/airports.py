import sys
import heapq
def dijkstra(grafo, partida, N):
    visitados = [False] * N
    distancias = [float('inf')] * N
    distancias[partida] = 0
    cola_prioridad = [(0, partida)]  # (distancia, nodo)

    while cola_prioridad:
        distancia_actual, nodo_actual = heapq.heappop(cola_prioridad)

        if visitados[nodo_actual]:
            continue

        visitados[nodo_actual] = True

        for vecino, peso in grafo[nodo_actual]:
            if not visitados[vecino]:
                nueva_distancia = distancia_actual + peso
                if nueva_distancia < distancias[vecino]:
                    distancias[vecino] = nueva_distancia
                    heapq.heappush(cola_prioridad, (nueva_distancia, vecino))

    return distancias
X=int(sys.stdin.readline().strip())
for _ in range(X):
    N,M,K=map(int,sys.stdin.readline().strip().split())
    grafo=[[] for _ in range(N)]
    ciudades_con_aeropuerto = [int(x) - 1 for x in sys.stdin.readline().strip().split()]
    for j in range(M):
        ciudad,ciudad2=map(int,sys.stdin.readline().strip().split())
        if ciudad-1 in ciudades_con_aeropuerto and ciudad2-1 in ciudades_con_aeropuerto:
            grafo[ciudad-1].append([ciudad2-1,0])
            grafo[ciudad2-1].append([ciudad-1,0])
        elif ciudad-1 in ciudades_con_aeropuerto:
            grafo[ciudad-1].append([ciudad2-1,1])
            grafo[ciudad2-1].append([ciudad-1,1])
        elif ciudad2-1 in ciudades_con_aeropuerto:
            grafo[ciudad2-1].append([ciudad-1,1])
            grafo[ciudad-1].append([ciudad2-1,1])
        else:
            grafo[ciudad-1].append([ciudad2-1,2])
            grafo[ciudad2-1].append([ciudad-1,2])
    print(grafo)
    Q=int(sys.stdin.readline().strip())
    for _ in range(Q):
        entrada,salida=map(int,sys.stdin.readline().strip().split())
        dijkstra_result = dijkstra(grafo, entrada-1, N)
        print(dijkstra_result[salida-1])



