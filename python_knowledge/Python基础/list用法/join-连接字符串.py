#语法：  'sep'.join(seq)
#sep：分隔符。可以为空
#seq：要连接的元素序列、字符串、元组、字典

#s = "ajldjlajfdljfddd"，去重并从小到大排序输出"adfjl"
s = "ajldjlajfdljfddd"
s = set(s)    #转换为set，去重
s = list(s)
s.sort()      #列表排序
res = "".join(s)  #“”已这个为分隔符，生成新字符串
print(res)


x = "abc"
y = "def"
z = ["d","e","f"]
m = x.join(y)  #以x为分隔符，生成新的y
n = x.join(z)  #以x为分隔符，生成新的z
print(m)
print(n)
