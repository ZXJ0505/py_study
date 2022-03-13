# 张晓静的绝作
# 时间：2022/3/4 20:36
#（1） % 占位符
name='张三'
age=20
print('我叫%s,今年%d岁。' % (name,age))   #最后一个 % 是固定符号


#（2） {}
print('我叫{0},今年{1}岁'.format(name,age))


#(3) f-string
print(f'我叫{name},今年{age}岁')


print('%10d' % 99)   #10表示的是宽度
print('%.3f' % 3.1415926)   #.3表示是小数点后三位
#同时表示宽度和精度
print('%10.3f' % 3.1415926)   #一共总宽度为10，小数点后3位

print('{0:.3}'.format(3.1415926))   #.3表示的是一共是三位数
print('{:.3f}'.format(3.1415926))   #.3f表示的是小数点后三位
print('{:10.3f}'.format(3.1415926))  #同时设置宽度和精度，一共是10位，3位是小数部分

s='天涯共此时'
#编码
print(s.encode(encoding='GBK'))  #在GBK这种编码格中，一个中文占两个字节
print(s.encode(encoding='UTF-8'))   #在UTF-8这种编辑格式中，一个中文占三个字节

#解码
#byte代表就是一个二进制数据（字节类型的数据）
byte=s.encode(encoding='GBK')  #编码
print(byte.decode(encoding='GBK'))  #解码

byte=s.encode(encoding='UTF-8')
print(byte.decode(encoding='UTF-8'))
