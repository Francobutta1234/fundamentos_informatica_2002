def pollo_vignolo(archivo1, archivo2, archivo3):
    with open(archivo1, "r") as f, open(archivo2, "r") as a, open(archivo3, "a") as af:
        for palabra in f.read():
              af.write(palabra)
        for letter in a.read():
              af.write(letter)

print(pollo_vignolo("bio.txt", "riber.txt", "tuteneta.txt"))