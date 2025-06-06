import sys
import bisect
def mejor_tren(autos):
    n = len(autos)
    maximo = 0
    LIS = []  
    LDS = []  
    for i in range(n-1,-1,-1):
        pos_lds = bisect.bisect_left(LDS, autos[i])
        if pos_lds == len(LDS):
            LDS.append(autos[i])
        else:
            LDS[pos_lds] = autos[i]
        len_lds = pos_lds + 1

        
        pos_lis = bisect.bisect_left(LIS, -autos[i])
        if pos_lis == len(LIS):
            LIS.append(-autos[i])
        else:
            LIS[pos_lis] = -autos[i]
        len_lis = pos_lis + 1

        maximo = max(maximo, len_lis + len_lds - 1)

    return maximo


t = int(sys.stdin.readline())
resultados = []

for _ in range(t):
    n = int(sys.stdin.readline())
    if n<1:
        resultados.append(n)
    else:
        autos=[]
        for _ in range(n):
            autos.append(int(sys.stdin.readline()))
        resultados.append(mejor_tren(autos))

# Salida
for r in resultados:
    print(r)