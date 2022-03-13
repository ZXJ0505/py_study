# 张晓静的绝作
# 时间：2022/3/11 15:02
file=open('a.txt','r')
#print(file.read(2))
#print(file.readline())   #读取一行内容
print(file.readlines())

file=open('c.txt','a')
#file.write('hello')
lst=['java','go','python']
file.writelines(lst)
file.close()