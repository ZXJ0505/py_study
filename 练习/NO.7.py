# 张晓静的绝作
# 时间：2022/3/13 16:34
constellation=['白羊座','金牛座','双子座','巨蟹座','狮子座','处女座']
nature=['积极乐观','固执内向','圆滑世故','多愁善感','蜜汁自信','精明计较']

#将两个列表转成集合
d=dict(zip(constellation,nature))
'''for item in a:
    print(item)'''
print(d)
key=input('请输入您的星座名称：')
flag=True
for item in d:
    if key==item:
        flag=True
        print(key,'的性格特点为：',d.get(key))
        break
    else:
        #print('对不起，您输入的星座有误')
        flag=False
if not flag:
    print('对不起，您输入的星座有误')
