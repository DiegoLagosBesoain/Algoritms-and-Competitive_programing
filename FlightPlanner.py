import sys
import functools
t = int(sys.stdin.readline())
sys.stdin.readline()  

def mejor_trayecto(col, alt, N, matriz):
    if alt < 0 or alt > 9 or col < 0 or col > N:
        return float('inf')

    if col == 0 and alt == 0:
        return 0

    opciones = []

    viento = matriz[alt][col - 1]  

    
    if alt > 0:
        opciones.append(mejor_trayecto(col - 1, alt - 1, N, matriz) + 60 + viento)

    
        opciones.append(mejor_trayecto(col - 1, alt, N, matriz) + 30 + viento)

    
    if alt < 9:
        opciones.append(mejor_trayecto(col - 1, alt + 1, N, matriz) + 20 + viento)

    return min(opciones)
for _ in range(t):
    distancia = int(sys.stdin.readline())
    N = distancia // 100  
    matriz = []

    for _ in range(10):
        fila = tuple(map(int, sys.stdin.readline().split()))
        matriz.append(fila)

    print(tuple(matriz)) 
    print(mejor_trayecto(N,0,N,tuple(matriz)))
    
    dp = [[float('inf')] * (N + 1) for _ in range(10)]
    dp[0][0] = 0  

    for col in range(1, N + 1):
        for alt in range(10):
            opciones = []

           
            if alt < 9:
                opciones.append(dp[alt + 1][col - 1] + 20 - matriz[alt][col - 1])

            
            opciones.append(dp[alt][col - 1] + 30 - matriz[alt][col - 1])

            
            if alt > 0:
                opciones.append(dp[alt - 1][col - 1] + 60 - matriz[alt][col - 1])

            dp[alt][col] = min(opciones)

    print(dp[0][N])
