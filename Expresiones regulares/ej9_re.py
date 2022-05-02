import re
#9
def guiones(string):
    return re.findall("-(.*?)-", string)
    return index
print(guiones("fff -esto- ff  ggrgr-esto tambien-gg"))