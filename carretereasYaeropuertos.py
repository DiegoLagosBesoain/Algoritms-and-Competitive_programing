import heapq
import sys
from math import sqrt, isclose
def dfs(u, cid, adj, comp_id):
    stack = [u]
    comp_id[u] = cid
    while stack:
        node = stack.pop()
        for neigh, _ in adj[node]:
            if comp_id[neigh] == -1:
                comp_id[neigh] = cid
                stack.append(neigh)

def collapse_graph(adj):
    n = len(adj)
    comp_id = [-1] * n

    cid = 0
    for i in range(n):
        if comp_id[i] == -1:
            dfs(i, cid, adj, comp_id)
            cid += 1

    new_graph = [dict() for _ in range(cid)]
    for u in range(n):
        for v, weight in adj[u]:
            cu, cv = comp_id[u], comp_id[v]
            if cu != cv:
                if cv in new_graph[cu]:
                    new_graph[cu][cv] = min(new_graph[cu][cv], weight)
                else:
                    new_graph[cu][cv] = weight
                if cu in new_graph[cv]:
                    new_graph[cv][cu] = min(new_graph[cv][cu], weight)
                else:
                    new_graph[cv][cu] = weight

    collapsed = []
    for d in new_graph:
        collapsed.append([(node, w) for node, w in d.items()])

    return collapsed, comp_id
def distancia_euclidiana(p1, p2):
    return ((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2) ** 0.5
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
def prim(n, r, adj):
    visited = [False] * n
    pq = [(0, 0)]  # (peso, nodo)
    road = 0.0
    rail = 0.0
    states = 1

    while pq:
        peso, u = heapq.heappop(pq)
        if visited[u]:
            continue
        visited[u] = True

        if peso > 0:  # Ignorar el primer nodo
            if peso <= r or isclose(peso, r):
                road += peso
            else:
                rail += peso
                states += 1

        for v, w in adj[u]:
            if not visited[v]:
                heapq.heappush(pq, (w, v))
T = int(sys.stdin.readline().strip())

def prim_total(n, r, grafo_completo):
    visited = [False] * n
    pq = [(0, 0)]
    road = 0.0
    rail = 0.0
    states = 1

    while pq:
        peso, u = heapq.heappop(pq)
        if visited[u]:
            continue
        visited[u] = True
        if peso > 0:
            if peso <= r or isclose(peso, r):
                road += peso
            else:
                rail += peso
                states += 1
        for v, w in grafo_completo[u]:
            if not visited[v]:
                heapq.heappush(pq, (w, v))

    return states, round(road), round(rail)
for case in range(1, T + 1):
    n, r = map(int, sys.stdin.readline().strip().split())
    distancias = [tuple(map(int, sys.stdin.readline().strip().split())) for _ in range(n)]

    grafo_carreteras = [[] for _ in range(n)]
    grafo_completo = [[] for _ in range(n)]

    # Construimos los dos grafos:
    for i in range(n):
        for j in range(i + 1, n):
            d = distancia_euclidiana(distancias[i], distancias[j])
            grafo_completo[i].append((j, d))
            grafo_completo[j].append((i, d))
            if d <= r:
                grafo_carreteras[i].append((j, d))
                grafo_carreteras[j].append((i, d))

    # Paso 1: colapsar componentes (estados)
    _, comp_id = collapse_graph(grafo_carreteras)
    num_estados = max(comp_id) + 1
    states, road_cost, rail_cost = prim_total(n, r, grafo_completo)
    print(f"Case #{case}: {states} {road_cost} {rail_cost}")

