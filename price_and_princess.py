import sys
import functools
@functools.lru_cache(None)
def torre_mas_larga_comun(torre1,torre2):
    ...
    if not torre1 or not torre2:
        return 0
    if torre1[0]==torre2[0]:
        return 1 +torre_mas_larga_comun(torre1[1:],torre2[1:])
    else:
        return max(torre_mas_larga_comun(torre1[1:],torre2), torre_mas_larga_comun(torre1,torre2[1:]))

t=int(sys.stdin.readline().strip())

for case in range(t):

    largo_posicion ,saltos_principes,saltos_princesa = map(int, sys.stdin.readline().strip().split())
    principe=tuple(map(int, sys.stdin.readline().strip().split()))
    princesa=tuple(map(int, sys.stdin.readline().strip().split()))
    print(torre_mas_larga_comun(principe,princesa))