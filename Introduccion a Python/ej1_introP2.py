def primera_letra(palabra):
    if palabra[0] == str.upper(palabra[0]):
        return "Mayuscula"
    else:
        return "Minuscula"  

print(primera_letra("ola"))