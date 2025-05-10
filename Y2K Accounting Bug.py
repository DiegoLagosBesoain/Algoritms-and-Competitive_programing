import sys
def backtraking(meses_actuales,s,d):#ejemlo de backtraking, no es el mejor pero es el que se me ocurrio, no se si hay otro mejor, pero este funciona
    if len(meses_actuales)==12:
        profit_total=sum(meses_actuales)
        if profit_total>0:
            return True
        else:
            return False
    if len(meses_actuales)>4:
        meses_por_revisar=meses_actuales[-5:]
        profit=sum(meses_por_revisar)
        if profit>=0:
            return False
    
    meses_actuales.append(-d)
    if backtraking(meses_actuales,s,d)>0:
        return True
    meses_actuales.pop()
    meses_actuales.append(s)
    if backtraking(meses_actuales,s,d)>0:
        return True
    meses_actuales.pop()
    return False
    

    
        
entrada=sys.stdin.readline().strip()
while entrada!="":
    s,d=map(int,entrada.split())
    meses_actuales=[]
    if backtraking(meses_actuales,s,d):
        print("YES")
        print(sum(meses_actuales))
    else:
        print("NO")
    entrada=sys.stdin.readline().strip()
