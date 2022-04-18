def susti(archivo1, archivo2):
    with open(archivo1, "r") as f, open(archivo2, "w") as a:
        for palabra in f.read():
            for letra in palabra:
                a.write(letra.replace(letra, letra + "\n"))

print(susti("bio.txt", "boooca.txt"))