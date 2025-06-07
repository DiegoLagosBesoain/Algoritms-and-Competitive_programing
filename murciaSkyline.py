import sys
import functools


#aqui esta tratando de buscar la mejor secuencia terminada en indice, eso pasa cuando buscamos algo diferente de la cantidad
@functools.lru_cache(None)
def LIS(edificios, indice):
    if indice==0:
        return edificios[indice][1]
    mejor = 0
    for j in range(indice):
        if edificios[j][0] < edificios[indice][0]:
            mejor = max(mejor, LIS(edificios, j))
    return mejor + edificios[indice][1]

@functools.lru_cache(None)
def LDS(edificios, indice):
    if indice==0:
        return edificios[indice][1]
    mejor = 0
    for j in range(indice):
        if edificios[j][0] > edificios[indice][0]:
            mejor = max(mejor, LDS(edificios, j))
    return mejor + edificios[indice][1]
t=int(sys.stdin.readline().strip())
for case in range(t):
    n=int(sys.stdin.readline().strip())
    altura_edificios=list(map(int,sys.stdin.readline().strip().split()))
    ancho_edificios=list(map(int,sys.stdin.readline().strip().split()))
    edificios=[]
    for i, altura in enumerate(altura_edificios):
        edificios.append((altura,ancho_edificios[i]))
    print(edificios)
    maximo=float("-inf")
    
    mejor_total = 0
    for i in range(len(edificios)):
        mejor_total = max(mejor_total, LIS(tuple(edificios), i))
    mejor_total_decreciente = 0
    for i in range(len(edificios)):
         mejor_total_decreciente = max( mejor_total_decreciente, LDS(tuple(edificios), i))

    print(mejor_total)
    print(mejor_total_decreciente)
