#迭代器有两个基本的方法：iter() 和 next()
import sys

list = [1,2,3,4]
it = iter(list)  # 创建迭代器对象
print(next(it))
print(next(it))
print(next(it))#依次输出1,2,3,

#迭代器对象可以使用常规for语句进行遍历：
list1 = [5,6,7,8,9]
it = iter(list1)  # 创建迭代器对象
for x in it:
    print(x,end="")

#也可以使用 next() 函数：
list2 = [9,8,7,6]
it = iter(list2)  # 创建迭代器对象
while True:
    try:
        print(next(it))
    except StopIteration:
        sys.exit()



