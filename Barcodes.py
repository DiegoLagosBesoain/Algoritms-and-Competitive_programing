import sys


#entendi re poco como arma la tabla pero es funcional

entrada=sys.stdin.readline().strip()
while entrada !="":
    n,k,m=map(int,entrada.split())
    formas_para_tener_n_barras_en_n_grupos=[[0 for j in range(51)] for i in range(51)]
    formas_para_tener_n_barras_en_n_grupos[0][0]=1
    for barras in range(1,n+1):
        for grupos in range(1,k+1):
            for ultimo_grupo in range(1,m+1):#para entendimiento s es el numero de barras del ultimo grupo que agregamos y se mueve entre 1 y m porque m es el amximo que buscamos
                if barras-ultimo_grupo>=0:#s evita que creemos grupos de mas de m barras ya que es simplemente agregar otro grupo al final de tamaño s
                    formas_para_tener_n_barras_en_n_grupos[barras][grupos]+=formas_para_tener_n_barras_en_n_grupos[barras-ultimo_grupo][grupos-1]
    print(formas_para_tener_n_barras_en_n_grupos[n][k])
    entrada=sys.stdin.readline().strip()
    #como el orden si importa agregamso de abajo hacia arriba en el caso contrario se hace de arriba hacia abajo
