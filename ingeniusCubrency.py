import sys

def ingeniusCubrncy(n_cubos):
    combinaciones=[0 for _ in range(10000 +1)]
    combinaciones[0]=1
    monedas=[i**3 for i in range(1,n_cubos +1)]
    for moneda in monedas:
        for suma in range(moneda,len(combinaciones)):
            combinaciones[suma]+=combinaciones[suma-moneda]
    return combinaciones

numero=sys.stdin.readline().strip()
while numero != "":
    numero=int(numero)
    print(ingeniusCubrncy(21)[numero])
    numero=sys.stdin.readline().strip()