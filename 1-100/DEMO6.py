# 张晓静的绝作
# 时间：2022/3/3 10:06
'''多分支结构，多选一执行
   从键盘录入一个整数 成绩
   90-100 A
   80-89  B
   70-79  C
   60-69  D
   0-59   E
小于0或者大于100，为非法数据（不是成绩的有效范围）'''
score=int(input('请输入一个成绩：'))
#判断
if score>=90 and score<=100:
    print('A级')
elif score>=80 and score<90:
    print('B级')
elif score>=70 and score<80:
    print('C级')
elif score>=60 and score<70:
    print('D级')
elif score>=0 and score<60:
    print('E级')
else:
    print('对不起，成绩有误，不在成绩的有效范围。')