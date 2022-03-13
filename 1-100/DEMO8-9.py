# 张晓静的绝作
# 时间：2022/3/4 15:13
#字符串中的大小写转换的方式
s='hello,python'
a=s.upper()  #upper将所有字母转化成大写，转成大写之后，会产生一个新的字符串对象
print(a,id(a))
print(s,id(s))
b=s.lower()  #lower将所有字母转化成小写，转成小写之后，会产生一个新的字符串对象
print(b.lower(),id(b))
print(b==s)
print(b is s)   #False


s2='hello,Python'
print(s2.swapcase())   #swapcase将所有大写转化成小写，将所有小写转化成大写

print(s2.title())      #title将每个单子的第一个字符转化成大写，把每个单词的剩余字符转换为小写

print(s2.capitalize()) #capitalize把第一个字符转化为大写，把其余字符转化为小写

print(s2.center(20,'*'))#center居中对齐，原字符串12，定义20,20-12=8/2=4，左右各填充4个*

print(s2.ljust(20,'*'))  #ljust左对齐
print(s2.ljust(10,'*'))  #不足时返回原值
print(s2.ljust(20))      #不定义填充符，默认空格

print(s2.rjust(20,'*'))  #rjust右对齐
print(s2.rjust(20))
print(s2.rjust(10))

print(s2.zfill(20))      #zfill右对齐，使用0填充
print(s2.zfill(10))
print('-8910'.zfill(8))  #-0008910

s3='helllo world Python'
lst=s3.split()
print(lst)

print('--------------')
s4='hello|world|Python'
print(s4.split(sep='|'))
print(s4.split(sep='|',maxsplit=1))

print('--------------')
'''rsplit()从右侧开始劈分'''
print(s3.rsplit())
print(s4.rsplit('|'))
print(s4.rsplit(sep='|',maxsplit=1))