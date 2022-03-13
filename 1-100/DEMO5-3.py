# 张晓静的绝作
# 时间：2022/3/2 14:47

print(1 + 1)  # 加法运算
print(1 - 1)  # 减法运算
print(2 * 4)  # 乘法运算
print(1 / 2)  # 除法运算
print(11 / 2)  # 除法运算
print(11 // 2)  # 5 整除运算
print(11 % 2)  # 1 取余运算
print(2 ** 2)  # 表示的是2的2次方
print(2 ** 3)  # 表示的是2的3次方 2*2*2

print(9 // 4)  # 2
print(-9 // -4)  # 2
print(9 // -4)  # -3
print(-9 // 4)  # -3 一正一负的整数公式，向下取整

print(9 % -4)  # -3 公式 余数=被除数-除数*商 9-（-4）*（-3）
print(-9 % 4)  # 3                       -9-4*（-3）

# 赋值运算符，运算顺序从右到左
i = 3 + 4
print(i)
a = b = c = 20  # 链式赋值
print(a, id(a))
print(b, id(b))
print(c, id(c))

print('--------支持参数赋值-------')
a = 20
a += 30  # 相当于a=a+30
print(a)
a -= 10  # 相当于a=a+10
print(a)
a *= 2  # 相当于a=a*2
print(a)
print(type(a))  # int
a /= 3
print(a)
print(type(a))  # float
a //= 2
print(a)
print(type(a))  # float
a %= 3
print(a)

print('----------解包赋值---------')
a, b, c = 20, 30, 40
print(a, b, c)

# a,b=20,30,40  报错，因为左右变量的个数和值得个数不对应
print('--------交换两个变量的值-------')
a, b = 10, 20
print('交换之前：', a, b)
# 交换
a, b = b, a
print('交换之后：', a, b)

#比较运算符，比较运算符的结果为bool类型
a,b=10,20
print('a>b吗？',a>b)     #False
print('a<b吗？',a<b)     #True
print('a<=b吗？',a<=b)   #True
print('a>=b吗？',a>=b)   #False
print('a==b吗？',a==b)   #False
print('a!=b吗？',a!=b)   #True

'''一个 = 称为赋值运算符 ， == 称为比较运算符
一个变量由三部分组成，标识，类型，值
==比较的是值还是标识呢？ 比较的是值
比较对象的标识使用 is
'''


a=10
b=10
print(a==b)     #True 说明，a与b的value，相等
print(a is b)   #True 说明，a与b的id标识，相等
lst1=[11,22,33,44]
lst2=[11,22,33,44]
print(lst1==lst2)        #value ---->True
print(lst1 is lst2)      #id    ---->False
print(a is not b)        #False  a的id与b的id是相等的
print(lst1 is not lst2)  #True lst1的id与lst2的id是不相等的

a,b=1,2
print(a==1 and b==2)
print(a==1 and b<2)
print(a!=1 and b==2)
print(a!=1 and b!=2)
print(a==1 or b==2)

f=True
f2=False
print(not f)
print(not f2)

s='helloworld'
print('w' in s)
print('k' in s)
print('w' not in s)
print('k' not in s)

print(4&8)   #按位与&，同为1时结果为1
print(4|8)   #按位或|，同为0时结果为0

print(4<<1)  #向左移动1位（移动一个位置）相当于乘以2
print(4<<2)  #向左移动2位（移动二个位置）
print(4>>1)  #向右移动1位（移动一个位置）相与于除以2
print(4>>2)  #向右移动2位（移动二个位置）相当于除以4