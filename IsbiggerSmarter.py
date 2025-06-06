import sys
import functools

elefantes=[]
elefante=sys.stdin.readline().strip()

@functools.lru_cache(None)
def is_bigger_smarter(elefantes,indice):
    if indice==0:
        return [elefantes[0]]
    else:
        maximo=[]
        for j in range(indice):
            if elefantes[j][1]>elefantes[indice][1] and elefantes[j][0]<elefantes[indice][0]:
                if len(maximo)<len(is_bigger_smarter(elefantes,j)):
                    maximo=is_bigger_smarter(elefantes,j)
                
        return maximo + [elefantes[indice]]
i=1
while elefante!="":
    elefante=tuple(list(map(int,elefante.split()))+[i])
    elefantes.append(elefante)
    elefante=sys.stdin.readline().strip()
    i+=1
print(elefantes)
elefantes.sort(key=lambda x: x[0])
print(elefantes)
mejor = []
for i in range(len(elefantes)):
    actual = is_bigger_smarter(tuple(elefantes), i)
    if len(actual) >= len(mejor):
        mejor = actual
print(mejor)