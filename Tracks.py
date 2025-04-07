import sys





def backtraking_de_canciones(conjunto_actual,N,max_suma,suma_actual,maximo_conjunto,indice,T,canciones):
    #si se paso deja de buscar
    if suma_actual>N:
        return
    #si esta en el rango y es mayor sigue buscando
    if suma_actual>max_suma[0]:
        max_suma[0]=suma_actual
        
        maximo_conjunto[0]=conjunto_actual.copy()
    #deja de buscar si paso el ultimo elemento
    if(indice>=T):
        return
    #busca en las ramas que quedan
    for i in range(indice+1,T):
        lista_copia = conjunto_actual.copy()
        lista_copia.append(int(canciones[i]))
        backtraking_de_canciones(lista_copia,N,max_suma,suma_actual+int(canciones[i]),maximo_conjunto,i,T,canciones)

    




entrada=sys.stdin.readline().strip()
while entrada!="":
    entrada=entrada.split()
    N=int(entrada[0])
    Tracks=int(entrada[1])
    canciones=entrada[2:]
    
    max_suma=[0]
    maximo_conjunto=[[]]
    for i , cancion in enumerate(canciones):
        backtraking_de_canciones([int(cancion)],N,max_suma,int(cancion),maximo_conjunto,i,Tracks,canciones)
    
    
    print(f"{" ".join(str(x) for x in maximo_conjunto[0])} sum:{max_suma[0]}")
    entrada=sys.stdin.readline().strip()

