def ubicacion(lugar):
    if lugar == "america del sur":
        return 10
    elif lugar == "america del norte":
        return 18
    elif lugar == "america central":
        return 15
    elif lugar == "europa":
        return 24
    elif lugar == "asia":
        return 30

def cobro(numero, function):
    if numero > 5:
        return "entrega'nt"
    else:
        return (function*numero)

print(cobro(4, ubicacion("america del sur")))