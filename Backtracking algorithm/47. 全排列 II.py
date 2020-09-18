#!/usr/local/bin/python3
# -*- coding:utf-8 -*-
"""
@author: 
@file: 47. 全排列 II.py
@time: 2020/9/18 10:04
@desc: 
"""
from typing import List
"""
给定一个可包含重复数字的序列，返回所有不重复的全排列。

示例:

输入: [1,1,2]
输出:
[
  [1,1,2],
  [1,2,1],
  [2,1,1]
]
"""

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def dfs(nums, temp_list):
            if len(temp_list) == n:
                result.append(temp_list)
            for i in range(len(nums)):
                if i > 0 and nums[i] == nums[i-1]:
                    continue
                dfs(nums[:i] + nums[i+1:], temp_list + [nums[i]])

        result = []
        n = len(nums)
        nums.sort()
        dfs(nums, [])
        return result


a = Solution().permuteUnique([1,1,2])
print(a)