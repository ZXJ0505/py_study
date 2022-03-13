# 张晓静的绝作
# 时间：2022/3/3 15:41
for i in range(1,4):
    for j in range(1, 5):
        print('*', end='\t')
    print()

print('-----九九口算表-----')
for i in range(1,10):
    for j in range(1,i+1):
        print(i,'*',j,'=',i*j,end='\t')
    print()


for i in range(5):
    for j in range(1,11):
        if j%2==0:
            #break
            continue
        print(j,end='\t')
    print()


lst=[10,20,30]
print('添加元素之前',lst,id(lst))
lst.append(100)
print('添加元素之后',lst,id(lst))
lst2=['hello','world']
lst.append(lst2)     #append将lst2作为一个元素添加到列表的末尾
print(lst,id(lst))
lst.extend(lst2)     #extend一次性向列表的末尾添加多个元素
print(lst,id(lst))
lst.insert(1,90)     #instert在列表的指定位置添加一个元素
print(lst)

lst3=[True,False,'hello']
lst[1:]=lst3      #切片，在列表的指定位置添加至少一个元素
print(lst)
