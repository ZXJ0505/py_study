# 张晓静的绝作
# 时间：2022/3/13 13:53
year=[82,89,88,86,85,00,99]
print('原列表：',year)
for index,value in enumerate(year):
    #pprint(index,value)
    if str(value)!='0':
        year[index]=int('19'+str(value))
    else:
        year[index]=int('200'+str(value))
print('修改之后的列表：',year)
#列表的排序
year.sort()
print('排序之后的列表为：',year)