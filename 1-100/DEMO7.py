# 张晓静的绝作
# 时间：2022/3/3 14:09
for item in('Python'):
    print(item)

for i in range(10):
    print(i)

for _ in range(5):
    print('人生苦短，我用Python')

sum=0
for i in range(1,101):
    if i%2==0:
        sum+=i
print('1到100之间的偶数和为：',sum)

for item in range(100,1000):
    ge=item%10
    shi=item//10%10
    bai=item//100
    #print(bai,shi,ge)
    if ge**3+shi**3+bai**3==item:
        print(item)
