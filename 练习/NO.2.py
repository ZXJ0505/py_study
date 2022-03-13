# 张晓静的绝作
# 时间：2022/3/13 10:10
book_name='Java程序设计教程'
publish='西安电子科技大学出版社'
pub_date='2019-02-02'
price=56.8
print('▶→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→◀')
print('▷\t\t《',book_name,'》 \t\t◁')
print('▶\t  出版社:',publish,'\t\t◀')
print('▷\t\t出版时间:',pub_date,'\t\t\t◁')
print('▶\t\t\t定  价:',price,'\t\t\t◀')
print('▷→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→◁')


print('------------------------------------------------------------')


'''1.变量的赋值'''
name1='林黛玉'
name2='薛宝钗'
name3='贾元春'
name4='贾探春'
name5='史湘云'
print('❶\t' +name1)
print('❷\t' +name2)
print('❸\t' +name3)
print('❹\t' +name4)
print('❺\t' +name5)
'''2.列表'''
lst_name=['林黛玉','薛宝钗','贾元春','贾探春','史湘云']
lst_sig=['❶','❷','❸','❹','❺']
for i in range(5):
    print(lst_sig[i],lst_name[i])

'''3.字典'''

d={'❶':'林黛玉','❷':'薛宝钗','❸':'贾元春','❹':'贾探春','❺':'史湘云'}
for key in d:
    print(key,d[key])

'''4.zip'''
for s,name in zip(lst_sig,lst_name):
    print(s,name)

print('---------------------------------------------------------------------------')

#\033[0:前景色+背景色+m—————————[m
print('\033[0:35m\t\t 图书音像勋章\033[m')
print('\033[0:35m----------------------------\033[m')
print('\033[0:32m❀图书音像勋章\t\t\t✪专享活动\033[m')
print('\033[0:33m❤专属优惠\t\t\t☎优惠提醒\033[m')
print('\033[0:35m----------------------------\033[m')

print('---------------------------------------------------------------------------')

height=170
weight=50.5
bmi=weight/(height+weight)
print('您的身高是:'+str(height))
print('您的体重是:'+str(weight))
print('您BMI的指数是:{:0.2f}'.format(bmi))