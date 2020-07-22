#sorted(iterable, key=None, reverse=False)
#iterable -- 可迭代对象。
#key -- 主要是用来进行比较的元素，只有一个参数，具体的函数的参数就是取自于可迭代对象中，指定可迭代对象中的一个元素来进行排序。
#reverse -- 排序规则，reverse = True 降序 ， reverse = False 升序（默认）

print(sorted([4,3,2,1]))  #默认升序

a = [3,4,2,5,1]
a.sort()
print(a)  #这个方法会修改原始的 list（返回值为None）。通常这个方法不如sorted()方便-如果你不需要原始的 list，list.sort()方法效率会稍微高一些。
#另一个区别在于list.sort() 方法只为 list 定义。而 sorted() 函数可以接收任何的 iterable。
print(sorted({1: 'D', 2: 'B', 3: 'B', 4: 'E', 5: 'A'}))
#利用key进行倒序排序
example_list = [5, 0, 6, 1, 2, 7, 3, 4]
result_list = sorted(example_list,reverse = True)
print(result_list)

#先按照成绩降序排序，相同成绩的按照名字升序排序：
d1 = [{'name':'alice', 'score':38}, {'name':'bob', 'score':18}, {'name':'darl', 'score':28}, {'name':'christ', 'score':28}]
l = sorted(d1,key = lambda x:(-x["score"],x["name"]))
print(l)

x = [4,6,9,5,2,8,7]
y = x[:]  #通过分片操作将列表x的元素全部拷贝给y，如果简单的把x赋值给y：y = x，y和x还是指向同一个列表，并没有产生新的副本。
y.sort()
print(x)
print(y)
#所有元素都是字符串，对它进行大小写无关的排序
li=['This','is','a','Boy','!']
l = [i.lower() for i in li]
l .sort()
print(l)

