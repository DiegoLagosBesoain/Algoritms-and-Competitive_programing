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


def verificar_linea(linea,numero_objetivo):
    if(not all(n != None for n in linea)):
        return True
    if(linea[0]==0):
        return False
    
    if(sum(linea)!=numero_objetivo):
        return False
    numero_primo=int(''.join(map(str, linea)))
    if(not is_prime(numero_primo)):
        return False
    return True

def verificar_diagonales(matriz,numero_objetivo):
    diagonal_principal = [matriz[i][i] for i in range(5)]
    
    diagonal_secundaria = [matriz[4 - i][i] for i in range(5)]
    
    return verificar_linea(diagonal_principal,numero_objetivo) and verificar_linea(diagonal_secundaria,numero_objetivo)


def verificar_horizontal(matriz,fila,numero_objetivo):
    
    return  verificar_linea(matriz[fila],numero_objetivo)

def verificar_columna(matriz,columna,numero_objetivo):
    columna=[matriz[i][columna] for i in range(5)]
    
    return verificar_linea(columna,numero_objetivo)


def backtraking_numero_primos(matriz,numero_objetivo,soluciones,fila,columna):
    
    print(matriz)
    for i in range(10):
        
        matriz[fila][columna]=i 
        suma1 = sum(n if n is not None else 0 for n in matriz[fila])
        columna1=[matriz[i][columna] for i in range(5)]
        suma2=sum(n if n is not None else 0 for n in columna1)
        diagonal_principal = [matriz[i][i] for i in range(5)]
        

        diagonal_secundaria = [matriz[4 - i][i] for i in range(5)]
        suma3=sum(n if n is not None else 0 for n in diagonal_principal)
        suma4=sum(n if n is not None else 0 for n in diagonal_secundaria)
        if suma1>numero_objetivo or suma2>numero_objetivo or suma3>numero_objetivo or suma4>numero_objetivo:
            matriz[fila][columna] = None
            break
            

        factible=True
        if fila==4 and (columna==0 or columna==4):
            if not verificar_diagonales(matriz,numero_objetivo):
                factible=False
                matriz[fila][columna] = None
                
                
                
                
        if fila==4:
            if not verificar_columna(matriz,columna,numero_objetivo):
                factible=False
                matriz[fila][columna] = None
        if columna==4:
            if not verificar_horizontal(matriz,fila,numero_objetivo):
                factible=False
                
                
        
        if factible:
            if  fila==4 and columna==4:
                print("entre")
                soluciones.append(copy.deepcopy(matriz))
            elif fila<4 and columna==4:
                
                backtraking_numero_primos(matriz,numero_objetivo,soluciones,fila+1,0)
                matriz[fila][columna] = None
            else:
                backtraking_numero_primos(matriz,numero_objetivo,soluciones,fila,columna+1)
                matriz[fila][columna] = None
        matriz[fila][columna] = None
                
                

        



        
        








number=int(sys.stdin.readline().strip())
inicio=int(sys.stdin.readline().strip())
Matriz[0][0]=inicio
soluciones=[]
backtraking_numero_primos(Matriz.copy(),number,soluciones,0,1)
print(soluciones)
