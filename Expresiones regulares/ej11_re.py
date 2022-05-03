import re,glob
def arranca_con_P(lista_str):
    resultado = []
    for string in lista_str:
        if re.findall("(P\w*) (P\w*)", string):
            resultado.append(string)
        else:
            pass
    return resultado
    
lista=["Practica Python", "Practica C++", "Practica Fortran", "Por Papa"]
print(arranca_con_P(lista))