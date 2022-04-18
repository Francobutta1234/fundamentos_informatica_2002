import re
#1
def caracter_permitido(string):
    return bool(re.search("[a-zA-Z0-9]", string))

print(caracter_permitido("---"))
print(caracter_permitido("FRAnco"))