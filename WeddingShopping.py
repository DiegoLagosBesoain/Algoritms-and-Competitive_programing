import sys

def knapsac_cambiado(catalogo,M,peso_actual,fila,maximo):
    if peso_actual>M:
        return 
    if fila==len(catalogo):
        maximo[0]=max(maximo[0],peso_actual)
        return
    for i in range(len(catalogo[fila])):
        knapsac_cambiado(catalogo,M,peso_actual+catalogo[fila][i],fila+1,maximo)



t=int(sys.stdin.readline().strip())
for case in range(t):
    M,C=map(int,sys.stdin.readline().strip().split())
    catalogo=[]
    for prenda in range(C):
        catalogo.append(tuple(map(int,sys.stdin.readline().strip().split()))[1:])
    maximo=[float("-inf")]
    knapsac_cambiado(catalogo,M,0,0,maximo)
    if maximo[0]==float("-inf"):
        print("no solution")
    else:
        print(maximo[0])

