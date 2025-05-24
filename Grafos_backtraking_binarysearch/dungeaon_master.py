import sys



def dfs(mazmorra, visitados, i, j, k,pasos_actuales,pasos_minimos,fin):
    if i== fin[0] and j == fin[1] and k == fin[2]:
        if pasos_minimos[0]==None or pasos_actuales < pasos_minimos[0]:
            pasos_minimos[0] = pasos_actuales
        return 
    if i < 0 or i >= len(mazmorra) or j < 0 or j >= len(mazmorra[0]) or k < 0 or k >= len(mazmorra[0][0]):
        return 
    if mazmorra[i][j][k] == 1 or visitados[i][j][k]:
        return False
    visitados[i][j][k] = True
    siguientes = [[i+1,j,k],[i-1,j,k],[i,j+1,k],[i,j-1,k],[i,j,k+1],[i,j,k-1]]
    for siguiente in siguientes:
        dfs(mazmorra, visitados, siguiente[0], siguiente[1], siguiente[2],pasos_actuales+1,pasos_minimos,fin)
    visitados[i][j][k] = False
    
    


pisos,filas,columnas=map(int,sys.stdin.readline().strip().split())
while pisos!=0 and filas!=0 and columnas!=0:
    
    mazmorra=[[[0 for _ in range(columnas)] for _ in range(filas)] for _ in range(pisos)]
    visitados=[[[False for _ in range(columnas)] for _ in range(filas)] for _ in range(pisos)]
    inicio=[0,0,0]
    fin=[0,0,0]
    for i in range(pisos):
        for j in range(filas):
            fila=list(sys.stdin.readline().strip())
            for k in range(columnas):
                if fila[k]=="S":
                    inicio=[i,j,k]
                elif fila[k]=="E":
                    fin=[i,j,k]
                elif fila[k]=="#":
                    mazmorra[i][j][k]=1
    pasos_minimos=[None]
    dfs(mazmorra,visitados,inicio[0],inicio[1],inicio[2],0,pasos_minimos,fin)
    if pasos_minimos[0] == None:
        print("Trapped!")
    else:
        print(f"Escaped in {pasos_minimos[0]} minute(s).")
    print(mazmorra)
    pisos,filas,columnas=map(int,sys.stdin.readline().strip().split())
    