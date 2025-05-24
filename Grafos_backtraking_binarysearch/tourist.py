import sys

import math
def mayor_minimo_flujo(grafo,nodo,fin,minimo_actual,maximo_flujo_posible,visitados):#dfs para grafos de adyacencia con pesos
    
    if nodo==fin:
        return minimo_actual
    visitados[nodo]=True
    for vecino in grafo[nodo]:
        if not visitados[vecino[0]]:
            maximo_flujo_posible=max(mayor_minimo_flujo(grafo,vecino[0],fin,min(minimo_actual,vecino[1]),maximo_flujo_posible,visitados),maximo_flujo_posible)
    visitados[nodo]=False
    
    
    return maximo_flujo_posible
            





N,R=map(int,sys.stdin.readline().strip().split())
while N!=0 and R!=0:
    grafo=[[] for i in range(N)]
    for camino in range(R):
        a,b,peso=map(int,sys.stdin.readline().strip().split())
        grafo[a-1].append((b-1,peso-1))
        grafo[b-1].append((a-1,peso-1))
    minimo_actual=float("inf")
    print(grafo)
    visitados=[False]*N
    S,D,T=map(int,sys.stdin.readline().strip().split())
    print(mayor_minimo_flujo(grafo,S-1,D-1,minimo_actual,0,visitados))
    N,R=map(int,sys.stdin.readline().strip().split())
    print(math.ceil(T/mayor_minimo_flujo(grafo,S-1,D-1,minimo_actual,0,visitados)))


