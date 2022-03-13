# 张晓静的绝作
# 时间：2022/3/9 15:21
try:                                             #try...except...  异常处理
    a=int(input('请输入第一个整数：'))
    b=int(input('请输入第二个整数：'))
    result=a/b
    print('结果为：',result)
except ZeroDivisionError:
    print('对不起，除数不允许为0')
except ValueError:
    print('只能输入数字串')
print('程序结束')