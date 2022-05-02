import re
def unidas(string):
    return re.findall("\D\w*_\D\w*", string)
print(unidas("me llamo_franco"))
print(unidas("me_llamo franco"))