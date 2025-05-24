import sys

def se_pueden_asignar_escribas(paginas, escribas,paginas_por_escriba):
    paginas_asignadas = 0
    escribas_asignados = 1
    for i in range(len(paginas)):
        paginas_asignadas += paginas[i]
        if paginas_asignadas > paginas_por_escriba:
            escribas_asignados += 1
            paginas_asignadas = paginas[i]

    return escribas_asignados <= escribas
def encontrar_max_paginas(paginas, escribas):
    izquierda = max(paginas)
    derecha = sum(paginas) + 1

    while izquierda < derecha:
        medio = (izquierda + derecha) // 2
        if se_pueden_asignar_escribas(paginas, escribas, medio):
            derecha = medio
        else:
            izquierda = medio + 1
    print(izquierda)
    return izquierda
def colocar_escribas(paginas, escribas, max_paginas):
    n = len(paginas)
    resultado = []
    total = 0
    cortes_restantes = escribas - 1

    for i in range(n - 1, -1, -1):
        # Forzamos un corte si:
        # - Agregar esta página excede el máximo
        # - O si necesitamos hacer más cortes que los lugares que quedan
        if total + paginas[i] > max_paginas or i < cortes_restantes:
            resultado.append("/")
            total = 0
            cortes_restantes -= 1
        total += paginas[i]
        resultado.append(str(paginas[i]))

    return " ".join(reversed(resultado))
        
C=int(sys.stdin.readline().strip())
respuestas=[]
for _ in range(C):
    m,escribas=map(int, sys.stdin.readline().strip().split())
    paginas=list(map(int, sys.stdin.readline().strip().split()))
    respuestas.append(colocar_escribas(paginas,escribas,encontrar_max_paginas(paginas, escribas)))
    

for respuesta in respuestas:
    print(respuesta)