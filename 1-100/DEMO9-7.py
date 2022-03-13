# 张晓静的绝作
# 时间：2022/3/5 17:47
def fun(a,b):
    c=a+b      #c就称为局部变量，因为c是在函数体内进行定义的变量，a，b为函数的形参，作用范围也是函数内部，相当于局部变量
    print(c)

#print(c)       因为a，c超出了起作用的范围（超出了作用域）
#print(a)

name='杨老师'
print(name)     #name的作用范围为函数内部和外部都可以使用 --->称为全局变量
def fun2():
    print(name)

fun2()

def fun3():
    global age
    age=20
    print(age)
fun3()
print(age)