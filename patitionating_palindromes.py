import sys




t= int(sys.stdin.readline().strip())
def es_palindormo(palabra):
    return palabra == palabra[::-1]
def cantidad_de_subpalindromos(palabra):
    print(palabra)
    if es_palindormo(palabra):
        return 1
    n = len(palabra)
    mejor=float('inf')
    for i in range(1,n):
        mejor=min(cantidad_de_subpalindromos(palabra[:i])+cantidad_de_subpalindromos(palabra[i:]),mejor)
    return mejor

for case in range(t):
    palabra=sys.stdin.readline().strip()
    print(cantidad_de_subpalindromos(palabra))
