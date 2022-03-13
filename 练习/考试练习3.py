# 张晓静的绝作
# 时间：2022/3/8 15:58
a = 'Helloworld'
b = list(a.lower())
c = b[5:] + [' '] + b[:5]
print(''.join(c))
