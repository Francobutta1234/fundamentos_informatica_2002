def tiempo(minutos):
    return str(int(minutos/60)) + " horas " + str(minutos % 60) + " minutos"

print(tiempo(150))