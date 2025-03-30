import sys
numeros=[]
line = sys.stdin.readline()
def determinar_cantidad_de_sumas(inicio,objetivo):
    
    suma=0
    while inicio<=objetivo:
        
        if suma+inicio<objetivo:
            suma+=inicio
            inicio+=1
        elif (suma+inicio==objetivo):
            return 1
        else:
            return 0
        
    return
        
        
    
    

while line != '\n':
    
    
    numeros.append(int(line))
    line=sys.stdin.readline()
for numero in numeros:
    i=1
    contador=0
    while i <=numero:
        contador+=determinar_cantidad_de_sumas(i,numero)
        i+=1
    print(contador)
