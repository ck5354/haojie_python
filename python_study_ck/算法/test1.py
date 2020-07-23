def check(x):
    y = x + 1
    if y == 5:
        return y
    else:
         check(y)

print(check(1))

# def division(n):
#     v = n + 2
#     print(v)
#     if v == 20:
#         return v
#     temp = division(v)
#     return v + temp  # 递归调用，函数内自己调用自己
#
#
# division(10)  #
