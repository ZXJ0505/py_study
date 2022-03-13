# 张晓静的绝作
# 时间：2022/3/13 21:48
try:
    score = int(input('请输入分数：'))
    if 0 <= score <= 100:
        print('分数为：', score)
    else:
        raise Exception('分数不正确')
except Exception as e:
    print(e)
