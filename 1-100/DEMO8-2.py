# 张晓静的绝作
# 时间：2022/3/3 21:51
scores={'张三':100,'李四':98,'王五':45}
#获取所有的key
keys=scores.keys()
print(keys)
print(type(keys))
print(list(keys))     #将所有的key组成的视图转成列表

#获取所有的value
values=scores.values()
print(values)
print(type(values))
print(list(values))

#获取所有的key-value对儿
items=scores.items()
print(items)
print(list(items))     #元组（），转换之后的列表元素是由元组组成

#字典元素的遍历
for item in scores:
    print(item,scores[item],scores.get(item))