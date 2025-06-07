import sys
import functools
@functools.lru_cache(None)
def detrminando(caso_base,i,j,n):

    if i==n and j==1:
        return caso_base
    if i>=j:
       
        left = 0
        if i < n:
            left = max(detrminando(caso_base,k,1,n) + detrminando(caso_base,k,j,n) for k in range(i+1, n+1))
        right = 0
        if j > 1:
            right = max(detrminando(caso_base,i,k,n) + detrminando(caso_base,n,k,n) for k in range(1, j))
        return left + right
    if i<j:
        return max(detrminando(caso_base,i,k,n)+detrminando(caso_base,k+1,j,n) for k in range(i,j))
    

caso=sys.stdin.readline().strip()

while caso!="":
    n , an1=map(int,caso.split())
    
    print(detrminando(an1,1,n,n))
    caso=sys.stdin.readline().strip()