# 张晓静的绝作
# 时间：2022/3/4 10:21
t=(10,[20,30],9)
print(t,id(t))
print(type(t))
print(t[0],type(t[0]),id(t[0]))
print(t[1],type(t[1]),id(t[1]))
print(t[2],type(t[2]),id(t[2]))
'''尝试将t[1]修改为100
t[1]=100   元素是不允许修改元素的'''
print('-----由于[20,30]列表，二列表是可变序列，所以可以向列表中添加元素，二列表的内存地址不变-----')
t[1].append(100)
print(t,id(t))

print('-----元组的遍历-----')
s=('Python','world',98)
'''第一种获取元组的方式，使用索引'''
print(s[0])
print(s[1])
print(s[2])
'''第二种方式——遍历元组'''
for item in s:
    print(item)
