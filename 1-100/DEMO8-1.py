# 张晓静的绝作
# 时间：2022/3/3 21:37
'''获取字典中的元素'''
scores={'张三':100,'李四':98,'王五':45}
'''第一种方式，使用[]'''
print(scores['张三'])
#print(scores['陈六'])   KeyError: '陈六'

'''第二种方式，使用get（）方法'''
print(scores.get('张三'))
print(scores.get('陈六'))   #None
print(scores.get('麻七',99))     #99是在查找'麻七'所对应的value不存在时，提供的一个默认值

print('张三' in scores)
print('张三' not in scores)

del scores['张三']     #删除指定的key-value对儿
#scores.clear()        #清空字典的元素
print(scores)
scores['陈六']=98     #新增元素
print(scores)

scores['陈六']=100     #修改元素
print(scores)