# 张晓静的绝作
# 时间：2022/3/4 11:20
s={10,20,30,405,60}
print(10 in s)
print(100 in s)
print(10 not in s)
print(100 not in s)
s.add(80)
print(s)
s.update([200,400,300])
print(s)
s.update((78,64,56))
print(s)
s.remove(10)
print(s)
'''s.remove(500)
print(s)'''
s.discard(500)
s.discard(64)
print(s)
s.pop()
s.pop()
#s.pop(78)    #pop不能指定参数删除，只能空元素删除第一个
print(s)
s.clear()
print(s)

print('-----集合间的关系-----')
s1={10,20,30,40}
s2={30,40,10,20}
print(s1==s2)
print(s1!=s2)

'''一个集合是否是另一个集合的子集'''
i={10,20,30,40,50,60,}
i1={10,20,30,40}
i2={10,20,90}
print(i1. issubset(i))   #True
print(i2. issubset(i))   #False

'''一个集合是否是另一个集合的超集'''
print(i.issuperset(i1))   #True
print(i.issuperset(i2))   #False

'''两个集合是否含有交集'''
print(i1.isdisjoint(i2))   #False   有交集为False
i3={100,200,300}
print(i1.isdisjoint(i3))   #True