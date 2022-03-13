# 张晓静的绝作
# 时间：2022/3/10 11:42
class Car:
    def __init__(self,brand):
        self.brand=brand
    def start(self):
        print('汽车已启动...')

car=Car('宝马x5')
car.start()
print(car.brand)

class Student:
    def __init__(self,name,age):
        self.name=name
        self.__age=age  #年龄不希望在类的外部被使用，所以加了两个__
    def show(self):
        print(self.name,self.__age)

stu=Student('张三',20)
stu.show()
#在类的外部使用name与age
print(stu.name)
#print(stu.__age)
#print(dir(stu))
print(stu._Student__age)   #在类的外部可以通过 _Student__age 进行访问
