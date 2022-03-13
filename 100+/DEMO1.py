# 张晓静的绝作
# 时间：2022/3/9 16:02
i=1
while i<=10:
    print(i)
    i+=1

print('--------------------------')

class Student:  #Student为类的名称（类名）由一个或多个单次组成，每个单次的首字母大写，其余小写
    pass

#Python中一切皆对象Student是对象吗？内存有开空间吗？
print(id(Student))   #1363693262240
print(type(Student))   #<class 'type'>
print(Student)   #<class '__main__.Student'>
