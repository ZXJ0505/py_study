# 张晓静的绝作
# 时间：2022/3/13 23:46
def find_answer(question):
    with open('replay.txt','r',encoding='gbk') as file:
        while True:
            line=file.readline()
            if not line:
                break
            #字符串的分割
            keyword=line.split('|')[0]
            reply=line.split('|')[1]
            if keyword in question:
                return reply
    return False


if __name__ == '__main__':
    question=input('Hi，您好，小蜜在此等主人很久了，有什么烦恼快和小蜜说吧')
    while True:
        if question=='bye':
            break
        replay=find_answer(question)   #开始在文件中查找
        if not replay :
            question=input('小蜜不知道你在说什么，您可以问一些关于订单、物流、账户、支付等问题（退出请输入bye)')
        else:
            print(replay)
            question=input('小主，你还可以继续问一些关于订单、物流、账户、支付等问题（退出请输入bye)')
    print('小主再见')