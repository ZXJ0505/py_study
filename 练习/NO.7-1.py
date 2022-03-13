# 张晓静的绝作
# 时间：2022/3/13 16:52
dict_ticket={'G1569':['北京南—天津南','18:05','18:39','00:34'],
             'G1567':['北京南—天津南','18:15','18:49','00:34'],
             'G8917':['北京南—天津西','18:20','19:19','00:59'],
             'G203 ':['北京南—天津南','18:35','19:09','00:34']}
print('车次\t   出发站—到达站 出发时间 到达时间 历时时长')
for item in dict_ticket:
    print(item,end='  ')
    for i in dict_ticket[item]:
        print(i,end='  ')
    print()   #换行
#输入要购买的车次
train_no=input('请输入要购买的车次：')
persons=input('请输入乘车人，如果是多人请使用逗号分隔')
s=f'您已购买了{train_no}'
s_info=dict_ticket[train_no]   #获取车次详细信息
s+=s_info[0]+' '+s_info[1]+' 开'
print(f'{s}请{persons}尽快取走纸质车票【铁路客服】')
