#两个列表相加（不能使用+），去重、排序
a = [8,9,12,2,3,3,6]
b = [2,29,4,7,17,6,8,0]
def xianglian(list_a,list_b):
    for i in list_b:
        list_a.append(i)
    return list_a
def quzhong(x):
    k = []
    for i in x:
        if i not in k:
            k.append(i)
    return k
def paixu(list_new):
    for i in range(len(list_new)-1):
        for j in range(len(list_new)-1):
            if list_new[j]>list_new[j+1]:
                list_new[j], list_new[j+1] = list_new[j+1], list_new[j]
    return list_new
list1 = xianglian(a,b)
print(list1)
list2 = quzhong(list1)
print(list2)
list3 = paixu(list2)
print(list3)



