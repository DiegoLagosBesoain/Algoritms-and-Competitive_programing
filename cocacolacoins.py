import sys
from itertools import product
import functools

@functools.lru_cache(None)
def coins(precio,n1,n5,n10):#problema de monedas con cantidades limitadas
    if precio==0:
        return 0
    if precio<0:
        return float("inf")
    menor=float("inf")
    if n1>0:
        menor=min(menor,coins(precio-1,n1-1,n5,n10))
    if n5>0:
        menor=min(menor,coins(precio-5,n1,n5-1,n10))
    if n10>0:
        menor=min(menor,coins(precio-10,n1,n5,n10-1))
    return menor +1

def vuelto_monedas(valor):
    if valor==0:
        return 0
    if valor<0:
        return float("inf")
    tipos=[1,5]
    return min(vuelto_monedas(valor-tipo) for tipo in tipos)+1


t = int(sys.stdin.readline())

for _ in range(t):
    C, n1, n5, n10 = map(int, sys.stdin.readline().split())

    total_monedas_usadas = 0

    for _ in range(C):
        mejor = float("inf")
        mejor_a = mejor_b = mejor_c = 0

        # Explorar TODAS las combinaciones posibles que paguen al menos 8
        for a in range(min(8, n1) + 1):           # monedas de 1, no necesitas más de 8
            for b in range(min(8 // 5 + 1, n5 + 1)):  # monedas de 5
                for c in range(min(8 // 10 + 2, n10 + 1)): # monedas de 10 (aunque no haya)
                    pago = a * 1 + b * 5 + c * 10
                    if pago < 8:
                        continue
                    if a > n1 or b > n5 or c > n10:
                        continue
                    usadas = a + b + c
                    if usadas < mejor:
                        mejor = usadas
                        mejor_a, mejor_b, mejor_c = a, b, c

        # Usar esas monedas
        n1 -= mejor_a
        n5 -= mejor_b
        n10 -= mejor_c
        pago = mejor_a * 1 + mejor_b * 5 + mejor_c * 10
        cambio = pago - 8

        # Recibir cambio (máximo en monedas de 5)
        n5 += cambio // 5
        n1 += cambio % 5

        total_monedas_usadas += mejor

    print(total_monedas_usadas)
        
    
