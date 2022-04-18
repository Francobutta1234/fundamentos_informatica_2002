def sumara(l1,l2):
    l3 = []
    for i in l2:
        l3.append(l1[i - 1] + l2[i - 1])
    return l3

print(sumara([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]))