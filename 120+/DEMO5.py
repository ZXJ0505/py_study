# 张晓静的绝作
# 时间：2022/3/11 15:09
file=open('a.txt','r')
file.seek(2)    #seek把文件指针移动到新的位置
print(file.read())
file.close()


file=open('c.txt','r')
file.seek(2)
print(file.read())
print(file.tell())   #返回文件指针的当前位置
file.close()

file=open('d.txt','a')
file.write('hello')
file.flush()      #先flush再close
file.write('world')
file.close()