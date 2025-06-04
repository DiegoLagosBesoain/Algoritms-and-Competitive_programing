import sys
import functools

def PreciseChangeDriver(peso_maximo, monedas):
    monedas = tuple(monedas)  
    menor_precio = [float("inf")]
    cantidad_monedas_minimas = [0]

    @functools.lru_cache(None)
    def PreciseChange(peso_actual, indice, cantidad_monedas):
        if peso_actual >= peso_maximo:
            if menor_precio[0] > peso_actual:
                menor_precio[0] = peso_actual
                cantidad_monedas_minimas[0] = cantidad_monedas
            elif menor_precio[0] == peso_actual and cantidad_monedas_minimas[0] > cantidad_monedas:
                cantidad_monedas_minimas[0] = cantidad_monedas
            return

        if indice == len(monedas):
            return

       
        PreciseChange(peso_actual + monedas[indice], indice + 1, cantidad_monedas + 1)

       
        PreciseChange(peso_actual, indice + 1, cantidad_monedas)

    PreciseChange(0, 0, 0)
    return menor_precio[0], cantidad_monedas_minimas[0]



t = int(sys.stdin.readline().strip())
respuestas=[]
for _ in range(t):
    producto = int(sys.stdin.readline().strip())
    cantidad_de_monedas = int(sys.stdin.readline().strip())
    monedas = [int(sys.stdin.readline().strip()) for _ in range(cantidad_de_monedas)]
    mejor_precio, cantidad_minima = PreciseChangeDriver(producto, monedas)
    respuestas.append((mejor_precio, cantidad_minima))
for respuesta in respuestas:
    print(respuesta[0], respuesta[1])  