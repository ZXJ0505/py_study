# 张晓静的绝作
# 时间：2022/3/4 23:08
def fun(*args):     #函数的定义时的 可变的位置参数
    print(args)
    print(args[0])

fun(10)
fun(10,30)
fun(30,405,50)


def fun1(**args):
    print(args)

fun1(a=10)
fun1(a=20,b=30,c=40)


def fun2(a,b,c):
    print('a=',a)
    print('b=',b)
    print('c=',c)

fun2(10,20,30)
lst=[11,22,33]
fun2(*lst)

fun2(a=100,c=300,b=200)
dic={'a':111,'b':222,'c':333}
fun2(**dic)

def fun3(a,b=10):
    print('a=',a)
    print('b=',b)

def fun4(*arge):
    print(arge)
def fun5(**arge2):
    print(arge2)

fun4(10,20,30,40)
fun5(a=11,b=22,c=33,d=44,e=55)

def fun6(a,b,c,d):
    print('a=',a)
    print('b=',b)
    print('c=',c)
    print('d=',d)

fun6(10,20,30,40)
fun6(a=10,c=30,b=20,d=40)
fun6(10,20,d=40,c=30)

def fun7(a,b,*,c,d,**args):
    pass

def fun8(*args,**args2):
    pass

def fun7(a,b=10,*args,**args2):
    pass
