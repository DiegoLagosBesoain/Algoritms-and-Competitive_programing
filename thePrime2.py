from dataclasses import dataclass
from typing import List
import math
import sys
from itertools import *
from itertools import islice, cycle,takewhile
import copy
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
N=None
Matriz=[[N,N,N,N,N],
        [N,N,N,N,N],
        [N,N,N,N,N],
        [N,N,N,N,N],
        [N,N,N,N,N]]

def suma_digitos(n):
    return sum(int(d) for d in str(n))
def generar_primos_con_suma(suma_deseada):
    
    primos_validos = []
    for i in range(10_000, 100_000):  # 5 dígitos
        if suma_digitos(i) == suma_deseada and is_prime(i):
            primos_validos.append(i)
    return primos_validos
def backtraking_numero_primos(matriz,number,soluciones,fila,columna,lista_primos):
    
    if fila==5:
        soluciones.append([row[:] for row in matriz])
        return
    

    for primo in lista_primos:
        digitos = numero_a_lista(primo)
        if digitos not in matriz:
            
            matriz[fila][:] = digitos[:]
            if validar_matriz(matriz,number,fila):
                
                backtraking_numero_primos(matriz,number,soluciones,fila+1,columna,lista_primos)
            matriz[fila][:] = [None]*5  

def lista_a_numero(l):
    return int(''.join(map(str, l)))

def numero_a_lista(n):
    return [int(d) for d in str(n)]
def validar_matriz(matriz, numero_objetivo, fila):
    suma_diag1 = suma_diag2 = 0
    for i in range(fila + 1):
        if matriz[i][i] is not None:
            suma_diag1 += matriz[i][i]
        if matriz[i][4 - i] is not None:
            suma_diag2 += matriz[i][4 - i]
        if suma_diag1 > numero_objetivo or suma_diag2 > numero_objetivo:
            return False

    if fila == 4:
        if suma_diag1 != numero_objetivo or suma_diag2 != numero_objetivo:
            return False
        diag1 = lista_a_numero([matriz[i][i] for i in range(5)])
        diag2 = lista_a_numero([matriz[i][4 - i] for i in range(5)])
        return is_prime(diag1) and is_prime(diag2)

    return True
number=int(sys.stdin.readline().strip())
inicio=int(sys.stdin.readline().strip())
Matriz[0][0]=inicio
soluciones=[]
total_primos=generar_primos_con_suma(11)
print(total_primos)
print(len(total_primos))
primos_filtrados = [p for p in total_primos if str(p).startswith(str(inicio))]
print(primos_filtrados)
for primo in primos_filtrados:
    Matriz[0]=numero_a_lista(primo)
    backtraking_numero_primos(Matriz,number,soluciones,1,0,total_primos)

print(soluciones)