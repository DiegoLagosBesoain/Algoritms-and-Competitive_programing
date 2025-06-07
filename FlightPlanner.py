import sys
import functools

t = int(sys.stdin.readline())
sys.stdin.readline()  

@functools.lru_cache(None)
def mejor_trayecto(col, alt, matriz):
    
    if col < 0 and alt == 9:
        return 0
    if col < 0 and alt != 9:
        return float("inf")

    viento = matriz[alt][col]

    opciones = []

    
    opciones.append(mejor_trayecto(col - 1, alt, matriz) + 30 - viento)

    
    if alt > 0:
        opciones.append(mejor_trayecto(col - 1, alt - 1, matriz) + 60 - viento)

    
    if alt < 9:
        opciones.append(mejor_trayecto(col - 1, alt + 1, matriz) + 20 - viento)

    return min(opciones)

for _ in range(t):
    distancia = int(sys.stdin.readline())
    N = distancia // 100  
    matriz = []

    for _ in range(10):
        fila = tuple(map(int, sys.stdin.readline().split()))
        matriz.append(fila)

    matriz = tuple(matriz)  

    resultado = mejor_trayecto(N-1, 9, matriz)  
    print(resultado)
    sys.stdin.readline() 