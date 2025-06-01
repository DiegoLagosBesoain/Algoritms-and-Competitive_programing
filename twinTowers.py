import sys
#problema de distancia nde edicion pero ahora preguntando la cadena despues de edicion mas larga
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
    
largo_torre1,largo_torre2=map(int,sys.stdin.readline().strip().split())
while largo_torre1!=0 and largo_torre2!=0:
    torre1=list(map(int,sys.stdin.readline().strip().split()))
    torre2=list(map(int,sys.stdin.readline().strip().split()))
    print(torre_mas_larga_comun(tuple(torre1),tuple(torre2)))
    largo_torre1,largo_torre2=map(int,sys.stdin.readline().strip().split())

