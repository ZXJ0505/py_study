# 张晓静的绝作
# 时间：2022/3/2 17:10
'''把大象装冰箱一共分几步'''
print('-----程序开始-----')
print('1.把冰箱门打开')
print('2.把大象放冰箱里')
print('3.把冰箱门关上')
print('-----程序结束-----')

#测试对象的布尔值
print('--------------以下对象的布尔值均为False---------------')
print(bool(False))   #False
print(bool(0))       #0
print(bool(0.0))     #0
print(bool(None))    #None
print(bool(''))      #空字符串
print(bool(""))      #空字符串
print(bool([]))      #空列表
print(bool(list()))  #空列表
print(bool(()))      #空元组
print(bool(tuple())) #空元组
print(bool({}))      #空字典
print(bool(dict()))  #空字典
print(bool(set()))   #空集合

print('--------------其他对象的布尔值均为True---------------')
print(bool(18))
print(bool(True))
print(bool('helloworld'))
