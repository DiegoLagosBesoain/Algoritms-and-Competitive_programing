import sys

def encontrar(n1, n2, c1, c2, N):
    min_costo = None
    mejor_i, mejor_j = 0, 0

    for i in range(N // n1 + 1): 
        resto = N - i * n1
        if resto % n2 == 0:  
            j = resto // n2
            costo = i * c1 + j * c2
            if min_costo == None or costo < min_costo:
                if(i!=0 and j!=0):
                    min_costo = costo
                    mejor_i, mejor_j = i, j

    return (mejor_i, mejor_j) 


N = int(sys.stdin.readline())
resultados = []
while N != 0:
    
    c1, n1 = map(int, sys.stdin.readline().split())

    c2, n2 = map(int, sys.stdin.readline().split())
    
    resultados.append(encontrar(n1, n2, c1, c2, N))
    
    N = int(sys.stdin.readline())


for i, j in resultados:
    print(f"{i} {j}" if i != 0 and j != 0 else "failed")