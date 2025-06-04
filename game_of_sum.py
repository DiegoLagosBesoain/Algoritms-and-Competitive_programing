import sys
sys.setrecursionlimit(10000)

def juego_de_la_suma(A):
    n = len(A)
    memo = [[None] * n for _ in range(n)]
    prefix_sum = [0] * (n + 1)

    # Calcular sumas prefixadas para O(1) suma entre i y j
    for i in range(n):
        prefix_sum[i + 1] = prefix_sum[i] + A[i]

    def suma(i, j):
        return prefix_sum[j + 1] - prefix_sum[i]

    def dp(i, j):
        if i > j:
            return 0
        if memo[i][j] is not None:
            return memo[i][j]

        mejor = float('-inf')

        # Tomar desde la izquierda: i hasta k
        for k in range(i, j + 1):
            total = suma(i, k)
            mejor = max(mejor, total - dp(k + 1, j))

        # Tomar desde la derecha: k hasta j
        for k in range(j, i - 1, -1):
            total = suma(k, j)
            mejor = max(mejor, total - dp(i, k - 1))

        memo[i][j] = mejor
        return mejor

    return dp(0, n - 1)

# Lectura de entradas
while True:
    linea = sys.stdin.readline()
    if not linea:
        break
    n = int(linea.strip())
    if n == 0:
        break
    arreglo = list(map(int, sys.stdin.readline().strip().split()))
    print(juego_de_la_suma(arreglo))