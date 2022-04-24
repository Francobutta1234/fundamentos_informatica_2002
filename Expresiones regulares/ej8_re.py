import re
def numeros(string):
    return re.findall("\d", string)

print(numeros("Naci el 01 de octubre de 2002"))