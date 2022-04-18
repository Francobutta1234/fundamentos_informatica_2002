import re
def reemplazar(str):
    return re.sub("\S", ";", str)

print(reemplazar('messi es mejor que    cristiano'))