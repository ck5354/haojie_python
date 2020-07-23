
# 跨文件调用方法
# fangfa("cccc")

"""可变对象在函数里修改了参数，那么在调用这个函数的函数里，原始的参数也被改变了"""

def changeme(alist):
    "修改传入的列表"
    alist.append([1, 2, 3, 4])
    # print("函数内取值: ", alist)
    return


# 调用changeme函数
mylist = [10, 20, 30]
changeme(mylist)
# print("函数外取值: ", mylist)


def chang_int(a):
     a+100

c =100
chang_int(c)
# print("函数外取值: ",c)



"""必需参数"""

"""关键字参数"""
# 可写函数说明
def printinfo(name, age,ds):
    "打印任何传入的字符串"
    print("名字: ", name)
    print("年龄: ", age)
    print("年龄: ", ds)
    return


# 调用printinfo函数
# 如果指定了参数age=50  则其他所有的参数也必须指明参数名称
# printinfo(age=50, name="runoob")
# printinfo(name="ddd", "runoob "eee")

"""默认参数"""

# def printinfo( name, age = 35 ):
#    "打印任何传入的字符串"
#    print ("名字: ", name)
#    print ("年龄: ", age)
#
# printinfo("chenkuo",67)

"""不定长参数"""

def multiple(arg, *args):
    # *args   args为元组
    print("arg: ", arg)
    # 打印不定长参数
    print(type(args))
    for value in args:
        print("other args:", value)


# multiple(1, 3, "2222",True)


def multiple2(**args):
    # **args  args为dict
    print(type(args))
    for key in args:
        print(key + ":" +str(args[key]))


# multiple2(name = '111',age = 4)
