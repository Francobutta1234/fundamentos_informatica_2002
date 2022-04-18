import re
def empezar(numero, string):
    return bool(re.match(str(numero), string))

print(empezar(9, "70654 veces"))
print(empezar(7, "70654 veces"))