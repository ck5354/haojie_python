l = [1,2,3,4,5,6,7,8,9,10]
def fn(x):
    return x%2 == 1
new_1 = filter(fn,l)
#filter() 函数用于过滤序列，过滤掉不符合条件的元素，返回由符合条件元素组成的新列表。
#接收两个参数，第一个为函数，第二个为序列，序列的每个元素作为参数传递给函数进行判断，
# 然后返回 True 或 False，最后将返回 True 的元素放到新列表中。
res = [i for i in new_1]
print(res)

a =  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
res = [i for i in a if i%2==1]
print(res)

