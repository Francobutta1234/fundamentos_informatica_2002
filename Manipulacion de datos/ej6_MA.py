def eliminar(archivo1, archivo2):
    with open(archivo1, "r") as f, open(archivo2, "w") as a:
        for linea in f.read():
            a.write(linea.strip("\n"))

print(eliminar("bio.txt", "vacio.txt"))