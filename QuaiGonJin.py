import sys
import functools

T = int(sys.stdin.readline().strip())

@functools.lru_cache(None)
def knapsack(indice, tiempo_usado):
    if indice == len(canciones):
        return (0, tiempo_usado)  

    
    sin_tomar = knapsack(indice + 1, tiempo_usado)

    
    mejor = sin_tomar
    duracion = canciones[indice]
    if tiempo_usado + duracion <= tiempo_limite:
        con_tomar = knapsack(indice + 1, tiempo_usado + duracion)
        con_tomar = (con_tomar[0] + 1, con_tomar[1])  

        
        if con_tomar[0] > sin_tomar[0]:
            mejor = con_tomar
        elif con_tomar[0] == sin_tomar[0] and con_tomar[1] > sin_tomar[1]:
            mejor = con_tomar

    return mejor

for _ in range(T):
    n, t = map(int, sys.stdin.readline().strip().split())
    canciones = tuple(map(int, sys.stdin.readline().strip().split()))
    tiempo_limite = t - 1  
    knapsack.cache_clear()

    cantidad, tiempo_usado = knapsack(0, 0)
    print(cantidad + 1, tiempo_usado + 678) 