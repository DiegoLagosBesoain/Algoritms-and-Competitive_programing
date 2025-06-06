import sys

import functools

@functools.lru_cache(None)
def LIC(lista,indice):
    if indice==0:
        return 1
    return max(LIC(lista,j) +1 for j in range(indice) if lista[j]<lista[indice])


@functools.lru_cache(None)
def LIS(lista, indice):
    if indice == 0:
        return [lista[0]]
    mejor = []
    for j in range(indice):
        if lista[j] < lista[indice]:
            subseq = LIS(lista, j)
            if len(subseq) > len(mejor):
                mejor = subseq
    return mejor+[lista[indice]]

numero=sys.stdin.readline().strip()
lista=[]
while numero!="":
    numero=int(numero)
    lista.append(numero)
    numero=sys.stdin.readline().strip()
print(lista)
print(LIS(tuple(lista),len(lista)-1))

