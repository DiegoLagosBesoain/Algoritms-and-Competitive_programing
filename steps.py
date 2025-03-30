import sys

def distancia_disminuyendo(largo_anterior):
    siguiente_paso=largo_anterior+1
    total=0
    while siguiente_paso>0:
        total+=siguiente_paso
        siguiente_paso-=1
    return total



numeros=[]
n=int(sys.stdin.readline())
for i in range(n):
    line = sys.stdin.readline()
    line=line.split(" ")
    K=int(line[0])
    L=int(line[1])
    numeros.append((K,L))

for K,L in numeros:
    largo_anterior=0
    restante = L-K
    pasos=0
    while restante>0:
        
        if distancia_disminuyendo(largo_anterior)>restante:
            if largo_anterior>1:
                largo_anterior-=1
        else:
            largo_anterior+=1
        
        restante-=largo_anterior
        pasos+=1
    print(pasos)
            

