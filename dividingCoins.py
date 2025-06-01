import sys
import functools
@functools.lru_cache(None)
def knapsack(coins, peso_maximo,indice,peso_actual):
    if indice==len(coins):
        return peso_actual
    if peso_actual+coins[indice]>peso_maximo:
        return knapsack(coins,peso_maximo,indice+1,peso_actual)
    else:
        return max(knapsack(coins,peso_maximo,indice+1,peso_actual),knapsack(coins,peso_maximo,indice+1,peso_actual+coins[indice]))

T= int(sys.stdin.readline().strip())
for _ in range(T):
    number_of_coins=int(sys.stdin.readline().strip())
    coins=list(map(int, sys.stdin.readline().strip().split()))
    monto=sum(coins)
    maximo=monto//2
    peso_del_menos_beneficiado=knapsack(tuple(coins),maximo,0,0)
    peso_del_mas_beneficiado=monto-peso_del_menos_beneficiado
    print(f"Case {_+1}: {peso_del_mas_beneficiado - peso_del_menos_beneficiado}")
