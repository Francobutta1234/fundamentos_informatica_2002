import re
def numeros(string):
    return re.findall("[0-9]", string)

print(numeros("Naci el 01 de octubre de 2002"))