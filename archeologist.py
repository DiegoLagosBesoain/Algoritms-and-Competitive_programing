import sys
import math

def contar_digitos(n):
    
    if n == 0:
        return 1  
    return int(math.log10(abs(n))) + 1  

def primeros_n_digitos_log(potencia, largo):
    
    log_valor = potencia * math.log10(2)  
    fraccion_decimal = log_valor - math.floor(log_valor) 
    primeros_digitos = int(10**(fraccion_decimal + largo - 1))  
    
    return primeros_digitos

def encontrar_potencia(numero_encontrado, largo):
    
    potencia = 1
    mod = 10**largo  
      

    while True:
        primeros_digitos = primeros_n_digitos_log(potencia, largo)
        total_digitos = int(potencia * math.log10(2)) + 1 
        
        if primeros_digitos == numero_encontrado and total_digitos > 2 * largo:
            return potencia
        
        potencia += 1
          


numeros = []
while True:
    numero = sys.stdin.readline().strip()  
    if numero == "":
        break
    numero = int(numero)
    if numero == 0:
        break
    print(encontrar_potencia(numero, contar_digitos(numero)))
