# 张晓静的绝作
# 时间：2022/3/4 13:39
print('-----集合的数学操作-----')
#(1)交集
s1={10,20,30,40}
s2={20,30,40,50,60}
print(s1.intersection(s2))
print(s1 & s2)      #intersection()与 & 等价，交集操作
#(2)并集操作
print(s1.union(s2))
print(s1 | s2)      #union与 | 等价，并集操作
#(3)差集操作
print(s1.difference(s2))
print(s1-s2)        #difference与 - 等价，差集操作
#(4)对称差集
print(s1.symmetric_difference(s2))
print(s1 ^ s2)      #symmetric_difference与 ^ 等价，对称差集

#列表生成式
lst=[i*i for i in range(10)]
print(lst)

#集合生成式
s={i*i for i in range(10)}
print(s)

s1='abc%'
s2='abc%'
print(s1 is s2)

s='hello,hello'
print(s.index('lo'))   #3
print(s.find('lo'))    #3
print(s.rindex('lo'))  #9
print(s.rfind('lo'))   #9
#print(s.index('k'))   报错
print(s.find('k'))     #-1
#print(s.rindex('k'))  报错
print(s.rfind('k'))    #-1