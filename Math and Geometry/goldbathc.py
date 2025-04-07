from dataclasses import dataclass
from typing import List
import math
import sys
from itertools import *
from itertools import islice, cycle,takewhile
EPS = 1E-8
def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

def lcm(a, b):
    return a * (b / gcd(a, b))
def factorize(N):
    """
    division: a / b             e.g. 2 / 1 = 2.0 : float
    integer division: a // b    e.g. 2 // 1 = 2 : int
    remainder: a % b remainder of the integer division a / b = a // b + (a %
    4 % 2 = 0
    """
    sqN = math.sqrt(N)
    for p in primes(): # potentially infinite
        if p > sqN: # guarantees it ends
            yield N
            break
        while N % p == 0:
            yield p
            N //= p # N = N // p
            sqN = math.sqrt(N)
        if N == 1:
            break

def primes():
    i = 3
    prime_list = [2]
    yield 2
    while True:
        sqi = math.sqrt(i)
        if next((False for p in takewhile(lambda x: x <= sqi, prime_list) if i%p == 0), True):
            prime_list.append(i)
            yield i
        i += 2
print()
def primos_hasta_N(N):
    primos=[]
    for i,p in enumerate(primes()):
        if p > N:
            break
        primos.append(p)
        
    return primos
def determinar_goldbatch(N):
    primos=primos_hasta_N(N)
    for i in primos:
        resto=N-i
        if resto in primos:
            return i , resto

N = int(sys.stdin.readline())
respuestas=[]
Numeros=[]

while N != 0 :
    Numeros.append(N)
    respuestas.append(determinar_goldbatch(N))
    N = int(sys.stdin.readline())
for i, j in enumerate(respuestas):
    print(f"{Numeros[i]} = {j[0]} + {j[1]}")





