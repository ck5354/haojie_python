x = [1, 3, 2, 4, 5, 6, 5, 4]
y = [9, 7, 2, 4, 5, 8, 5, 4]

def hebing(list_a, list_b):
    for i in list_b:
        list_a.append(i)
    return list_a

def quchong(x):
    k = []
    for i in x:
        if i not in k:
            k.append(i)
    return k

def maopao(list):
    for i in range(0, len(list)):
        for j in range(0, len(list) - 1):
            if list[j] > list[j + 1]:
                list[j], list[j + 1] = list[j + 1], list[j]
    return list

list_hebing = hebing(x, y)
print(list_hebing)
list_quchong = quchong(list_hebing)
print(list_quchong)
list_paixu = maopao(list_quchong)
print(list_paixu)
