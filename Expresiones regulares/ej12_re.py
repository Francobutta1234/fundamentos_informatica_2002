import re
sustituir=[" ", "_", ":"] 
def reemplazar(string):
    return re.sun(sustituir,"|", string)

print(reemplazar('messi es el mejor'))