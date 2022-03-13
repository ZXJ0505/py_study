# 张晓静的绝作
# 时间：2022/3/10 14:06
class Person(object):  #Person继承object类
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def info(self):
        print(self.name,self.age)

class Student(Person):
    def __init__(self,name,age,stu_no):
        super().__init__(name,age)   #super()执行父亲的方法
        self.stu_no=stu_no

class Teacher(Person):
    def __init__(self,name,age,teachofyear):
        super().__init__(name,age)
        self.teachofyear=teachofyear


stu=Student('张三',20,'1001')
teachenr=Teacher('李四',34,10)

stu.info()
teachenr.info()





class A(object):
    pass

class B(object):
    pass

class C(A,B):
    pass