# 张晓静的绝作
# 时间：2022/3/3 19:05
lst=[10,20,30,40,50,60,30]
lst.remove(30)   #从列表中移除一个元素，如果有重复元素只移动第一个
print(lst)

#pop()根据索引移除元素
lst.pop(1)
print(lst)
lst.pop()     #如果不指定元素（索引）将删除列表中的最后一个元素
print(lst)
print('-----切片操作-删除至少一个元素，将产生一个新的列表对象-----')
new_list=lst[1:3]
print('愿列表',lst)
print('切片后的列表',new_list)


print('-----不产生新的列表对象，而是删除愿列表中的内容-----')
lst[1:3]=[]
print(lst)


print('-----清除列表中的所有元素-----')
lst.clear()
print(lst)


print('-----del语句将列表对象删除-----')
del lst
#print(lst)