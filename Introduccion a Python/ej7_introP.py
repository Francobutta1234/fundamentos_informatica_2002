def ganancia(sueldo):
    comision = 0.1*int(sueldo)*4
    return int(sueldo) + int(comision)

print(ganancia(100))