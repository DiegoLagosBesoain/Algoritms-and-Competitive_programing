import sys
from math import gcd

def extended_gcd(a, b):
    
    if b == 0:
        return a, 1, 0
    g, x1, y1 = extended_gcd(b, a % b)
    return g, y1, x1 - (a // b) * y1

def encontrar_min_costo(n1, n2, c1, c2, N):
    g, x0, y0 = extended_gcd(n1, n2)
    
    if N % g != 0:
        return "failed"  
    
    
    factor = N // g
    x0 *= factor
    y0 *= factor
    
    
    step = n2 // g
    k_min = (-(x0 // step)) if x0 < 0 else (-x0 // step)
    k_max = (y0 // (n1 // g)) if y0 >= 0 else ((y0 // (n1 // g)) - 1)
    
    soluciones = []
    for k in range(k_min, k_max + 1):
        x = x0 + k * step
        y = y0 - k * (n1 // g)
        if x > 0 and y > 0:
            soluciones.append((x, y))
    
    if not soluciones:
        return "failed"
    
    
    mejor_x, mejor_y = min(soluciones, key=lambda t: c1 * t[0] + c2 * t[1])
    return f"{mejor_x} {mejor_y}"

N = int(sys.stdin.readline())
resultados = []
while N != 0:
    c1, n1 = map(int, sys.stdin.readline().split())
    c2, n2 = map(int, sys.stdin.readline().split())
    resultados.append(encontrar_min_costo(n1, n2, c1, c2, N))
    N = int(sys.stdin.readline())
    
for res in resultados:
    print(res)

