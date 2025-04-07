from itertools import *
import sys
from math import gcd, isqrt, lcm as lcm1
min_suma=[]
numeros=[]
line = int(sys.stdin.readline())
def econtrar_divisores(numero):
    divisors = []
    for i in range(2, isqrt(numero) + 1):
        if numero % i == 0:
            divisors.append(i)
            divisors.append(numero // i)
    divisors.sort(reverse=True)
    return divisors
def encontrar_min_sum_mcl_con_backtraking(numero, divisores):
    
    min_suma = [numero + 1]  
    memo = {}  

    for i, divisor in enumerate(divisores):
        buscar_min_suma(numero, i, divisores, [divisor], divisor, min_suma, memo)

    return min_suma[0]

def buscar_min_suma(numero, indice_divisores, divisores, conjunto_actual, lcm_actual, min_suma, memo):
   
    suma_actual = sum(conjunto_actual)

    
    if suma_actual >= min_suma[0]:
        return

    
    if lcm_actual > numero:
        return

    
    if lcm_actual == numero:
        min_suma[0] =min(suma_actual,min_suma[0])
        return

    
    clave = (indice_divisores, lcm_actual)
    if clave in memo and memo[clave] <= suma_actual:
        return
    memo[clave] = suma_actual

    
    for i in range(indice_divisores, len(divisores)):
        nuevo_divisor = divisores[i]
        nuevo_suma = suma_actual + nuevo_divisor

        
        if nuevo_suma >= min_suma[0]:
            continue

        nuevo_lcm = lcm1(lcm_actual, nuevo_divisor)

        
        if nuevo_lcm > numero:
            continue
        if(len(conjunto_actual)==4):
            continue  

        
        buscar_min_suma(numero, i, divisores, conjunto_actual + [nuevo_divisor], nuevo_lcm, min_suma, memo)



#la dejo por si la tengo que usar en vez del backtraking
def encontrar_min_sum_mcl(numero,divisores):
    min_suma[0] = numero+1
    for k in range(1,len(divisores)+1):
        for combinacion in combinations(divisores,k):
            if lcm1(*combinacion)==numero:
                min_suma=min(min_suma,sum(combinacion))        

            
    

while line !=0:
    numeros.append(int(line))
    line = int(sys.stdin.readline())
for i, numero in enumerate(numeros):
    divisores=econtrar_divisores(numero)
    print(f"Case {i+1}: {encontrar_min_sum_mcl_con_backtraking(numero,divisores)}")
