import sys


dp=[[0 for _ in range(101)] for _ in range(101)]

dp[0][0]=1



for numero in range(101):
    for suma in range(numero,101):
        for cantidad_de_numeros in range(1, 101):
            
            dp[suma][cantidad_de_numeros] += dp[suma - numero][cantidad_de_numeros-1]
print(2*(dp[24][9])-1)

