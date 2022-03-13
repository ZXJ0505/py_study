# 张晓静的绝作
# 时间：2022/3/11 14:37

file = open('a.txt', 'r')   #只读模式
print(file.readlines())   #readlines读取的是一个列表内容
file.close()


file=open('b.txt','w')   #只写模式，如有内容覆盖原信息
file.write('Python')
file.close()


file=open('b.txt','a')   #追加模式
file.write('Python')
file.close()