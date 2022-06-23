def imprimir(archivo, lineas):
    contador = lineas
    with open(archivo, "r") as f:
        listas = f.readlines()
        print(listas[:contador])

print(imprimir("bio.txt", 1))
