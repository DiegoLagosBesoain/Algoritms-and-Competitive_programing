import sys
def verificar_bipartito(grafo):
    color = [-1] * len(grafo)
    total_guardias = 0
    for i in range(len(grafo)):
        if color[i] == -1:
            color[i] = 0
            stack = [i]
            cant0 = 1
            cant1 = 0
            es_bipartito = True
            while stack:
                nodo = stack.pop()
                for vecino in grafo[nodo]:
                    if color[vecino] == -1:
                        color[vecino] = 1 - color[nodo]
                        if color[vecino] == 0:
                            cant0 += 1
                        else:
                            cant1 += 1
                        stack.append(vecino)
                    elif color[vecino] == color[nodo]:
                        return -1  # conflicto => no es bipartito
            # Componente válida → sumamos el mínimo
            # Caso especial: componente aislada con un solo nodo → debe poner un guardia
            if cant0 + cant1 == 1:
                total_guardias += 1
            else:
                total_guardias += min(cant0, cant1)
    return total_guardias

# Input
C = int(sys.stdin.readline().strip())
resultados = []

for _ in range(C):
    v, e = map(int, sys.stdin.readline().strip().split())
    grafo = [[] for _ in range(v)]
    for _ in range(e):
        a, b = map(int, sys.stdin.readline().strip().split())
        grafo[a].append(b)
        grafo[b].append(a)

    if e == 0:
        resultados.append(str(v))  # Cada nodo aislado necesita un guardia
    else:
        res = verificar_bipartito(grafo)
        resultados.append(str(res) if res != -1 else "-1")

# Output
for res in resultados:
    print(res)