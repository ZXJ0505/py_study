# 张晓静的绝作
# 时间：2022/3/1 22:50
name = '马丽亚'
print(name)

name = '楚溜冰'
print(name)

#整数可以代表正数、负数、零
n1=90
n2=-76
n3=0
print(n1,type(n1))
print(n2,type(n2))
print(n3,type(n3))

#整数可以表示为二进制，十进制。八进制，十六进制
print('十进制',118)
print('二进制',0b1010000111)    #二进制以0b开头
print('八进制',0o176)           #八进制以0o开头
print('十六进制',0x1EAF)        #十六进制以0x开头

a=3.14159
print(a,type(a))

n1=1.1
n2=2.2
n3=2.1
print(n1+n2)
print(n1+n3)

from decimal import Decimal
print(Decimal('1.1')+Decimal('2.2'))

f1=True
f2=False
print(f1,type(f1))
print(f2,type(f2))

#布尔值可以转成整数计算
print(f1+1) #2 1+1的结果为2，True表示1
print(f2+1) #1 0+1的结果为1，False表示0

str1='人生苦短，我用Python'
str2="人生苦短，我用Python"
str3="""人生苦短，
我用Python"""
str4='''人生苦短，
我用Python'''
print(str1,type(str1))
print(str2,type(str2))
print(str3,type(str3))
print(str4,type(str4))