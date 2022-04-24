import re
#7
def ej7(string):
    return re.findall("[\d\w\s]", string)
print(ej7("holaKJGKHGJH "))