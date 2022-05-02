import re
def con_h(string):
    return bool(re.search("he*", string))

def he(string):
    return bool(re.search("he+", string))

def hee(string):
    return bool(re.search("he{2,3}", string))

print(con_h("heelo"))
print(he("hrmosa"))
print(hee("heeermosa"))