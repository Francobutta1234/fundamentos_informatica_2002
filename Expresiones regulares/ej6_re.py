import re
def find_word(lista, frase):
    return bool(re.search(lista in frase))

listax= ["soy", "un", "maldito", "peda"]
    
print(find_word(listax,"ayer vi jugar a messi"))