import sys
import math
import functools
sys.setrecursionlimit(10000)

@functools.lru_cache(None)
def CoinChange_dos_valores_posibles(monedas,valor,e,p):
    if abs(valor-math.sqrt((e)**2+p**2))<1e-9:
        return 0
    if valor<math.sqrt((e)**2+p**2):
        return float("inf")
    menor=float("inf")
    for c in monedas:
        menor=min(menor,CoinChange_dos_valores_posibles(monedas,valor,e+c[0],p+c[1]))

    return menor+1
t=int(sys.stdin.readline().strip())

for caso in range(t):
    tipos, valor= map(int,sys.stdin.readline().strip().split())
    monedas=[]
    for moneda in range(tipos):
        e,p = map(int,sys.stdin.readline().strip().split())
        monedas.append((e,p))
    cantidad=CoinChange_dos_valores_posibles(tuple(monedas),valor,0,0)
    if cantidad==float("inf"):
        print("not possible")
    else:
        print(cantidad)
    
    