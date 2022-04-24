import re
def substrings(string):
    return re.findall("@(.*?)&", string)

print(substrings("hola @ como es tu & nombre @ el mio es & raquel"))    