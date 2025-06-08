import sys
import math
import functools

@functools.lru_cache(None)
def knapsack_divisorio(numeros,divisor,cantidad,suma,indice):
    
    if indice == len(numeros):
        print(suma)
        return int(cantidad == 0 and suma % divisor == 0)
    else:
        total=0
        total+=knapsack_divisorio(numeros,divisor, cantidad,suma,indice+1)
        if cantidad > 0:
            total+=knapsack_divisorio(numeros,divisor, cantidad-1, suma+numeros[indice] , indice+1)
        return total

N,Q=map(int,sys.stdin.readline().strip().split())


while N!=0 and Q!=0:
    numeros=[]
    for _ in range(N):
        numeros.append(int(sys.stdin.readline().strip()))
    querys=[]
    for _ in range(Q):
        querys.append(list(map(int,sys.stdin.readline().strip().split())))
    for i,query in enumerate(querys):
        print(f"query {i}",knapsack_divisorio(tuple(numeros),query[0],query[1],0,0))
    N,Q=map(int,sys.stdin.readline().strip().split())


    