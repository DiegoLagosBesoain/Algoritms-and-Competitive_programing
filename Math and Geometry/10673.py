from dataclasses import dataclass
from typing import List
import math
import sys
from itertools import *
from itertools import islice, cycle
def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

def lcm(a, b):
    return a * (b / gcd(a, b))
def extended_euclid(a, b):
    if b == 0:
        return (1, 0, a)
    x, y, d = extended_euclid(b, a % b)
    return (y, x - (a // b) * y, d)

def extended_euclid(a, b):
    if b == 0:
        return 1, 0, a
    x1, y1, g = extended_euclid(b, a % b)
    return y1, x1 - (a // b) * y1, g

def encontrar_p_q( x, a, b):
    x0, y0, g = extended_euclid(a, b)

    if x % g != 0:
        return "failed"
    
    
    factor = x // g
    x0 *= factor
    y0 *= factor

    
    step = b // g
    k_min = (-x0 // step) if x0 < 0 else -(x0 // step)
    k_max = (y0 // (a // g)) if y0 >= 0 else ((y0 // (a // g)) - 1)
    
    
    for k in range(k_min, k_max + 1):
        p = x0 + k * step
        q = y0 - k * (a // g)
        return p, q  
    
    return "failed"


            
            


N = int(sys.stdin.readline())
resultados=[]
for i in range(N):
    l=sys.stdin.readline().split()
    x=int(l[0])
    k=int(l[1])
    ski=math.ceil(x/k)
    flo=math.floor(x/k)
    resultados.append(encontrar_p_q(x,ski,flo))
print(resultados)
for i,j in resultados:
    print(f"{i} {j}")
    