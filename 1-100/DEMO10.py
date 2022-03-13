# 张晓静的绝作
# 时间：2022/3/7 14:33
def fac(n):
    if n==1:
        return 1
    else:
        res=n*fac(n-1)
        return res

print(fac(6))