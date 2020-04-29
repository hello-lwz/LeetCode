#!/usr/local/bin/python3
# -*- coding:utf-8 -*-
"""
@author: 
@file: 541.反转字符串II.py
@time: 2020/4/17 17:17
@desc: 
"""
"""
给定一个字符串和一个整数 k，你需要对从字符串开头算起的每个 2k 个字符的前k个字符进行反转。如果剩余少于 k 个字符，则将剩余的所有全部反转。如果有小于 2k 但大于或等于 k 个字符，则反转前 k 个字符，并将剩余的字符保持原样。
示例:
输入: s = "abcdefg", k = 2
输出: "bacdfeg"
要求:
该字符串只包含小写的英文字母。
给定字符串的长度和 k 在[1, 10000]范围内。
"""


class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        # s_new = ""
        # for i in range(0, len(s), 2):
        #     s_new += s[i*k:(i+1)*k][::-1] + s[(i+1)*k:(i+2)*k]
        # return s_new

        s_new = ""
        for i in range(0, len(s), 2*k):
            s_new += s[i:i+k][::-1] + s[i+k:i+k*2]
        return s_new


a = Solution().reverseStr("abcde", 5)
print(a)