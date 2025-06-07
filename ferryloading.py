import sys
import functools

@functools.lru_cache(None)
def knapsack_doble(autos,port_space,starboard_space,secuencia,indice):
    if indice==len(autos):
        return secuencia
    if autos[indice]>port_space and autos[indice]>starboard_space:
        return secuencia
    maximo=[]

    if autos[indice]<=port_space:
        seq=knapsack_doble(autos,port_space-autos[indice],starboard_space,secuencia+("port",),indice+1)
        if len(seq)>len(maximo):
            maximo=seq
    if autos[indice]<=starboard_space:
        seq=knapsack_doble(autos,port_space,starboard_space-autos[indice],secuencia+("starboard",),indice+1)
        if len(seq)>len(maximo):
            maximo=seq
    return maximo
        
t = int(sys.stdin.readline().strip())
for case in range(t):
    sys.stdin.readline().strip()
    large=int(sys.stdin.readline().strip())*100
    auto=int(sys.stdin.readline().strip())
    autos=[]
    while auto!=0:
        autos.append(auto)
        auto=int(sys.stdin.readline().strip())
    print(knapsack_doble(tuple(autos),large,large,(),0))
#falla en casos extremadamente largos