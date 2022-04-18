import re
def con_h(string):
    return bool(re.search("he", string))

print(con_h("homofobia"))  