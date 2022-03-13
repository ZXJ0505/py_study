# 张晓静的绝作
# 时间：2022/3/11 10:47
import sys
import time
import urllib.request
import math

print(sys.getsizeof(24))
print(sys.getsizeof(45))
print(sys.getsizeof(True))
print(sys.getsizeof(False))

print(time.time())
print(time.localtime(time.time()))

print(urllib.request.urlopen('http://www.baidu.com').read())

print(math.pi)