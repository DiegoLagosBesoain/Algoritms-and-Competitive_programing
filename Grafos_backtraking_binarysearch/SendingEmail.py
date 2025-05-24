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

N=int(sys.stdin.readline().strip())
for caso in range(N):
    n,m,S,T=map(int,sys.stdin.readline().strip().split())
    grafo=[[] for i in range(n)]
    for conexion in range(m):
        a,b,peso=map(int,sys.stdin.readline().strip().split())
        grafo[a].append((b,peso))
        grafo[b].append((a,peso))
    print(grafo)
    print(dijkstra(grafo,S,N)[T])