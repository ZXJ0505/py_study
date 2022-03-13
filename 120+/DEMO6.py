# 张晓静的绝作
# 时间：2022/3/11 15:17
print(type(open('a.txt', 'r')))
with open('a.txt', 'r') as file:
    print(file.read())

'''
MyContentMgr实现了特殊方法__enter__(),__exit__()称为该类对象蹲守了上下文管理器协议
该类对象的实例对象，称为上下文管理器
MyContentMgr（）
'''


class MyContentMgr(object):
    def __enter__(self):
        print('enter方法被调用执行了')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('exit方法被调用执行了')

    def show1(self):
        print('show方法被调用执行了')

    def show2(self):
            print('show方法被调用执行了')


with MyContentMgr() as file:  # 相当于file=MyContentMgr
    file.show1()
    file.show2()
print(type(MyContentMgr()))
m=MyContentMgr()
m.show1()