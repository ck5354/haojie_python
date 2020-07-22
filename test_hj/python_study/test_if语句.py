a = 1
while a < 7:
    if(a % 2 == 0):
        print (a,"is even")
    else:
        print (a,"is odd")
    a += 1

var1 = 100
if var1:
    print("1-if 表达式条件为 ture")
    print(var1)
var2 = 0
if var2:
    print ("2-if 表达式条件为 ture")
    print(var2)
print ("Good bye!")

age = int(input("请输入你家狗狗的年龄：2"))
print("")
if age <=0:
    print("你是在逗我吧")
elif age == 1:
    print("相当于14岁的人。")
elif age == 2:
    print("相当于22岁的人。")
elif age >= 2:
    humen = 22+(age-2)*5
    print("对应人类年龄：",humen)
##退出提示
input("点击enter键退出")

number = 7
guess = -1
print("数字财迷游戏")
while guess != number:
    guess = int(input("请输入你猜的数字：7"))
    if guess== number:
        print("恭喜，猜对了")
    elif guess < number:
        print("猜的数字小了、、、、")
    elif guess > number:
        print("猜的数字大了、、、、")


num = int(input("输入一个数字：29"))
if num % 2 == 0:
    if num % 3 == 0:
        print("你输入的数字可以整除2和3")
    else:
        print("你输入的数字可以除以2，但不能除以3")
else:
    if num % 3 == 0:
        print("你输入的数字可以整除3，但不能整除2")
    else:
        print("你输入的数字不能整除2和3")