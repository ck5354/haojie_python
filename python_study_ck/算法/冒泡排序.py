a =[3,8,2,1,9,5,6,4,7]

def maopao(list):
    for i in range(0, len(list)):
        for j in range(0, len(list)-1):
            if list[j] > list[j+1]:
                a = list[j]
                list[j] = list[j+1]
                list[j+1] = a
    return list
print(maopao(a))