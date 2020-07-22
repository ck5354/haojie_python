# map() 函数语法：
# map(function, iterable, ...)   function -- 函数   iterable -- 一个或多个序列
def squ(x):
    return x**2
map(squ,[1, 2, 3, 4, 5])

a = [2,3,4]
a.append(1)
print(a)
