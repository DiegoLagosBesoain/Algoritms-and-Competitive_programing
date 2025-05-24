import sys


entrada= sys.stdin.readline().strip()
def backtraking(k,S,cadena_actual,cadenas_validas,indice):
    print(cadena_actual)
    if indice>k:
        return
    if len(cadena_actual)==6:
        cadenas_validas.append(cadena_actual[:])
        return
    

    for i in range(indice,k):
        cadena_actual.append(S[i])
        backtraking(k,S,cadena_actual,cadenas_validas,i+1)
        cadena_actual.pop()

    



while entrada!="0":
    k=int(entrada[0])
    S=list(map(int,entrada.split()))[1:]
    print(k)
    print(S)
    cadenas_validas=[]
    cadena_actual=[]
    entrada= sys.stdin.readline().strip()
    backtraking(k,S,cadena_actual,cadenas_validas,0)
    print(cadenas_validas)

