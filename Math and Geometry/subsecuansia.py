import sys

def encontrar_divisores(largo):
    i=1
    divisores=[]
    while i<largo:
        if largo%i==0:
            divisores.append(i)
        i+=1
    return divisores
def promedio_de_un_array(arreglo):
    larg=len(arreglo)
    promedio=sum(arreglo)/larg
    return promedio
def permutaciones(lista):
    if len(lista) == 1:
        return [lista]
    
    resultado = []
    
    for i in range(len(lista)):
        
        elem = lista[i]
        
        resto = lista[:i] + lista[i+1:]
        
        for p in permutaciones(resto):
            resultado.append([elem] + p)
    
    return resultado
def determinar_veracidad(arreglo,valor_buscado):
    largo_arrrglo=len(arreglo)
    print(largo_arrrglo)
    
    if(largo_arrrglo==1):
        if(arreglo[0]==valor_buscado):
            return True
        else:
            return False
    if(largo_arrrglo==2):
        print(f"entre {promedio_de_un_array(arreglo)}")
        if promedio_de_un_array(arreglo)==valor_buscado:
            return True
        else:
            return False
    else:
        divisores=encontrar_divisores(largo_arrrglo)
        divisores.reverse()
        indices = [i for i in range(largo_arrrglo)]
        combinaciones=permutaciones(indices)
        print(divisores)
        if(len(divisores)<1):
            return False
        
        for divisor in divisores:
            tamaño_de_los_pasos=int(largo_arrrglo/divisor)
            for combinacion in combinaciones:
                arreglo_nuevo_orden=[arreglo[i] for i in combinacion]
                print(arreglo_nuevo_orden)
                i=0
                nuevo_arreglo=[]
                
                while(i<largo_arrrglo):
                    
                    print(arreglo_nuevo_orden[i:i+tamaño_de_los_pasos])
                    nuevo_arreglo.append(promedio_de_un_array(arreglo_nuevo_orden[i:i+tamaño_de_los_pasos]))
                    i+=tamaño_de_los_pasos
                print(nuevo_arreglo)
                if determinar_veracidad(nuevo_arreglo,valor_buscado):
                    return True
        return False


        

n=int(sys.stdin.readline())
for i in range(n):
    line = sys.stdin.readline()
    line=line.split(" ")
    largo=int(line[0])
    x=int(line[1])
    line = [int(i) for i in sys.stdin.readline().split(" ")]
    if(determinar_veracidad(line,x)):
        print("YES")
    else:
        print("NO")
