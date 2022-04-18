import re
def unidas(string, palabra1, palabra2):
    return bool(re.search(palabra1 + "_" + palabra2, string))

print(unidas("me llamo_franco", "me", "llamo"))
print(unidas("me_llamo franco", "me", "llamo"))