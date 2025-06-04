def mayor_secuencia_de_tortugas(tortugas):
    n = len(tortugas)
    maximo_tortugas = [[1, tortugas[i][0]] for i in range(n)] 
    mejor_altura = 1

    for i in range(n):
        for j in range(i):
            peso_total_si_agrego_i = maximo_tortugas[j][1] + tortugas[i][0]
           
            if peso_total_si_agrego_i <= tortugas[i][1]:  
                if maximo_tortugas[j][0] + 1 >= maximo_tortugas[i][0]:
                    maximo_tortugas[i][0] = maximo_tortugas[j][0] + 1
                    maximo_tortugas[i][1] = peso_total_si_agrego_i
                    mejor_altura = max(mejor_altura, maximo_tortugas[i][0])

    return mejor_altura

import sys
linea = sys.stdin.readline().strip()
tortugas = []
while linea != "":
    peso, resistencia = map(int, linea.split())
    tortugas.append((peso, resistencia))  
    linea = sys.stdin.readline().strip()


tortugas.sort(key=lambda x: x[1])

print(mayor_secuencia_de_tortugas(tortugas))
#no funciona bien 