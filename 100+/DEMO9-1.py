# 张晓静的绝作
# 时间：2022/3/10 16:27
a=20
b=100
c=a+b
d=a.__add__(b)

print(c)
print(d)

class Student:
    def __init__(self,name):
        self.name=name
    def __add__(self, other):
        return self.name+other.name

    def __len__(self):
        return len(self.name)

stu1=Student('Jack')
stu2=Student('李四')

s=stu1+stu2   #实现了两个对象的加法运算（因为在Student类中，编写 __add__()特殊的方法
print(s)
s=stu1.__add__(stu2)
print(s)

print('--------')
lst=[11,22,33,44]
print(len(lst))   #len是内容函数len
print(lst.__len__())
print(len(stu1))