import sys
import functools
#me genereo permutaciones
@functools.lru_cache(None)
def coin_cahnge_que_cuenta_la_cantidad_de_formas(coins,valor):
    if valor<=0:
        return 0
    
    cantidad=1
    for c in coins:
        cantidad+=coin_cahnge_que_cuenta_la_cantidad_de_formas(coins,valor-c)
    return cantidad
@functools.lru_cache(None)
#me genera combinaciones
def contar_formas(i, valor,monedas):
    if valor == 0:
        return 1
    if valor < 0 or i == len(monedas):
        return 0
    
    return contar_formas(i, valor - monedas[i],monedas) + contar_formas(i + 1, valor,monedas)

dinero=sys.stdin.readline().strip()
while dinero!="":
    dinero=int(dinero)
    print(contar_formas(0,dinero,(1,5,10,25,50)))
    dinero=sys.stdin.readline().strip()

