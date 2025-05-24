import sys
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
def primos_hasta_N(N):
    primos=[]
    for i,p in enumerate(primes()):
        if p > N:
            break
        primos.append(p)
        
    return primos
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
def is_prime(n):
    
    if n < 2:
        return False
    # Casos pequeños
    for p in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29):
        if n == p:
            return True
        if n % p == 0:
            return False

    
    d = n - 1
    s = 0
    while d % 2 == 0:
        s += 1
        d //= 2

    
    for a in (2, 325, 9375, 28178, 450775, 9780504, 1795265022):
        
        if a % n == 0:
            continue
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(s - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True


primos=primos_hasta_N(1120)
tabla_de_sumas=[[0]*15 for i in range(1121)]
tabla_de_sumas[0][0]=1


for primo in primos:
    for suma in range(1120,primo-1,-1):
        for cantidad in range(14,0,-1):
            tabla_de_sumas[suma][cantidad]+=tabla_de_sumas[suma-primo][cantidad-1]
n,k=map(int,sys.stdin.readline().strip().split())
while n!=0 and k!=0:
    print(tabla_de_sumas[n][k])
    n,k=map(int,sys.stdin.readline().strip().split())

