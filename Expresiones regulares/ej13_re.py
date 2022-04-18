import re
def reemplazar(str):
    return re.sub('\W','_', str, 2)

print(reemplazar('hola messi es el mejor del siglo 21'))