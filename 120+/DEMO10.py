# 张晓静的绝作
# 时间：2022/3/12 11:04
import os
path=os.getcwd()
lst_files=os.walk(path)
print(lst_files)
for dirpath,dirname,filename in lst_files:
    '''print(dirpath)   #显示文件目录
    print(dirname)   #目录下多少文件夹
    print(filename)   #所在目录下有多少文件
    print('-----------------------------')'''
    for dir in dirname:
        print(os.path.join(dirpath,dir))
    print('-----------------------------')
    for file in filename:
        print(os.path.join(dirpath,file))
    print('-----------------------------')