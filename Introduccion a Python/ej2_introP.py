def letras(palabra):
    if len(palabra) <= 4:
        return "quinta'nt y sexta'nt"
    else:
        return str.upper(palabra[5]), str.upper(palabra[6])

print(letras("bondiola"))