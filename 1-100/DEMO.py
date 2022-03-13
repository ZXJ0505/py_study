# 张晓静的绝作
# 时间：2022/3/1 21:03
print(520)
print(98.5)

print("helloworld")

print(3 + 1)
#所指定的盘符在存在，使用file=
fp = open('D:/text.txt', 'a+')#如果文件不存在就创建，存在就在文件内容的后面继续追加
print('hellowprld', file=fp)
fp.close()

print('hello', 'world', 'Python')
