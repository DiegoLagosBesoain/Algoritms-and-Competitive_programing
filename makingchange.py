import sys
import functools

monedas = [5, 10, 20, 50, 100, 200]

@functools.lru_cache(None)
def coinchange(vuelto, n5, n10, n20, n50, n100, n200):
    
    if vuelto == 0:
        return 0
    if vuelto < 0:
        return float("inf")
    minimo = float("inf")
    if n5 > 0:
        minimo = min(minimo, coinchange(vuelto - 5, n5 - 1, n10, n20, n50, n100, n200))
    if n10 > 0:
        minimo = min(minimo, coinchange(vuelto - 10, n5, n10 - 1, n20, n50, n100, n200))
    if n20 > 0:
        minimo = min(minimo, coinchange(vuelto - 20, n5, n10, n20 - 1, n50, n100, n200))
    if n50 > 0:
        minimo = min(minimo, coinchange(vuelto - 50, n5, n10, n20, n50 - 1, n100, n200))
    if n100 > 0:
        minimo = min(minimo, coinchange(vuelto - 100, n5, n10, n20, n50, n100 - 1, n200))
    if n200 > 0:
        minimo = min(minimo, coinchange(vuelto - 200, n5, n10, n20, n50, n100, n200 - 1))
    if minimo == float("inf"):
        return minimo
    return minimo + 1

def cambio_tendero(monto):
    dp = [float("inf")] * (monto + 1)
    dp[0] = 0
    for x in range(1, monto + 1):
        for c in monedas:
            if x - c >= 0 and dp[x - c] != float("inf"):
                dp[x] = min(dp[x], dp[x - c] + 1)
    return dp

entrada = sys.stdin.readline().strip()
while entrada != "":
    if entrada == "0 0 0 0 0 0":
        break
    n5, n10, n20, n50, n100, n200, precio = entrada.split()
    n5, n10, n20, n50, n100, n200 = map(int, [n5, n10, n20, n50, n100, n200])
    precio = float(precio)
    precio_cent = int(round(precio * 100))

    
    max_pago = precio_cent + 200
    dp_cambio = cambio_tendero(max_pago)

    resultado = float("inf")

    
    for pago in range(precio_cent, max_pago + 1, 5):  
        monedas_pago = coinchange(pago, n5, n10, n20, n50, n100, n200)
        if monedas_pago == float("inf"):
            continue
        vuelto = pago - precio_cent
        monedas_vuelto = dp_cambio[vuelto]
        total = monedas_pago + monedas_vuelto
        if total < resultado:
            resultado = total

    print(f"{resultado:3d}")
    entrada = sys.stdin.readline().strip()

    

