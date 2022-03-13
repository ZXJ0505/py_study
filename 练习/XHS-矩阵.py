# 张晓静的绝作
# 时间：2022/3/13 20:15
# !/bin/python
# -*- coding: utf8 -*-
import sys
import os
import re


class Solution:
    def isExist(self, matrix, target):
        # Write Code Here
        if not matrix:
            return 0
        m, n = len(matrix), len(matrix[0])
        row, col = m - 1, 0
        while row >= 0 and col < n:
            if matrix[row][col] < target:
                col += 1
            elif matrix[row][col] > target:
                row -= 1
            else:
                return 1
        return 0


matrix_rows, matrix_cols = list(map(int, input().split()))

matrix = []
for matrix_i in range(matrix_rows):
    matrix.append(list(map(int, input().split())))

target = int(input())

s = Solution()
res = s.isExist(matrix, target)

print(res)
