def multiple(arg, *args):
    # *args   args为元组
    print("arg: ", arg)
    # 打印不定长参数
    print(type(args))
    for value in args:
        print("other args:", value)

multiple(1, 2, 3)


def chang_int(a):
    a += 100
    print("函数内取值：", a)


c = 99
chang_int(c)
print("函数外取值: ", c)


def multiple2(a,b,**args):
    # **args  args为dict
    print(type(args))
    print(a)
    print(b)
    print(args)
    for key in args:
        print(key + ":" + str(args[key]))

multiple2(1,2,name = "chen", age = 18, nod = 888)


