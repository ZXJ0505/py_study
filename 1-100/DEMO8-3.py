# 张晓静的绝作
# 时间：2022/3/3 22:22
d = {'name': '张三', 'name': '李四'}  # key不允许重复
print(d)

d = {'name': '张三', 'nikename': '张三'}  # value可以重复的
print(d)

lst = [10, 20, 30]
lst.insert(1, 100)
print(lst)

items = ['Fruits', 'Books', 'Others']
prices = [96, 78, 85,100,120]

d = {item.upper(): price for item, price in zip(items, prices)}
print(d)
