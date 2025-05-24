import sys
def encontrar_maxima_diferencia(saltos):
    max_diferencia = 0
    for i in range(len(saltos) - 1):
        diferencia = abs(saltos[i] - saltos[i + 1])
        if diferencia > max_diferencia:
            max_diferencia = diferencia
    return max_diferencia
def fuerza_valida(saltos,fuerza):
    fuerza_actual=fuerza
    for i in range(len(saltos)-1):
        diferencia=abs(saltos[i]-saltos[i+1])
        if diferencia>fuerza:
            return False
        if diferencia==fuerza:
            fuerza_actual-=1
    if fuerza_actual>=0:
        return True
def encontrar_fuerza(saltos):
    max_diferencia = encontrar_maxima_diferencia(saltos)+len(saltos)-1
    izquierda = 1
    derecha = max_diferencia
    while izquierda < derecha:
        medio = (izquierda + derecha) // 2
        if fuerza_valida(saltos, medio):
            derecha = medio
        else:
            izquierda = medio + 1
    return izquierda
C=int(sys.stdin.readline().strip())
for _ in range(C):
    N=int(sys.stdin.readline().strip())
    
    saltos=sys.stdin.readline().strip()
    saltos=[int(x) for x in saltos.split()]
    max_diferencia = encontrar_maxima_diferencia(saltos)
    print(encontrar_fuerza(saltos))
    



