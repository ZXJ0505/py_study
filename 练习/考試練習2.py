# 张晓静的绝作
# 时间：2022/3/7 22:48
item = []
for i in range(2):
    item.append(input())
res = ""
for tmp in zip(*item):
    tmp_set = set(tmp)
    if len(tmp_set) == 1:
        res += tmp[0]
    else:
        break
print(res)
