import sys
from collections import defaultdict, deque
def maxflow(grafo, s, t):

    # Build an adjacency list and a capacity map from the given grafo format
    G = defaultdict(list)
    edge_weights = defaultdict(int)

    # Iterate over each node and its neighbors as (neighbor, capacity)
    for u in grafo:
        for v, cap in grafo[u]:
            G[u].append(v)
            G[v].append(u)  # add reverse edge for residual graph
            edge_weights[(u, v)] += cap
            # Ensure reverse edge exists with 0 capacity initially
            if (v, u) not in edge_weights:
                edge_weights[(v, u)] = 0

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

    return total_flow,edge_weights

linea=sys.stdin.readline().strip()

while linea!="":
    grafo={"S":[],"0":[("T",1)],"1":[("T",1)],"2":[("T",1)],"3":[("T",1)],"4":[("T",1)],"5":[("T",1)],"6":[("T",1)],"7":[("T",1)],"8":[("T",1)],"9":[("T",1)],"T":[]}
    instancias_requeridas=0
    while linea!="":
        
        tarea,computadores_aptos=linea.split()
        grafo["S"].append((tarea[0],int(tarea[1])))
        if tarea[0] not in grafo:
            grafo[tarea[0]] = []
        instancias_requeridas+=int(tarea[1])
        computadores_aptos=list(computadores_aptos)
        computadores_aptos.pop()
        for computador in computadores_aptos:
            grafo[tarea[0]].append((computador,1))
        linea=sys.stdin.readline().strip()
    print(grafo)
    print()
    flujo_total, edge_weights = maxflow(grafo, "S", "T")
    if flujo_total < instancias_requeridas:
        print("!")
    else:
        resultado = ['_'] * 10
        for i in range(10):
            for app in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
                if edge_weights[(str(i), app)] > 0:
                    if app!="T":
                        resultado[i] = app
        print("".join(resultado))
    linea=sys.stdin.readline().strip()

    