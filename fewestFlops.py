import sys
from itertools import permutations

def contar_grupos_consecutivos(cadena):
    if not cadena:
        return 0
    grupos = 1
    for i in range(1, len(cadena)):
        if cadena[i] != cadena[i-1]:
            grupos += 1
    return grupos

def generar_reordenaciones_unicas(bloque):
    return set(permutations(bloque))

def fewest_flops(cadena, tam_bloque):
    n = len(cadena)
    num_bloques = n // tam_bloque
    bloques = [cadena[i * tam_bloque:(i + 1) * tam_bloque] for i in range(num_bloques)]

    dp = [{} for _ in range(num_bloques)]

    # Primer bloque
    for perm in generar_reordenaciones_unicas(bloques[0]):
        reord = ''.join(perm)
        grupos = contar_grupos_consecutivos(reord)
        ultima_letra = reord[-1]
        if ultima_letra not in dp[0] or grupos < dp[0][ultima_letra]:
            dp[0][ultima_letra] = grupos

    # Resto de los bloques
    for i in range(1, num_bloques):
        for perm in generar_reordenaciones_unicas(bloques[i]):
            reord_actual = ''.join(perm)
            grupos_actual = contar_grupos_consecutivos(reord_actual)
            letra_inicio = reord_actual[0]
            letra_fin = reord_actual[-1]

            for letra_anterior, grupos_previos in dp[i - 1].items():
                extra = 0 if letra_anterior == letra_inicio else 1
                total = grupos_previos + grupos_actual + extra
                if letra_fin not in dp[i] or total < dp[i][letra_fin]:
                    dp[i][letra_fin] = total

    return min(dp[-1].values())

# Entrada
t = int(sys.stdin.readline().strip())
for _ in range(t):
    k, word = sys.stdin.readline().strip().split()
    k = int(k)
    print(fewest_flops(word, k) - 1)