#!/usr/local/bin/python3
# -*- coding:utf-8 -*-
"""
@author: 
@file: 1414.和为k的最少斐波那契数字数目.py
@time: 2020/4/20 16:32
@desc: 
"""
"""
给你数字 k ，请你返回和为 k 的斐波那契数字的最少数目，其中，每个斐波那契数字都可以被使用多次。
斐波那契数字定义为：
F1 = 1
F2 = 1
Fn = Fn-1 + Fn-2 ， 其中 n > 2 。
数据保证对于给定的 k ，一定能找到可行解。
示例 1：
输入：k = 7
输出：2 
解释：斐波那契数字为：1，1，2，3，5，8，13，……
对于 k = 7 ，我们可以得到 2 + 5 = 7 。
示例 2：

输入：k = 10
输出：2 
解释：对于 k = 10 ，我们可以得到 2 + 8 = 10 。
示例 3：

输入：k = 19
输出：3 
解释：对于 k = 19 ，我们可以得到 1 + 5 + 13 = 19 。

提示：

1 <= k <= 10^9
"""


class Solution(object):
    def findMinFibonacciNumbers(self, k):
        """
        :type k: int
        :rtype: int
        """
        global result
        result = 1
        def FibonacciList(n):
            list_ = [1]
            pre = 1
            cur = 1
            while pre < n:
                pre, cur = cur, cur+pre
                list_.append(pre)
            return list_
        list_ = FibonacciList(k)
        if k in list_:
            return result
        def find_min_num(list_, cur, pre):
            global result
            result += 1
            if cur-pre in list_:
                return
            else:
                list__ = FibonacciList(cur-pre)
                find_min_num(list__, cur-pre, list__[-2])
        find_min_num(list_, k, list_[-2])
        return result


a = Solution().findMinFibonacciNumbers(19)
print(a)



