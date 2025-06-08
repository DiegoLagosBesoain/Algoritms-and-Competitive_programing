import sys
import functools


@functools.lru_cache(None)
def LIS_desde_i(lista,indice):#el largo de la anticadena mas larga es igual a la cantidad minima de grupos que esten todos ordenados vamoooooos
    max_lis=1
    for j in range(indice+1, len(lista)):
        if lista[j][1] >= lista[indice][1]: 
            max_lis = max(max_lis, 1 + LIS_desde_i(lista,j))
    return max_lis 
t=int(sys.stdin.readline().strip())
for case in range(t):
    cantidad_de_muñecas=int(sys.stdin.readline().strip())
    linea=list(map(int,sys.stdin.readline().strip().split()))
    muñecas=[]
    for i in range(len(linea)//2):
        muñecas.append((linea[2*i],linea[2*i+1]))
    print(muñecas)

    muñecas.sort(key=lambda x: (-x[0], x[1]))
    resultado = 0
    #recordatorio para la prueba probar desde todos los inicios
    for i in range(len(muñecas)):
        resultado = max(resultado, LIS_desde_i(tuple(muñecas), i))
    print(resultado)