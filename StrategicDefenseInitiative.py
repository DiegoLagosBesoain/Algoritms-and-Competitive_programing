import sys
import functools

@functools.lru_cache(None)
def LIS(lista,indice):
    if indice==0:
        return [lista[0]]
    else:
        mejor=[]
        for j in range(indice):
            if lista[j]<lista[indice]:
                subseq=LIS(lista,j)
                if len(subseq)>len(mejor):
                    mejor=subseq
    return mejor+[lista[indice]]

t=int(sys.stdin.readline().strip())
sys.stdin.readline().strip()
for caso in range(t):
    
    objetivos=[]
    objetivo=sys.stdin.readline().strip()
    while objetivo!="":
        objetivo=int(objetivo)
        objetivos.append(objetivo)
        objetivo=sys.stdin.readline().strip()
    aceirtos=LIS(tuple(objetivos),len(objetivos)-1)
    print(aceirtos,len(aceirtos))
    
