# 张晓静的绝作
# 时间：2022/3/9 15:54
#print(10/0)

import traceback
try:
    print('------------')
    print(1/0)
except:
    traceback.print_exc()