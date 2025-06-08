import sys
import math

def calcular_costo_total(total_dimsum,te,N):
    costo_tea = (N + 1) * te
    costo_base = total_dimsum + costo_tea
    costo_servicio = math.ceil(costo_base * 0.1)
    costo_total = costo_base + costo_servicio
    return costo_total

def knapsack(dimsums,N,x,cantidad_de_platos,indice,total_dimsum,T,favor_acumulado):
    if calcular_costo_total(total_dimsum,T,N)>(N+1)*x:
        return float("-inf")
    if indice==len(dimsums):
        return favor_acumulado/(N+1)
    
    maximo=float("-inf")
    maximo=max(maximo, knapsack(dimsums,N,x,cantidad_de_platos,indice+1,total_dimsum,T,favor_acumulado))
    if cantidad_de_platos>0:
        maximo=max(maximo, knapsack(dimsums,N,x,cantidad_de_platos-1,indice+1,total_dimsum+dimsums[indice][0],T,favor_acumulado+dimsums[indice][1]))
    return maximo
        


N,x,T,K=map(int,sys.stdin.readline().strip().split())

while N!=0 and x!=0 and T !=0 and K!=0:
    dimsums=[]
    for plato in range(K):
        dimsum=list(map(int,sys.stdin.readline().strip().split()))
        dimsums.append((dimsum[0],sum(dimsum[1:])))
        dimsums.append((dimsum[0],sum(dimsum[1:])))
    print(dimsums)
    print(f"{round(knapsack(dimsums,N,x,N+1,0,0,T,0),2):.2f}")
    N,x,T,K=map(int,sys.stdin.readline().strip().split())
#deberia estar funcional