#条件、循环语句#
#条件语句if#
#False、None、0、""、（）、[]、{}这些作为布尔表达式的时候都会为假#
#if语句:在if和冒号之间的表达式为真，则执行；else在第一个语句块为假时执行.检查多个条件使用elif.#

#断言，简单的说就是肯定某条件为真。使用assert关键字检查条件或检查函数参数属性等，在程序出现错误条件时，直接崩溃，有助于排错。#

#while循环，条件为真的时候重复执行一个代码块，当需要为一个集合的每一个元素执行一个代码块的时候就需要for循环了。能使用for循环，就尽量不使用while循环。#
from cmath import sqrt

# name = ""
# while not name.strip():
#     name = input("input your name: ")
# print ("hello, %s" % name)

# for num in range(1,11):
#     print(num)
#循环遍历字典#
# diction = {'name':'bob','age':'23','sex':'men'}
# for d in diction:
#     print(d,diction[d])
#break跳出循环，而continue跳过循环体，不结束循环。#
# for n in range(99,0,-1):
#     i = sqrt(n)
#     if i == int(i):
#         print(i)
#         break
# #while True实现一个自己不会停止的循环，但是在循环内部加入满足条件break可以终止循环。#
while True:
    dd = input("input your name:")
    if not dd:
        break
    print(dd)
#


