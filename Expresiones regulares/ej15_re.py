import re
def mail_valido(mail):
    return bool(re.search("[\w]+[-_\.]*[\w]+@[a-z]{1,9}\.[a-z]{2,4}", mail))
        

print(mail_valido("anibalgarcia@gmail.com"))