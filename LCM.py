from itertools import *
import sys
from math import gcd, isqrt
numeros=[]

line = int(sys.stdin.readline())
def lcm(a, b):
    return a * (b // gcd(a, b))
revisados=[]
def encontrar_mcl(numero):
    min_suma = numero + 1
    min_suma = min(min_suma, 1 + numero)
    for a in range(1, isqrt(numero) + 1):
        if numero % a == 0:
            b = numero // a
            if lcm(a, b) == numero and a != b:
                min_suma = min(min_suma, a + b)
    return min_suma 
                
            
    

while line !=0:
    numeros.append(int(line))
    line = int(sys.stdin.readline())
for i, numero in enumerate(numeros):
    print(f"Case {i+1}: {encontrar_mcl(numero)}")
