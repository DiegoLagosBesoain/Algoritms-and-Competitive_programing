import sys
import functools
sys.setrecursionlimit(10000)

@functools.lru_cache(None)
def mitad_monedas_mitad_Knapsack(tiempo_restante, n, m):
    if tiempo_restante < n and tiempo_restante < m:
        return 0, tiempo_restante

    maximo = (0, tiempo_restante)

    if tiempo_restante >= n:
        resultado = mitad_monedas_mitad_Knapsack(tiempo_restante - n, n, m)
        resultado = (resultado[0] + 1, resultado[1])
        if (
            resultado[1] < maximo[1] or
            (resultado[1] == maximo[1] and resultado[0] > maximo[0])
        ):
            maximo = resultado

    if tiempo_restante >= m:
        resultado = mitad_monedas_mitad_Knapsack(tiempo_restante - m, n, m)
        resultado = (resultado[0] + 1, resultado[1])
        if (
            resultado[1] < maximo[1] or
            (resultado[1] == maximo[1] and resultado[0] > maximo[0])
        ):
            maximo = resultado

    return maximo

entrada = sys.stdin.readline().strip()
while entrada != "":
    n, m, t = map(int, entrada.split())
    print(*mitad_monedas_mitad_Knapsack(t, n, m))
    entrada = sys.stdin.readline().strip()
