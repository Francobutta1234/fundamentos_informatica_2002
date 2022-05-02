import re
def substrings(string):
    return re.search("(@|&)(.*?)(@|&)", string)
    
print(substrings("hola @ como es tu & nombre"))    