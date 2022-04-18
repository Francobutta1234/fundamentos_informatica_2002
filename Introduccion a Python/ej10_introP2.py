def letras(palabra):
    dic = {}
    for letra in palabra:
        if letra not in dic:
            dic[letra] = 1
        elif letra in dic:
            dic[letra] += 1
    return dic

print(letras("holala"))   