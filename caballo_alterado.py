import sys

T=int(sys.stdin.readline().strip())
def determinar_movieminto_valido(mapa,R,C,M,N,x,y):
    if x>=0 and x<R and y>=0 and y<C:
        if mapa[x][y]==0:
            return True
        else:
            return False
    else:
        return False
def dfs(mapa,R,C,M,N,x,y,visitados,pares,impares):
    visitados[x][y]=True
    movimientos=[(M,N),(M,-N),(-M,N),(-M,-N),(N,M),(N,-M),(-N,M),(-N,-M)]
    movimientos_validos=[]
    for movimiento in movimientos:
        nuevo_x=x+movimiento[0]
        nuevo_y=y+movimiento[1]
        if determinar_movieminto_valido(mapa,R,C,M,N,nuevo_x,nuevo_y) and (nuevo_x,nuevo_y) not in movimientos_validos:
            movimientos_validos.append((nuevo_x,nuevo_y))
    if len(movimientos_validos)%2==0:
        pares[0]+=1
    else:
        impares[0]+=1
    for nuevo_x,nuevo_y in movimientos_validos:
        if not visitados[nuevo_x][nuevo_y]:
            dfs(mapa,R,C,M,N,nuevo_x,nuevo_y,visitados,pares,impares)
            
        
    

respuestas=[]    
for _ in range(T):
    R,C,M,N=map(int,sys.stdin.readline().strip().split())
    mapa=[[0 for i in range(C)] for i in range(R)]
    a=int(sys.stdin.readline().strip())
    for agua in range(a):
        x,y=map(int,sys.stdin.readline().strip().split())
        mapa[x][y]=1
    
    visitados=[[False for i in range(C)] for i in range(R)]
    pares=[0]
    impares=[0]
    dfs(mapa,R,C,M,N,0,0,visitados,pares,impares)
    respuestas.append([pares[0],impares[0]])
for i,respuesta in enumerate(respuestas):
    print("Caso %d: %d %d" %(i+1,respuesta[0],respuesta[1]))
    
