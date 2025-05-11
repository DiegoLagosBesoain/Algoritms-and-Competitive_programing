import sys


def backtrakint(insectos,Cmax,Cmin,cadena_actual,indice):
    if Cmin<=sum(cadena_actual)<=Cmax:
        return True
    if sum(cadena_actual)>Cmax:
        return False
    else:
        for i in range(indice,len(insectos)):
            cadena_actual.append(insectos[i])
            if(backtrakint(insectos,Cmax,Cmin,cadena_actual,i+1)):
                return True
            cadena_actual.pop()
    return False



T=int(sys.stdin.readline().strip())

for caso in range(T):
    entrada=list(map(int,sys.stdin.readline().strip().split()))
    Cmin,Cmax=entrada[:2]
    insectos=entrada[2:]
    print(Cmin,Cmax)
    print(insectos)
    
    print(backtrakint(insectos,Cmax,Cmin,[],0))

