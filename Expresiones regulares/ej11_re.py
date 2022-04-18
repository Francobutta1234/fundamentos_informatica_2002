import re
def arranca_con_P(lista_str):
    return(re.findall('[^P]', lista_str))
lista=["Practica Python", "Practica C++", "Practica Fortran"]
print(arranca_con_P(lista))