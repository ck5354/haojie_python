dic = {"name":"iu","age":18,"city":"首尔","tel":"16788889999"}
p = sorted(dic.items(),key=lambda i:i[0])
#items()获取字典键值对的元组，i[0]表示字典的键，i[1]表示值
print(p)
new_dic = {}
for i in p:
    new_dic[i[0]] = i[1]
print(new_dic)
