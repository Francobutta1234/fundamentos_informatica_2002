import re
def mail_valido(mail):
    if re.match("^[(a-z0-9_-.)]+@[(a-z0-9_-.)]+.[(a-z)]{2,15}$", mail.lower()):
        print("Correo Incorrecto")
    else:
        print("Correo Correcto") 

print(mail_valido("anibalgarcia@gmail.com"))