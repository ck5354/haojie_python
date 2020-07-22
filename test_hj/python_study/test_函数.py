def hello():
    print("Hello World")
hello()
###########参数变量
def area(width, height):
    return width * height
def print_welcome(name):
    print("Welcome", name)
print_welcome("Runoob")
w = 4
h = 5
print("width =", w, " height =", h, " area =", area(w, h))

###########传不可变对象
def ChangeInt(a):
    a = 10
b = 2
ChangeInt(b)
print(b)  # 结果是 2

##########传可变对象
def changeme(mylist):
    "修改传入的列表"
    mylist.append([1, 2, 3, 4])
    print("函数内取值: ", mylist)
    return
# 调用changeme函数
mylist = [10, 20, 30]
changeme(mylist)
print("函数外取值: ", mylist)

##########关键字参数
def printme(str):
    "打印任何传入的字符串"
    print(str)
    return
printme(str = "你好，加油！")

##########默认参数
def printinfo(name, age=35):
    "打印任何传入的字符串"
    print("名字: ", name)
    print("年龄: ", age)
    return
# 调用printinfo函数
printinfo(age=50, name="runoob")
print("------------------------")
printinfo(name="runoob")
def printinfo(name,age):
    print("名字是：",name)
    print("年龄是：",age)
    return
printinfo(age = 3,name = "python")


#############冒泡排序，从小到大
a =[1,23,44,3,2,5,89,334,12,123]
for i in range(len(a)-1):
    for j in range(len(a)-1):
        if a[j]>a[j+1]:
           a[j],a[j+1] = a[j+1],a[j]
print(a)

############不定长参数
def printinfo_one(arg1,*vartuple):
    print("输出：")
    print(arg1)
    print(vartuple)
printinfo_one(20,30,40)

