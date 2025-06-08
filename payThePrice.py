import sys


def coinchange_cantidad_de_monedas(combinaciones,valor,bajo,alto):
    
    
    
    total=0
    for combinacion in range(bajo,alto+1):
        total+=combinaciones[valor][combinacion]
    return total

entrada=sys.stdin.readline().strip()
combinaciones= [[0 for _ in range(1001)] for _ in range(301)]
combinaciones[0][0]=1
monedas=[i for i in range(1,300 +1)]
for moneda in monedas:
    for suma in range(moneda,301):
        for cantidad in range(1,1001):
            combinaciones[suma][cantidad]+=combinaciones[suma-moneda][cantidad-1]

while entrada !="":

    entrada=list(map(int,entrada.split()))
    if len(entrada)==1:
        suma=entrada[0]
        bajo=1
        alto=suma
    if len(entrada)==2:
        suma=entrada[0]
        bajo=1
        alto=entrada[1]
    if len(entrada)==3:
        suma=entrada[0]
        bajo=entrada[1]
        alto=entrada[2]
    print(coinchange_cantidad_de_monedas(combinaciones,suma,bajo,alto))
    entrada=sys.stdin.readline().strip()
#funciona pero es ineficiente para casos muy altos

