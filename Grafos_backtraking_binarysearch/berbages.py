import sys


def topological_sort(graph):#valido para diccionarios y lista de adyacencia
    visited = set()
    result = []

    def dfs(node):
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                dfs(neighbor)
        result.append(node)  # agregamos el nodo solo después de procesar todos sus vecinos

    for node in graph:  # mantiene el orden de aparición en el diccionario
        if node not in visited:
            dfs(node)

    return result[::-1]

from collections import deque, defaultdict

from collections import defaultdict
import heapq

def topological_sort(graph):
    in_degree = defaultdict(int)
    position = {node: i for i, node in enumerate(graph)}  # orden original
    result = []
    
    # Calcular in-degree de cada nodo
    for u in graph:
        for v in graph[u]:
            in_degree[v] += 1
        if u not in in_degree:
            in_degree[u] = 0  # Asegurar nodos sin entrada

    # Min-heap con nodos de in-degree 0, usando orden original
    heap = [node for node in graph if in_degree[node] == 0]
    heap.sort(key=lambda x: position[x])  # inicial ordenado por aparición
    heapq.heapify(heap)

    while heap:
        node = heapq.heappop(heap)
        result.append(node)
        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                heapq.heappush(heap, neighbor)
    
    return result
N=sys.stdin.readline().strip()
while N!="":
    N=int(N)
    grafo={}
    for i in range(N):
        alcohol=sys.stdin.readline().strip()
        grafo[alcohol]={}
    M=int(sys.stdin.readline().strip())
    for i in range(M):
        inicio,fin=sys.stdin.readline().strip().split()
        grafo[inicio][fin]=1
    
    print(grafo)
    print(topological_sort(grafo))
    N=sys.stdin.readline().strip()
    
    