import sys

n=int(sys.stdin.readline().strip())

def programacion_dinamica(bloques):
    alturas_maximas=[0 for i in range(len(bloques))]
    alturas_maximas[0]=bloques[0][2]
    for i in range(len(bloques)):
        alturas_maximas[i]=bloques[i][2]

        for j in range(i):#reviso todos los bloques que pueden ir abajo
            if (bloques[j][0] > bloques[i][0] and bloques[j][1] > bloques[i][1]) or (bloques[j][1] > bloques[i][0] and bloques[j][0] > bloques[i][1]):
                alturas_maximas[i]=max(alturas_maximas[i],alturas_maximas[j]+bloques[i][2])
    #print(f"alturas {alturas_maximas}")
    return max(alturas_maximas)


i=1
while n!=0:
    tipos_de_bloque=[]
    for caso in range(n):
        x,y,z=map(int,sys.stdin.readline().strip().split())
        tipos_de_bloque.append((max(x,y),min(x,y),z))
        tipos_de_bloque.append((max(z,y),min(y,z),x))
        tipos_de_bloque.append((max(x,z),min(x,z),y))
    tipos_de_bloque.sort(reverse=True, key=lambda b: (b[0] * b[1]))
    #print(tipos_de_bloque)
    n=int(sys.stdin.readline().strip())
    print(f"Case {i}: maximum height = {programacion_dinamica(tipos_de_bloque)}")
    i+=1