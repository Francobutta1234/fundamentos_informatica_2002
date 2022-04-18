numeros = [input("n1: "), input("n2: "), input("n3: "), input("n4: ")]
listax = []
for numero in numeros:
    if int(numero) >= 0:
        listax += numero
    else:
        print(listax)