import traceback

# l2 = [i for i in range(1,101) if i % 2 == 0]
# print(l2)
from functools import reduce

l1 = ['太白金星', 'fdsaf', 'alex', 'sb', 'ab']

l2 = [i.upper() for i in l1 if len(i) > 3]
print(l2)
#统计在一个队列中的数字，有多少个正数，多少个负数，如[1, 3, 5, 7, 0, -1, -9, -4, -5, 8]
a = [1,3,5,7,0,-1,-9,-4,-5,8]
b = [i for i in a if i > 0]
print("大于0的个数：%s" % len(b))
c = [i for i in a if i < 0]
print("小于0的个数：%s" % len(c))
#####字符串切片######字符串 “aheboeceydej”，如果得到结果“abcd”
a = "aheboeceydej"
print(a[::3])

#字符串切割#
#已知一个字符串为“hello_world_yoyo”, 如何得到一个队列 [“hello”,”world”,”yoyo”]
a = "hello_word_yoyo"
b = a.split("_")
print(b)
#已知一个数字为1，如何输出“0001”
a = 1
print("%04d" % a)
#已知一个队列,如： [1, 3, 5, 7], 如何把第一个数字，放到第三个位置，得到：[3, 5, 1, 7]
a= [1,3,5,7]
a.insert(3,a[0])
print(a[1:])
#已知 a = 9, b = 8,如何交换a和b的值，得到a的值为8,b的值为9
a = 9
b = 8
a,b = b,a
print("a =",a)
print("b =",b)
#打印出100-999所有的”水仙花数”，所谓”水仙花数”是指一个三位数，
# 其各位数字立方和等于该数本身。例如：153是一个”水仙花数”，
# 因为153=1的三次方＋5的三次方＋3的三次方。
sxh = []
for i in range(100, 1000):
    s = 0
    m = list(str(i))
    for j in m:
        s += int(j)**len(m)
    if i == s:
        print(i)
        sxh.append(i)
print("100-999的水仙花数：%s" % sxh)

a = [1, 3, 10, 9, 21, 35, 4, 6]
for i in range(len(a)-1):
    for j in range(len(a)-1):
        if a[j] > a[j+1]:
           a[j],a[j+1] = a[j+1],a[j]
print(a)

#已知一个队列[1, 3, 6, 9, 7, 3, 4, 6]

#•按从小到大排序
#•按从大大小排序
#•去除重复数字
a = [1, 3, 6, 9, 7, 3, 4, 6]
#1.sort排序，正序
a.sort()
print(a)
#2.sort倒叙
a.sort(reverse=True)
print(a)
#3.去重，set()
b = list(set(a))
print(b)

a = 10
b = reduce(lambda x, y: x*y, range(1, a+1))
print(b)

def digui(n):
    if n == 1:
        return 1
    else:
        return n*digui(n-1)
a = 10
print(digui(a))

a = [1,2,3,3,6]
b = [2,4,7,6,8,0]
list_new = []
for i in a:
    list_new.append(i)
for j in b:
    list_new.append(j)
print(list_new)
print(list_new.sort(key = list_new.index))





