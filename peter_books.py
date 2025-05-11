import sys

def encontrar_par(libros, indice_p1, precio_buscado):
    low = indice_p1 + 1  # solo buscamos hacia adelante
    high = len(libros) - 1
    while low <= high:
        mid = (low + high) // 2
        if libros[mid] == precio_buscado:
            return libros[mid]
        elif libros[mid] < precio_buscado:
            low = mid + 1
        else:
            high = mid - 1
    return -1




def buscar_par_de_libros(libros,precio):
    par_menor_diferencia=None
    for i,libro in enumerate(libros):
        candidato=encontrar_par(libros,i,precio-libro)
        if candidato!=-1:
            if par_menor_diferencia ==None or abs(libro-candidato)<abs(par_menor_diferencia[1]-par_menor_diferencia[0]):
                par_menor_diferencia=(libro,candidato)
    return par_menor_diferencia





booksN=sys.stdin.readline().strip()
while booksN!="":
    booksN=int(booksN)
    libros=list(map(int,sys.stdin.readline().strip().split()))
    libros.sort()
    print(libros)
    dinero=int(sys.stdin.readline().strip())
    print(buscar_par_de_libros(libros,dinero))
    booksN=sys.stdin.readline().strip()

    