def nombrar(nombre, apellido1, apellido2):
    return str.upper(nombre[0]), str.upper(apellido1[0]), str.upper(apellido2[0])

print(nombrar("franco", "martinez", "sandia"))