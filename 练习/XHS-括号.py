# 张晓静的绝作
# 时间：2022/3/13 18:15
# !/bin/python
# -*- coding: utf8 -*-
import sys
import os
import re


class Solution:
    def isValid(self, str_str):
        # Write Code Here
        d = {'(': ')', '[': ']', '{': '}', '?': '?'}
        s = ['?']
        for c in str_str:
            if c in d:
                s.append(c)
            elif d[s.pop()] != c:
                return 0
        if len(s) ==1:
            return 1
        return 0


try:
    str_str = input()
except:
    str_str = None

s = Solution()
res = s.isValid(str_str)

print(res)
