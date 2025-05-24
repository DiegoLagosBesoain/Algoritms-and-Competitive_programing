import sys 


def verificar_nodo(nodo,grafo,colores,tamañoR,tamañoA):#este es mio para casos donde tengo una lsita de adyacencias tendira que hacer otro si uso la matriz 
    #en este codigo busco todos los que puedo juntar, si tengo compoenetes separadas no me importa, sigo buscando en las partes que funcionan
    stack=[]
    resultado=True
    if colores[nodo]=="R":
                
        tamañoR[0]+=1
    else:
        tamañoA[0]+=1
    for vecino in grafo[nodo]:
        if colores[vecino]==colores[nodo]:
            resultado= False
        if colores[vecino]==-1:
            stack.append(vecino)
            if colores[nodo]=="R":
                colores[vecino]="A"
                

            else:
                colores[vecino]="R"
                
    for vecino in stack:
        if not verificar_nodo(vecino,grafo,colores,tamañoR,tamañoA):
            resultado= False
    return resultado
def verificar_biparticion(grafo,N,maximo):
    colores=[-1] * N
    valor=True
    
    for nodo in range(N):
        if colores[nodo]==-1:
            tamañoA=[0]
            tamañoR=[0]
            colores[nodo]="R"
            
            
            if verificar_nodo(nodo,grafo,colores,tamañoR,tamañoA):
                
                
                maximo[0]+=max(tamañoR[0],tamañoA[0])
            
            #print(tamañoA[0])
            
            
    #print(colores)
    return True


        
C=int(sys.stdin.readline().strip())
sys.stdin.readline().strip()
respuestas=[]        
for _ in range(C):
    N=int(sys.stdin.readline().strip())
    enemigos_por_persona = []
    max_persona = N
    for persona in range(N):
        
        
        
        enemigos = list(map(int, sys.stdin.readline().strip().split()))
        #print(enemigos)
        if enemigos[0] != 0:
            max_enemigo = max(enemigos[1:])
            max_persona = max(max_persona, max_enemigo)
        enemigos_por_persona.append(enemigos)
    #print(enemigos_por_persona)
    #print(max_persona)
    max_persona = N
    grafo = [[] for _ in range(max_persona)]
    
    for persona_idx, enemigos in enumerate(enemigos_por_persona):
        #print(enemigos)
        if enemigos[0] != 0:
            for enemigo in enemigos[1:]:
                if  enemigo <=N and enemigo - 1 not in grafo[persona_idx] and enemigo <=N:
                    grafo[persona_idx].append(enemigo - 1)
                if enemigo <=N and persona_idx not in grafo[enemigo - 1] :
                    grafo[enemigo - 1].append(persona_idx)
    
    maximo=[0]
    verificar_biparticion(grafo,max_persona,maximo)
    respuestas.append(maximo[0])
        
    sys.stdin.readline().strip()
for i in respuestas:
    print(i)
    
