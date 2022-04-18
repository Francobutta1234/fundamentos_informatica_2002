def es_par(numero):
    if numero %2 == 0:
        return "par"
    else:
        return "impar"  

print(es_par(2))  

def tipo_numero(numero):
    if numero > 0:
        return ("positivo y", es_par(numero))
    elif numero == 0:
        return ("cero y", es_par(numero))
    else:
        return ("negativo y", es_par(numero))

print(tipo_numero(-3))