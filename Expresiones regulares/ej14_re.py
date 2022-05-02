import re
def reemplazar(str):
    return re.sub("[\s\t]", ";", str)

print(reemplazar('messi es mejor que    cristiano'))