import sys
line = sys.stdin.readline()
line=line.split(" ")
M=int(line[0])
N=int(line[1])
if(N==1):
    print(M//2)
elif(M==1):
    print(N//2)
else:
    total=0
    if N>M:
        lado_mas_grande=N
        lado_mas_pequeño=M
    else:
        lado_mas_grande=N
        lado_mas_pequeño=M
    if (lado_mas_grande%2==0 and lado_mas_pequeño%2==0):
        total=lado_mas_grande*lado_mas_pequeño/2
    elif(lado_mas_grande%2==0):
        total=(lado_mas_pequeño//2)*lado_mas_grande+lado_mas_grande/2
    elif(lado_mas_pequeño%2==0):
        total=(lado_mas_grande//2)*lado_mas_pequeño+lado_mas_pequeño/2
    else:
        total=lado_mas_grande*(lado_mas_pequeño//2)+lado_mas_grande//2
    
    print(total)
    