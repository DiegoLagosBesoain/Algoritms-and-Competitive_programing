import sys


def mejor_segmento(segmentos, fin):
    if fin < 0:
        return (0, -1, -1)  
    mejor_anterior=mejor_segmento(segmentos, fin - 1)
    if mejor_anterior[0]<=0:
        return (segmentos[fin], fin, fin) 
    nueva_suma=mejor_anterior[0]+segmentos[fin]
    return (nueva_suma,mejor_anterior[1],fin)
    
    


t = int(sys.stdin.readline())
for caso in range(t):
    n = int(sys.stdin.readline())
    segmentos = [int(sys.stdin.readline()) for _ in range(n - 1)]
    mejor_suma = float('-inf')
    mejor_inicio = mejor_fin = -1
    for i in range(len(segmentos)):
        suma,ini,fin=mejor_segmento(segmentos, i)
        largo=fin-ini
        mejor_largo=mejor_fin-mejor_inicio
        if (suma > mejor_suma or(suma==mejor_suma and largo>mejor_largo) or(suma==mejor_suma and largo==mejor_largo and ini<mejor_inicio)):
            mejor_suma= suma
            mejor_inicio= ini
            mejor_fin =fin

    if mejor_suma <= 0:
        print(f"Route {caso} has no nice parts")
    else:
        print(f"The nicest part of route {caso} is between stops {mejor_inicio + 1} and {mejor_fin + 2}")