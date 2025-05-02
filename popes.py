import sys

def backtraking(papas,Y,cantidad,indice,primer_papa,max_cantidad):
    
    if indice>=len(papas) or papas[indice]-primer_papa>Y-1:
        return False
    print(Y,cantidad,indice,papas[indice],primer_papa,max_cantidad)
    if papas[indice]-primer_papa<=Y and cantidad>max_cantidad[0]:
        max_cantidad[0]=cantidad
        max_cantidad[1]=papas[indice]
        max_cantidad[2]=primer_papa

    
    if papas[indice]-primer_papa<= Y-1:
        
        backtraking(papas,Y,cantidad+1,indice+1,primer_papa,max_cantidad)
            
    
Y=int(sys.stdin.readline().strip())

P=int(sys.stdin.readline().strip())

papas=[]

for _ in range(P):
    papas.append(int(sys.stdin.readline().strip()))


papas.sort()
print(papas)
max_cantidad=[0,0,0]
for i,papa in enumerate(papas):
    backtraking(papas,Y,1,i+1,papa,max_cantidad)
print(max_cantidad)
    

