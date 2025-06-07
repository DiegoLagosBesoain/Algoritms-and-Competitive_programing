import sys
import functools


@functools.lru_cache(None)
def knapsack(dinero_acumulado, indice, M, objetos):
    if indice == len(objetos):
        
        if M > 1800 and dinero_acumulado > M and dinero_acumulado <= 2000:
            return float("-inf")
        return 0

    if dinero_acumulado > M + 200:
        return float('-inf')

    tomar = objetos[indice][1] + knapsack(dinero_acumulado + objetos[indice][0], indice + 1, M, objetos)
    no_tomar = knapsack(dinero_acumulado, indice + 1, M, objetos)

    return max(tomar, no_tomar)

especificaciones = sys.stdin.readline().strip()

while especificaciones !="":
    dinero, items = map(int, especificaciones.split())
    lista=[]
    for _ in range(items):
        lista.append(tuple(map(int, sys.stdin.readline().strip().split())))
    print(knapsack(0,0,dinero,tuple(lista)))
    especificaciones = sys.stdin.readline().strip() 