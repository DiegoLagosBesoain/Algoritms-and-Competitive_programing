import sys


def calcular_cuenta(consumo):
    consumo_restante=consumo
    iteracion=1
    precio=0
    if consumo<=100:
        precio_total=consumo*2
    elif 100<consumo<=10000:
        precio+=2*100
        precio+=(consumo-100)*3
    elif 10000<consumo<=1000000:
        precio+=2*100+9900*3
        precio+=(consumo-10000)*5
    else:
        precio+=2*100+9900*3+990000*5
        precio+= (consumo-1000000)*7
    return precio


def calcular_consumo(cuenta):
    if cuenta <= 200:
        return cuenta // 2
    elif cuenta <= 29900:
        return 100 + (cuenta - 200) // 3
    elif cuenta <= 4979900:
        return 10000 + (cuenta - 29900) // 5
    else:
        return 1000000 + (cuenta - 4979900) // 7
        


def binary_search(A,B):
    consumo_total=calcular_consumo(A)
    top=consumo_total//2
    low=0
    K=(top+low)//2
    consumo_propio=K
    consumo_vecino=consumo_total-K
    cuenta_mia=calcular_cuenta(consumo_propio)
    cuenta_vecino=calcular_cuenta(consumo_vecino)
    diferencia=abs(cuenta_mia-cuenta_vecino)
    while top>low:
        if diferencia==B:
            print(consumo_propio,consumo_vecino)
            return calcular_cuenta(consumo_propio),calcular_cuenta(consumo_vecino)
            
        if diferencia < B:
            top=K-1
            low =low
            K=(top+low)//2
            consumo_propio=K
            consumo_vecino=consumo_total-K
            cuenta_mia=calcular_cuenta(consumo_propio)
            cuenta_vecino=calcular_cuenta(consumo_vecino)
            diferencia=abs(cuenta_mia-cuenta_vecino)
        else:
            
            top=top
            low = K+1
            K=(top+low)//2
            consumo_propio=K
            consumo_vecino=consumo_total-K
            cuenta_mia=calcular_cuenta(consumo_propio)
            cuenta_vecino=calcular_cuenta(consumo_vecino)
            diferencia=abs(cuenta_mia-cuenta_vecino)
    print(consumo_propio,consumo_vecino)
    return calcular_cuenta(consumo_propio),calcular_cuenta(consumo_vecino)
        



    


A , B = map(int,sys.stdin.readline().strip().split())
while A!=0 and B !=0:
    print(binary_search(A,B))
    
    
    A , B = map(int,sys.stdin.readline().strip().split())

