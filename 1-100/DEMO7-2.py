# 张晓静的绝作
# 时间：2022/3/3 15:22
for item in range(1,51):
    if item%5==0:
        print(item)



print('-----使用continue-----')
for item in range(1,51):
    if item%5!=0:
        continue
    print(item)