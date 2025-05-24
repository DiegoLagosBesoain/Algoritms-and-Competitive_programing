import sys

def dfs(grafo, nodo_inicial, nodo_final, visitados):
    if nodo_inicial == nodo_final:
        return True
    visitados.add(nodo_inicial)
    for vecino in grafo[nodo_inicial]:
        if vecino not in visitados:
            if dfs(grafo, vecino, nodo_final, visitados):
                return True
    return False

T = int(sys.stdin.readline())
  # Línea en blanco después del número de casos

respuestas = []
for _ in range(T):
    while True:
        linea = sys.stdin.readline()
        if linea.strip() != '':
            break  # Salta líneas vacías hasta encontrar la del número de computadoras

    computadoras = int(linea.strip())
    grafo = [[] for _ in range(computadoras)]

    validos = 0
    no_validos = 0

    while True:
        linea = sys.stdin.readline()
        if linea == '' or linea.strip() == '':
            break  # Fin del caso

        tipo, a, b = linea.strip().split()
        a = int(a)
        b = int(b)

        if tipo == "c":
            grafo[a-1].append(b-1)
            grafo[b-1].append(a-1)
        elif tipo == "q":
            visitados = set()
            if dfs(grafo, a-1, b-1, visitados):
                validos += 1
            else:
                no_validos += 1

    respuestas.append(f"{validos},{no_validos}")

# Imprimir respuestas separadas por línea en blanco
for respuesta in respuestas:
    print(respuesta)
    print()