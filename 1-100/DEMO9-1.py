# 张晓静的绝作
# 时间：2022/3/4 17:03
s='hello,Python'
print(s.replace('Python','Java'))
s1='hello,Python,Python,Python'
print(s1.replace('Python','Jave',2))

lst=['hello','jave','python']
print('|'.join(lst))
print(''.join(lst))

t=('hello','java','python')
print(''.join(t))

print('*'.join('Python'))


print('----------')
print('apple'>'app')
print('apple'>'banana')


print(ord('a'),ord('b'))
print(chr(97),chr(98))
print(ord('杨'))
print(chr(26472))

p='hello,Python'
p1=p[:5]
p2=p[6:]
p3='!'
newstr=p1+p3+p2

print(p1)
print(p2)
print(newstr)
print(id(p))
print(id(p1))
print(id(p2))
print(id(p3))
print(id(newstr))

print('-----切片[start:end:step]-----')
print(p[1:5:1])
print(p[::2])
print(p[::-1])
print(p[-6::1])