import sys


def total_de_combinacines_para_cada_precio(monedas,max_valor):
    combinaciones=[0 for i in range(max_valor+1)]
    combinaciones[0]=1
    for moneda in monedas:
        for monto in range(moneda,len(combinaciones)):
            combinaciones[monto]+=combinaciones[monto-moneda]
    return combinaciones
numero=sys.stdin.readline().strip()
monedas=[1,5,10,25,50]
combianciones=total_de_combinacines_para_cada_precio(monedas,7489)
while numero!="":
    numero=int(numero)
    print(combianciones[numero]) 
    numero=sys.stdin.readline().strip()

