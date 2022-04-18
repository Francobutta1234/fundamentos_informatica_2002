respuestas = [input("respuesta1: "), input("respuesta2: "), input("respuesta3: ")]
nota = 0
for respuesta in respuestas:
    if respuesta == "Correcta":
        nota += 4
    if respuesta == "Incorrecta":
        nota -= 1
    if respuesta == "":
        nota += 0

print(nota) 
