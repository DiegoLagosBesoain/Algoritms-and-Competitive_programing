import sys
import collections
from collections import defaultdict, deque
def maxflow(grafo, s, t):#maxflow para diccionarios con listas de tuplas
    G = defaultdict(list)
    edge_weights = defaultdict(int)

    for u in grafo:
        for v in grafo[u]:
            cap = grafo[u][v]
            G[u].append(v)
            G[v].append(u)
            edge_weights[(u, v)] += cap
            edge_weights[(v, u)] += 0

    def bfs():
        parent = {s: None}
        flow = {s: float('inf')}
        queue = deque([s])

        while queue:
            u = queue.popleft()
            for v in G[u]:
                if v not in parent and edge_weights[(u, v)] > 0:
                    parent[v] = u
                    flow[v] = min(flow[u], edge_weights[(u, v)])
                    if v == t:
                        return flow[t], parent
                    queue.append(v)
        return 0, parent

    total_flow = 0
    while True:
        new_flow, parent = bfs()
        if new_flow == 0:
            break
        total_flow += new_flow
        cur = t
        while cur != s:
            prev = parent[cur]
            edge_weights[(prev, cur)] -= new_flow
            edge_weights[(cur, prev)] += new_flow
            cur = prev

    return total_flow
T=int(sys.stdin.readline().strip())
respuestas=[]
for _ in range(T):
    poleras,voluntarios=map(int,sys.stdin.readline().strip().split())
    
    cantidad_poleras=poleras/6
    grafo={"Victor":[("XS",cantidad_poleras),("S",cantidad_poleras),("M",cantidad_poleras),("L",cantidad_poleras),("XL",cantidad_poleras),("XXL",cantidad_poleras)],"sumidero":[],
            "XS":[], "S":[], "M":[], "L":[], "XL":[], "XXL":[]}

    for i in range(voluntarios):
        talla1,talla2=sys.stdin.readline().strip().split()
        grafo[i]=[("sumidero",1)]
        grafo[talla1].append((i,1))
        grafo[talla2].append((i,1))
    
    if(maxflow(grafo,"Victor","sumidero")<voluntarios):
        respuestas.append("NO")
    else:
        respuestas.append("YES")
for respuesta in respuestas:
    print(respuesta)

