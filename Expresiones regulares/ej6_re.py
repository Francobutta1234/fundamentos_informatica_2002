import re
def estan_enFrase(lista_strings, frase):
    for string in lista_strings:
        resultado =  bool(re.findall(string, frase))
    return resultado

print(estan_enFrase(["hola", "como", "va"], "hola como va"))