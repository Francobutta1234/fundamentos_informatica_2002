import re
def con_h(string):
    return bool(re.search("h?", string))

def he(string):
    return bool(re.search("he+", string))

def hee(string):
    return bool(re.search("he{2, 4}", string))
 