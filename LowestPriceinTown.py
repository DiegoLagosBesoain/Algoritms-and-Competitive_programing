import sys
import functools


@functools.lru_cache(None)
def unidades_optimas(objetos,cantidad_esperada,costo):
    if cantidad_esperada<=0:
        return costo
    
    return min(unidades_optimas(objetos,cantidad_esperada-objeto[1],costo+objeto[0]) for objeto in objetos )

entrada=sys.stdin.readline().strip()
i=1

while entrada!="":
    precio_unitario, ofertas=map(float,entrada.split())
    objetos=[(precio_unitario,1)]
    for oferta in range(int(ofertas)):
        cantidad , precio =map(float,sys.stdin.readline().strip().split())
        objetos.append((precio,int(cantidad)))
    print(objetos)
    busquedas=list(map(int,sys.stdin.readline().strip().split()))
    print(f"Case {i}:")
    for cantindad in busquedas:
        print(f"Buy {cantindad} for ${unidades_optimas(tuple(objetos),cantindad,0)}")
    entrada=sys.stdin.readline().strip()
    i+=1
#funcional pero ineficiente
