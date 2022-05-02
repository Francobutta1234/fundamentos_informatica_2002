import re
def reemplazar(string):
      return re.sub("[ _:]", "|", string)

print(reemplazar("messi el mejor_del:mundo"))    