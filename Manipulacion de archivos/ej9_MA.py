def world_counter(archivo):
    frecuencias = {}
    with open(archivo, "r") as arc:
        word_list = arc.read().split()
        for palabra in word_list:
            if palabra in frecuencias:
                frecuencias[palabra] += 1
            else:
                frecuencias[palabra] = 1
        for word in frecuencias.keys():
            frecuencias[word] = round(frecuencias[word] / len(word_list),3)

print(world_counter("boooca.txt"))