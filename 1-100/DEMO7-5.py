# 张晓静的绝作
# 时间：2022/3/3 19:34
lst=[10,20,30,40]
#一次修改一个值
lst[2]=100
print(lst)

lst[1:3]=[300,400,500,600]
print(lst)

print('排序前的列表：',lst,id(lst))
lst.sort()
print('排序后的列表：',lst,id(lst))

#通过指定关键字参数，将列表中的元素进行降序排序
lst.sort(reverse=True)
print(lst)    #reverse=True 表示降序排序，reverse=False就是升序排序
lst.sort(reverse=False)
print(lst)


print('-----使用内置函数sorted（）对列表进行排序，将产生一个新的列表对象-----')
lst=[10, 300, 400, 500, 600, 40]
new_list=sorted(lst)
print(lst)
print(new_list)
#指定关键字参数，实现列表元素的降序排序
desc_list=sorted(lst,reverse=True)
print(desc_list)