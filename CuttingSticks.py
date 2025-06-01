import sys
import functools
@functools.lru_cache(None)
def calcular_costo_corte(i, j):
    if i+1>= j:
        return 0  
    mejor = float('inf')
    for k in range(i+1, j):
        costo = calcular_costo_corte(i, k) + calcular_costo_corte(k, j) + (cortes[j] - cortes[i])
        mejor = min(mejor, costo)
    return mejor
largo=int(sys.stdin.readline().strip())
while largo!=0:
    cantidad_de_cortes=int(sys.stdin.readline().strip())

    cortes=tuple([0]+list(map(int,sys.stdin.readline().strip().split()))+[largo])
    print(cortes)
    print(calcular_costo_corte(0, len(cortes)- 1))
    calcular_costo_corte.cache_clear()
    largo=int(sys.stdin.readline().strip())