



def backtraking_matriz(matriz,fila,columna,suma_actual,suma_minima,secuencia_actual,secuencia_minima):
    if columna==len(matriz[0])-1:
        
        if suma_actual<suma_minima[0]:
            suma_minima[0]=suma_actual
            secuencia_minima[0]=secuencia_actual.copy()
        return
    else:
        #movimiento hacia arriba
        pisoarriba=fila-1
        if(pisoarriba<0):
            pisoarriba=len(matriz)-1
        if suma_actual+matriz[pisoarriba][columna+1]>suma_minima[0]:
            pass
        else:
            siguiente_secuencia=secuencia_actual.copy()
            siguiente_secuencia.append(pisoarriba+1)
            backtraking_matriz(matriz,pisoarriba,columna+1,suma_actual+matriz[pisoarriba][columna+1],suma_minima,siguiente_secuencia,secuencia_minima)
        #movimiento recto
        if suma_actual+matriz[fila][columna+1]>suma_minima[0]:
            pass
        else:
            siguiente_secuencia=secuencia_actual.copy()
            siguiente_secuencia.append(fila+1)
            backtraking_matriz(matriz,fila,columna+1,suma_actual+matriz[fila][columna+1],suma_minima,siguiente_secuencia,secuencia_minima)
        
        #movimiento hacia abajo    
        pisoabajo=fila+1
        if(pisoabajo>len(matriz)-1):
            pisoabajo=0
        if suma_actual+matriz[pisoabajo][columna+1]>suma_minima[0]:
            pass
        else:
            siguiente_secuencia=secuencia_actual.copy()
            siguiente_secuencia.append(pisoabajo+1)
            backtraking_matriz(matriz,pisoabajo,columna+1,suma_actual+matriz[pisoabajo][columna+1],suma_minima,siguiente_secuencia,secuencia_minima)
    return



def trabajar_matriz(matriz,suma_minima,secuencia_minima):
    for i,fila in enumerate(matriz):
        backtraking_matriz(matriz,i,0,fila[0],suma_minima,[i+1],secuencia_minima)
matrices = []
    
try:
    while True:
        # Lee las dimensiones de la matriz (m x n)
        m, n = map(int, input().split())
        matrix = []
        # Lee los valores de la matriz en orden por filas
        for _ in range(m):
            row = list(map(int, input().split()))
            matrix.append(row)
        matrices.append((m, n, matrix))
        min_suma=[float("inf")]
        min_conjunto=[[]]
        trabajar_matriz(matrix,min_suma,min_conjunto)
        print(min_suma,min_conjunto)

except EOFError:
    for matriz in matrices:
        min_suma=[0]
        min_conjunto=[[]]
        trabajar_matriz(matriz,min_suma,min_conjunto)
        print(min_suma,min_conjunto)



    
