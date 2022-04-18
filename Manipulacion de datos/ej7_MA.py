def palabra_larga(archivo):
    caracteres = 0
    palabra = ""
    with open(archivo, "r") as f:
        lista_palabras = f.read().split()
        for word in lista_palabras:
            if len(word) > caracteres:
                caracteres = len(word)
                palabra = word
    return palabra, caracteres
    
print(palabra_larga("bio.txt"))