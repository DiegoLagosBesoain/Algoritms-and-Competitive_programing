import sys

def bfs(grafo, partida, visitados):
    queue = [partida]
    visitados[partida] = True
    maxima_cantidad_de_vecinos=0
    dia=1
    dia_maximo=0
    amigos_actuales=[partida]
    while amigos_actuales:
        nuevos_amigos=[]
        boom_actual=0
        for amigo in amigos_actuales:

            nodo = amigo
            
            for vecino in grafo[nodo]:
                
                if not visitados[vecino]:
                    boom_actual+=1
                    visitados[vecino] = True
                    nuevos_amigos.append(vecino)
        amigos_actuales=nuevos_amigos
                
        if boom_actual>maxima_cantidad_de_vecinos:
            maxima_cantidad_de_vecinos=boom_actual
            dia_maximo=dia
        dia+=1
    return maxima_cantidad_de_vecinos, dia_maximo   

N=int(sys.stdin.readline().strip())
grafo=[[] for _ in range(N)]
for i in range(N):
    amigo=list(map(int,sys.stdin.readline().strip().split()))[1:]
    grafo[i]=amigo
Q=int(sys.stdin.readline().strip())

respuestas=[]
for i in range(Q):
    partida=int(sys.stdin.readline().strip())
    visitados=[False]*N
    maxima_cantidad_de_vecinos, dia_maximo=bfs(grafo, partida, visitados)
    if maxima_cantidad_de_vecinos==0:
        respuestas.append("0")
    else:
        respuestas.append(str(maxima_cantidad_de_vecinos)+" "+str(dia_maximo))
for respuesta in respuestas:
    print(respuesta)
