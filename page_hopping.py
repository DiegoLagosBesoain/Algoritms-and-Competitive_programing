import sys
def floyd_warshall(grafo, nodos):
    n = len(nodos)
    # Mapear nodos reales a índices
    indice = {nodo: i for i, nodo in enumerate(nodos)}
    
    dist = [[float('inf')] * n for _ in range(n)]
    
    for i in range(n):
        dist[i][i] = 0

    for u in grafo:
        for v, peso in grafo[u]:
            i = indice[u]
            j = indice[v]
            dist[i][j] = min(dist[i][j], peso)

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

    return dist, indice

def promedio_de_promedios_sin_inf(matriz):
    promedios_fila = []
    for fila in matriz:
        valores_validos = [x for x in fila if x != float('inf')]
        if valores_validos:
            promedio = sum(valores_validos) / len(valores_validos)
            promedios_fila.append(promedio)
    if promedios_fila:
        promedio_total = sum(promedios_fila) / len(promedios_fila)
    else:
        promedio_total = float('nan')  
    return promedios_fila, promedio_total
entrada=sys.stdin.readline().strip()
def calcular_promedio(dist):
    n = len(dist)
    suma = 0
    cantidad = 0
    for i in range(n):
        for j in range(n):
            if i != j and dist[i][j] != float('inf'):
                suma += dist[i][j]
                cantidad += 1
    return suma / cantidad if cantidad else 0
def promedio_de_promedios(matriz):
    promedios_fila = [sum(fila) / len(fila) for fila in matriz]
    promedio_total = sum(promedios_fila) / len(promedios_fila)
    return promedios_fila, promedio_total
if entrada[0]!="0" and entrada[2]!="0":
    grafo={}
    entrada=entrada.split("  ")[:len(entrada)-1]
    for camino in entrada:
        a,b =map(int,camino.split())
        if a not in grafo:
            grafo[a]=[]
        grafo[a].append((b,1))
    print(grafo)
    
    dist,indice=floyd_warshall(grafo,grafo.keys())
    print(dist)
    print(calcular_promedio(dist))
    
