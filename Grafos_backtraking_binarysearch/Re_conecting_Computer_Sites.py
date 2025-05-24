import heapq
import sys
def prims(start, neighbors):
    n = len(neighbors)              
    visited = [False] * n           
    min_edge = [float('inf')] * n    
    parent = [-1] * n                

    total_cost = 0
    min_edge[start] = 0
    pq = [(0, start)]                

    while pq:
        cost, u = heapq.heappop(pq)
        if visited[u]:
            continue

        visited[u] = True
        total_cost += cost

        for v, weight in neighbors[u]:
            if not visited[v] and weight < min_edge[v]:
                min_edge[v] = weight
                parent[v] = u
                heapq.heappush(pq, (weight, v))

    return total_cost, parent
N=sys.stdin.readline().strip()
while N!="":
    N=int(N)
    grafo_anterior=[[] for i in range(N)]
    costo_anterior=0
    for _ in range(N-1):
        inicio,fin,costo=map(int,sys.stdin.readline().strip().split())
        grafo_anterior[inicio-1].append((fin-1,costo))
        grafo_anterior[fin-1].append((inicio-1,costo))
        costo_anterior+=costo
    grafo_nuevo=[[] for i in range(N)]
    K=int(sys.stdin.readline())
    for _ in range(K):
        inicio,fin,costo=map(int,sys.stdin.readline().strip().split())
        grafo_nuevo[inicio-1].append((fin-1,costo))
        grafo_nuevo[fin-1].append((inicio-1,costo))
    M=int(sys.stdin.readline())
    for _ in range(M):
        inicio,fin,costo=map(int,sys.stdin.readline().strip().split())
        grafo_nuevo[inicio-1].append((fin-1,costo))
        grafo_nuevo[fin-1].append((inicio-1,costo))
    costo_nuevo,MSt=prims(0,grafo_nuevo)
    print(costo_anterior)
    print(min(costo_anterior,costo_nuevo))
    sys.stdin.readline().strip()
    N=sys.stdin.readline().strip()


