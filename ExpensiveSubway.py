import sys
import heapq
def prims(start, neighbors):#prim para lista de adyacencias
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
def determinar_conexion(parents):
    ya_visto=False
    for parent in parents:
        if parents[parent]==-1:
            if ya_visto:
                return False
            ya_visto=True
            
    return True
def prims2(start, neighbors):#prim para diccionario de adyacencias
    n = len(neighbors)              
    visited = set()          
    min_edge = {vertex: float('inf') for vertex in neighbors}
    parent = {vertex: -1 for vertex in neighbors}                

    total_cost = 0
    min_edge[start] = 0
    pq = [(0, start)]                

    while pq:
        cost, u = heapq.heappop(pq)
        if u in visited:
            continue

        visited.add(u)
        total_cost += cost

        for v, weight in neighbors[u]:
            if v not in visited and weight < min_edge[v]:
                min_edge[v] = weight
                parent[v] = u
                heapq.heappush(pq, (weight, v))

    return total_cost, parent
s,c = map(int,sys.stdin.readline().strip().split())
while s!=0 and c!=0:
    grafo={}
    for _ in range(s):
        grafo[sys.stdin.readline().strip()]=[]
    for _ in range(c):
        ciudad1,ciudad2,peso=sys.stdin.readline().strip().split()
        grafo[ciudad1].append((ciudad2,int(peso)))
        grafo[ciudad2].append((ciudad1,int(peso)))
    inicio=sys.stdin.readline().strip()
    print(grafo)
    print(prims2(inicio,grafo))
    s,c = map(int,sys.stdin.readline().strip().split())
    valor,grafo=prims2(inicio,grafo)
    if determinar_conexion(grafo):
        print(valor)
    else:
        print("imposible")