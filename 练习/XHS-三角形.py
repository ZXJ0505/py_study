# 张晓静的绝作
# 时间：2022/3/13 19:32
# !/bin/python
# -*- coding: utf8 -*-
import sys
import os
import re


class Solution:
    def getCode(self, nums):
        n = len(nums)
        if n > 10000 or n < 3:
            return 0
        # Write Code Here
        nums.sort()
        for a in range(n - 2):
            b = a + 1
            for c in range(b + 1, n):
                while b < n and (nums[a] + nums[b]) > nums[c]:
                    return nums[a] + nums[b] + nums[c]
        return 0


nums_cnt = int(input())
nums = list(map(int, input().split()))

s = Solution()
res = s.getCode(nums)

print(res)
