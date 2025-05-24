def se_puede_llenar(vasijas, contenedores_totales, capacidad_maxima):
    contenedores_usados = 1
    llenado_actual = 0

    for leche in vasijas:
        if leche > capacidad_maxima:
            return False
        if llenado_actual + leche > capacidad_maxima:
            contenedores_usados += 1
            llenado_actual = 0
        llenado_actual += leche

    return contenedores_usados <= contenedores_totales

import sys
def capacidad_minima(high, low, vessels, cantidad_de_vasijas):
    if low >= high:
        return low
    mid = (low + high) // 2
    if se_puede_llenar(vessels, cantidad_de_vasijas, mid):
        return capacidad_minima(mid, low, vessels, cantidad_de_vasijas)
    else:
        return capacidad_minima(high, mid + 1, vessels, cantidad_de_vasijas)

input_lines=sys.stdin.readline()

while input_lines!="":

    n,m = map(int, input_lines.strip().split())
    
    vessels = list(map(int, sys.stdin.readline().strip().split()))
    print(capacidad_minima(sum(vessels),max(vessels), vessels, m))
    input_lines = input_lines=sys.stdin.readline()