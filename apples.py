
import sys
from functools import lru_cache

@lru_cache(maxsize=None)
def total_costo(l, r):
    if l>=r:
        return 0
    res=float('inf')
    casos=r - l + 1
    for i in range(l,r+1):
        costo=pesos[i]*casos+total_costo(l,i-1)+total_costo(i+1,r)
        
        res=min(res, costo)
    return res

T = int(sys.stdin.readline().strip())

for _ in range(T):
    n, k = map(int, sys.stdin.readline().strip().split())
    pesos = [i + k + 1 for i in range(n)]
    
    print(f"Case {_+1}: {total_costo(0, n-1)}")
    total_costo.cache_clear()