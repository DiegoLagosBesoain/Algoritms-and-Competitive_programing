import sys
import functools


@functools.lru_cache(None)
def maxima_secuencia(alturas,indice):
    if indice==0:
        return 1
    opciones = [maxima_secuencia(alturas, j) + 1 for j in range(indice) if alturas[j] > alturas[indice]]
    return max(opciones) if opciones else 1
altura=int(sys.stdin.readline().strip())
while altura !=-1:
    alturas=[]
    while altura !=-1:
        alturas.append(altura)
        altura=int(sys.stdin.readline().strip())
    
    maximo = max(maxima_secuencia(tuple(alturas), i) for i in range(len(alturas)))
    print("maximas", maximo)
    


    altura=int(sys.stdin.readline().strip())