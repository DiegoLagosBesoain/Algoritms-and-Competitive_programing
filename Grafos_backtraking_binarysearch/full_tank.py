import sys


def dijkstra(grafo, inicio):
    distancias = {nodo: float('inf') for nodo in grafo}
    distancias[inicio] = 0
    visitados = set()
    while len(visitados) < len(grafo):
        nodo_actual = min((nodo for nodo in grafo if nodo not in visitados), key=lambda x: distancias[x])
        visitados.add(nodo_actual)
        for vecino, peso in grafo[nodo_actual]:
            if vecino not in visitados:
                nueva_distancia = distancias[nodo_actual] + peso
                if nueva_distancia < distancias[vecino]:
                    distancias[vecino] = nueva_distancia
    return distancias
n,m=map(int,sys.stdin.readline().strip().split())

precios=[int(x) for x in sys.stdin.readline().strip().split()]
conexiones=[]

for _ in range(m):
    a,b,c=map(int,sys.stdin.readline().strip().split())
    conexiones.append((a,b,c))
    conexiones.append((b,a,c))

q=int(sys.stdin.readline().strip())
for q in range(q):
    c,s,e=map(int,sys.stdin.readline().strip().split())
    grafo={}
    for i in range(n):#ciudades
        for j in range(c+1):#estados de gasolina
            grafo[(i,j)]=[]
            if j<c:
                
                grafo[(i,j)].append(((i,j+1),precios[i]))#si necesito gasolina compro por el precio de la ciudad
        #ahora conectamos entre ciudades
    for a,b,d in conexiones:
        for i in range(c+1):
            if i-d>=0:
                grafo[(a,i)].append(((b,i-d),0))#costo 0 porque ya compre gasolina
    print(grafo)
    distancias = dijkstra(grafo, (s, 0))#parto sin gasolina
    mejor = min(distancias.get((e, g), float('inf')) for g in range(c + 1))
    print(mejor if mejor != float('inf') else "impossible")
                    
