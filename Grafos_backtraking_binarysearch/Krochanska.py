import sys
import heapq
def dijkstra(adj, start, n):#para lista de adyacencia (u,v,costo)
    
    dist = [float('inf')] * n
    dist[start] = 0
    pq = [(0, start)]  # (distancia acumulada, nodo)

    while pq:
        d, u = heapq.heappop(pq)
        if d > dist[u]:
            continue  # ya se encontró un camino mejor antes

        for v, weight in adj[u]:
            if dist[u] + weight < dist[v]:
                dist[v] = dist[u] + weight
                heapq.heappush(pq, (dist[v], v))

    return dist
def calcular_promedio_a_ciudades_imortantes(dijstra,ciudades_importantes):
    sum=0
    for ciudad in ciudades_importantes:
        sum+=dijstra[ciudad]
    return sum/(len(ciudades_importantes)-1)


T= int(sys.stdin.readline().strip())
for case in range(T):
    N, S = map(int, sys.stdin.readline().strip().split())
    grafo = [[] for i in range(N)]
    # Armar un contador de líneas en las que aparece cada estación.
    station_line_occurrences = [0] * N

    for _ in range(S):
        estaciones = list(map(int, sys.stdin.readline().strip().split()))
        # Construir el grafo usando pares consecutivos.
        for idx in range(len(estaciones) - 2):
            a = estaciones[idx] - 1
            b = estaciones[idx + 1] - 1
            grafo[a].append((b, 1))
            grafo[b].append((a, 1))
        # Actualizar ocurrencia: contar sólo una vez por línea cada estación.
        unique_stations = set(s - 1 for s in estaciones)
        for s in unique_stations:
            station_line_occurrences[s] += 1

    print(grafo)

    # Una estación es importante si aparece en más de una línea.
    estaciones_importantes = [i for i, count in enumerate(station_line_occurrences) if count > 1]
    print()
    print(estaciones_importantes)
    menor_promedio=None
    estacion_menor=0
    for estacion_importante in estaciones_importantes:
        distancias = dijkstra(grafo, estacion_importante, N)
        print(distancias)
        if menor_promedio==None or calcular_promedio_a_ciudades_imortantes(distancias, estaciones_importantes)<menor_promedio :
            menor_promedio=calcular_promedio_a_ciudades_imortantes(distancias, estaciones_importantes)
            estacion_menor=estacion_importante+1
    print("estacion Menor:",estacion_menor)
    