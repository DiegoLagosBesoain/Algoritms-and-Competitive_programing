import sys

def knapsack(objetos,indice,peso_restante,valor_actual):
    if indice ==len(objetos):
        return valor_actual
    if objetos[indice][1]>peso_restante:
        return knapsack(objetos,indice+1,peso_restante,valor_actual)
    else:
        sin_tomar = knapsack(objetos,indice+1,peso_restante,valor_actual)
        con_tomar = knapsack(objetos,indice+1,peso_restante-objetos[indice][1],valor_actual+objetos[indice][0])
        return max(sin_tomar,con_tomar)


t= int(sys.stdin.readline().strip())
for caso in range(t):
    N=int(sys.stdin.readline().strip())
    objetos=[]
    for objeto in range(N):
        objetos.append(tuple(map(int,sys.stdin.readline().strip().split())))
    P=int(sys.stdin.readline().strip())
    familia=[]
    for p in range(P):
        familia.append(knapsack(objetos,0,int(sys.stdin.readline().strip()),0))
    print(sum(familia))
    