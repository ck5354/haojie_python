def ling_test(x,y):
 for i in range (x,y):
    for q in range(i):
        print("",end='')
    print(' '*(y-i)," *"*i)

    if i == y-1:
        for w in range(x, y-1):
            for z in range(w):
                print("", end=' ')
            print(" ", ' *' * ((y-1) - w))

ling_test(1,23)
a = 4
b = 6
assert a,b
