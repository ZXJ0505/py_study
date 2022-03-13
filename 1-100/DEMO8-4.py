# 张晓静的绝作
# 时间：2022/3/3 22:55
'''不可变序列，可变序列'''
'''可变序列：列表，字典'''
lst=[10,20,40,45]
print(id(lst))
lst.append(300)
print(type(lst))
'''不可变序列，字符串，元组'''
s='hello'
print(id(s))
s=s+'world'
print(id(s))
print(s)

print('-----元组的创建方式，第一种，使用（）-----')
t=('Python','world',98)
print(t)
print(type(t))

t2='Python','world',98     #省略了小括号
print(t2)
print(type(t2))

t3=('Python',)     #如果元组中只有一个元素，逗号不能省
print(t3)
print(type(t3))

print('-----第二种创建方式，使用内置函数tuple（）-----')
t1=tuple(('Python','world',98))
print(t1)
print(type(t1))

print('-----第三种，空元组的创建方式-----')
'''空列表的创建方式'''
lst=[]
lst1=list()

d={}
d2=dict()

#空元组
t4=()
t5=tuple()

print('空列表',lst,lst1)
print('空字典',d,d2)
print('空元组',t4,t5)