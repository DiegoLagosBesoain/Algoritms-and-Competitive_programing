import sys
combinaciones=[
    "BCG",
    "BGC",
    "CBG",
    "CGB",
    "GBC",
    "GCB"
]

def crear_caja(lista):
    caja={"B":int(lista[0]),"G":int(lista[1]),"C":int(lista[2])}
    return caja
def determinar_numero_de_movimientos(Orden,cajas):
    i=0
    total = 0
    
    for k in Orden:
        
        
        if(i==0):
            
            total = total+cajas["CAJA 2"][k]+cajas["CAJA 3"][k]
            
        if(i==1):
            
            total = total+cajas["CAJA 1"][k]+cajas["CAJA 3"][k]
            
        if(i==2):
            
            
            total = total+cajas["CAJA 1"][k]+cajas["CAJA 2"][k]
        i+=1
        
        
    return total



line = sys.stdin.readline()
while (line!=""):
    
    line=line.split(" ")
    cajas={"CAJA 1":crear_caja(line[0:3]),"CAJA 2":crear_caja(line[3:6]),"CAJA 3":crear_caja(line[6:9])}
    orden_mas_bajo=combinaciones[0]
    movimientos_mas_bajos=determinar_numero_de_movimientos(combinaciones[0],cajas)
    for orden in combinaciones:
        if determinar_numero_de_movimientos(orden,cajas)<movimientos_mas_bajos:
            orden_mas_bajo = orden
            movimientos_mas_bajos = determinar_numero_de_movimientos(orden,cajas)

    
    print(f"{orden_mas_bajo} {movimientos_mas_bajos}")
    line = sys.stdin.readline()




