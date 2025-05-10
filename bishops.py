import sys

def verificar_alfil(matriz, i, j, n):
    for k in range(n):
        # SOLO diagonales
        if i+k < n and j+k < n and matriz[i+k][j+k] == 1:
            return False
        if i-k >= 0 and j-k >= 0 and matriz[i-k][j-k] == 1:
            return False
        if i+k < n and j-k >= 0 and matriz[i+k][j-k] == 1:
            return False
        if i-k >= 0 and j+k < n and matriz[i-k][j+k] == 1:
            return False
    return True

def backtracking(n, m, alfiles_colocados, contador, matriz, i, j):
    if alfiles_colocados == m:
        contador[0] += 1
        return

    if i == n:

        return
        
            
        

    if j == n:
        backtracking(n, m, alfiles_colocados, contador, matriz, i + 1, 0)
        return

    # Intentar colocar un alfil si es válido
    if verificar_alfil(matriz, i, j, n):
        matriz[i][j] = 1
        backtracking(n, m, alfiles_colocados + 1, contador, matriz, i, j + 1)
        matriz[i][j] = 0

    # Omitir esta celda y continuar
    backtracking(n, m, alfiles_colocados, contador, matriz, i, j + 1)

# Entrada principal
for line in sys.stdin:
    n, m = map(int, line.strip().split())
    if n == 0 and m == 0:
        break
    matriz = [[0]*n for _ in range(n)]
    contador = [0]  # usamos lista para pasar por referencia
    backtracking(n, m, 0, contador, matriz, 0, 0)
    print(contador[0])