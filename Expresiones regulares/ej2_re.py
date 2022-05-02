import re
def caracter_permitido1(string):
    resultado = True
    for caracter in string:
        if not bool(re.findall("\w", caracter)):
            return False
        else:
            return resultado    


print(caracter_permitido1("..-ola"))
print(caracter_permitido1("Hola 98"))