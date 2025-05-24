import sys
def revisar_diagonal_positiva(tablero,posicion):
    i = posicion.copy()
    j = posicion.copy()
    while(i[1]<8 and i[0]>=0):
        if(tablero[i[0]][i[1]]==1):
            return False
        i[0]-=1
        i[1]+=1
    while(j[1]>=0 and j[0]<8):
        print(j[0],j[1])
        if(tablero[j[0]][j[1]]==1):
            return False
        j[0]+=1
        j[1]-=1
        
    return True
def revisar_diagonal_negativa(tablero,posicion):
    i = posicion.copy()
    j = posicion.copy()
    while(i[1]>=0 and i[0]>=0):
        if(tablero[i[0]][i[1]]==1):
            return False
        i[0]-=1
        i[1]-=1
    while(j[1]<8 and j[0]<8):
        if(tablero[j[0]][j[1]]==1):
            return False
        j[0]+=1
        j[1]+=1
    return True
def revisar_validez(tablero,posicion,verticales,horizontales):
    if horizontales[posicion[0]]:
        return False
    if verticales[posicion[1]]:
        return False
    if not revisar_diagonal_positiva(tablero,posicion):
        return False
    if not revisar_diagonal_negativa(tablero,posicion):
        return False
    return True
def backtaking_reinas(tablero,verticales,horizontales,soluciones,Actual):
    print(horizontales)
    if Actual==9:
        soluciones.append([row[:] for row in tablero])
        return
    if(horizontales[Actual-1]):
        
        backtaking_reinas(tablero,verticales,horizontales,soluciones,Actual+1)
        
    else:
        for i in range(8):
            
            if revisar_validez(tablero,[Actual-1,i],verticales,horizontales):
                print("entre",Actual-1,i)
                tablero[Actual-1][i]=1
                horizontales[Actual-1]=True
                verticales[i]=True
                backtaking_reinas(tablero,verticales,horizontales,soluciones,Actual+1)
                tablero[Actual-1][i]=0
                horizontales[Actual-1]=False
                verticales[i]=False

                

    
def matriz_ceros(filas, columnas):
    return [[0 for _ in range(columnas)] for _ in range(filas)]
N=int(sys.stdin.readline())
soluciones_totales=[]
for _ in range(N):
    sys.stdin.readline()
    tablero=matriz_ceros(8,8)
    x,y=map(int,sys.stdin.readline().strip().split())
    
    tablero[x-1][y-1]=1
    
    horizontales=[False for i in range(8)]
    horizontales[x-1]=True
    verticales=[False for i in range(8)]
    verticales[y-1]=True
    print(horizontales)
    soluciones=[]
    backtaking_reinas(tablero,verticales,horizontales,soluciones,1)
    for s in soluciones:
        for fila in s:
            print(" ".join(str(x) for x in fila))
        print()







                    
    
