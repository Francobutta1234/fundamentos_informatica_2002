import re
#7
def ej7(string):
    return re.findall("[A-Za-z0-9]", string)
print(ej7("holaKJGKHGJH"))