import sys
import functools
@functools.lru_cache(None)
def Max_product(arreglo,indice):
    if indice==0:
        return arreglo[0]
    return max(Max_product(arreglo,indice-1)*arreglo[indice],arreglo[indice])

entrada=sys.stdin.readline().strip()
while entrada!="":
    numeros=list(map(int,entrada.split()))
    numeros.pop()
    print(Max_product(tuple(numeros),len(numeros)-1))
    entrada=sys.stdin.readline().strip()