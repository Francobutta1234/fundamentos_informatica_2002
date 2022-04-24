import re
def reemplazar(str):
    return re.sub("\s", ";", str)

print(reemplazar('messi es mejor que    cristiano'))