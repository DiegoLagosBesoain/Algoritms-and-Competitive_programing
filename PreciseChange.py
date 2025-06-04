import sys



def PreciseChage(peso_maximo,peso_actual,monedas,indice,menor_precio,cantidad_monedas_minimas,cantidad_monedas):
    if peso_actual >= peso_maximo:
        if menor_precio[0] > peso_actual:
            menor_precio[0]=peso_actual
            cantidad_monedas_minimas[0]=cantidad_monedas
        elif menor_precio[0] == peso_actual and cantidad_monedas_minimas[0] > cantidad_monedas:
            menor_precio[0]=peso_actual
            cantidad_monedas_minimas[0]=cantidad_monedas

        return
    if indice == len(monedas):
        return
    
    PreciseChage(peso_maximo,peso_actual+monedas[indice],monedas,indice+1,menor_precio,cantidad_monedas_minimas,cantidad_monedas+1)
    PreciseChage(peso_maximo,peso_actual,monedas,indice+1,menor_precio,cantidad_monedas_minimas,cantidad_monedas)


t= int(sys.stdin.readline().strip())
for _ in range(t):
    producto=int(sys.stdin.readline().strip())
    cantidad_de_monedas=int(sys.stdin.readline().strip())
    monedas=[]
    menor_precio=[float("inf")]
    cantidad_monedas_minimas=[0]
    for _ in range(cantidad_de_monedas):
        monedas.append(int(sys.stdin.readline().strip()))
    PreciseChage(producto,0,monedas,0,menor_precio,cantidad_monedas_minimas,0)
    print(menor_precio,cantidad_monedas_minimas)
