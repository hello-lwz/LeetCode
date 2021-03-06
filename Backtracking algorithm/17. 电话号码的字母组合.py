#!/usr/local/bin/python3
# -*- coding:utf-8 -*-
"""
@author: 
@file: 17. 电话号码的字母组合.py
@time: 2020/8/26 09:27
@desc: 
"""
import itertools
from typing import List
"""
给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。
给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。



示例:

输入："23"
输出：["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
说明:
尽管上面的答案是按字典序排列的，但是你可以任意选择答案输出的顺序。
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/letter-combinations-of-a-phone-number
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        result = []
        map = {"1":"", "2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        def help(digits, temp):
            # 满足条件 加入result 然后跳出当前递归
            if not len(digits):
                result.append(temp)
                return
            for dig in map[digits[0]]:
                # 选择
                temp += dig
                # 进入递归
                help(digits[1:], temp)
                # 撤销选择，进入下次循环
                temp = temp[:-1]
        help(digits, "")
        return result

        # if len(digits) == 0:
        #     return []
        # conversion = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        # return [''.join(item) for item in itertools.product(*(conversion[char] for char in digits))]


a = Solution().letterCombinations("23")
print(a)