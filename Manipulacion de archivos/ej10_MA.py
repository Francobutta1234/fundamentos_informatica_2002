import glob
import os
def funcion1(archivo, ruta):
    os.chdir(ruta)
    lista_txt = glob.glob("*.txt")

    with open(archivo, "a") as s:
        for f in lista_txt:
            file = open(f, "r")
            s.write(file.read())
            file.close()
