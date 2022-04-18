import re
def caracter_permitido1(string):
    return bool(re.findall("[^a-zA-Z0-9.]", string))

print(caracter_permitido1("abrazo"))
print(caracter_permitido1("Hola 98"))