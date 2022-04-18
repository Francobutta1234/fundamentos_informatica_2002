def guardar(archivo, lineas):
    lista = []
    with open(archivo, "r") as f:
        for i in f:
            lista.append(i)       
    print(lista[-lineas:])

print(guardar("bio.txt", 3))