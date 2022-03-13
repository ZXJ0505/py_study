# 张晓静的绝作
# 时间：2022/3/11 22:01
import os.path
print(os.path.abspath('DEMO1.py'))   #获取文件的绝对路径
print(os.path.exists('DEMO1.py'),os.path.exists('DEMO1O.py'))   #文件是否存在。True/False
#print(os.path.join('E://Python','DEMO1.py'))   #拼接操作
print(os.path.split('DEMO1.py'))   #分离文件名和拓展名
print(os.path.splitext('DEMO1.py'))   #分离文件名和拓展名
#print(os.path.basename(E://Python//DEMO1.py'))   #从一个目录中提取文件名
print(os.path.dirname('C://Users//Clover//PycharmProjects//pythonProject//120+//DEMO1.py'))   #提取文件路径
#print(os.path.isdir(E://Python//DEMO1.py'))   #判断是否为路径下的文件



'''列出指定目录下的所有py文件'''
import os
path=os.getcwd()
lst=os.listdir(path)
for filname in lst:
    if filname.endswith('.py'):
        print(filname)