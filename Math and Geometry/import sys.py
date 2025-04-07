import sys

def es_primo(num):
    for n in range(2, num):
        if num % n == 0:
            
            return False
    
    return True
def determinar_el_minimo_factor_primo(numero):
    i=2
    while True:
        if numero%i==0 and es_primo(i):
            break
        i+=1
    return i


K=-1
L=-1
numeros=[]
while (L!=0 and K!=0):
    line = sys.stdin.readline()
    line=line.split(" ")
    K=int(line[0])
    L=int(line[1])
    if((L!=0 and K!=0)):
        numeros.append((K,L))

for K,L in numeros:
    if determinar_el_minimo_factor_primo(K) < L:
        print(f"BAD {determinar_el_minimo_factor_primo(K)}")
    else:print("GOOD")    


    