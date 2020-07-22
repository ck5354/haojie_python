dict = {'Google': 'www.google.com', 'Runoob': 'www.runoob.com', 'taobao': 'www.taobao.com'}
print("字典值 : %s" % dict.items()) #items() 函数以列表返回可遍历的(键, 值) 元组数组。
# 遍历字典列表
for key,values in dict.items():
    print(key,values)

d = {'one': 1, 'two': 2, 'three': 3}
print(d.items())
print(type(d.items()))
for key,values in d.items():
    print(key+":"+str(values))
for i in d.items():
    print(i)


