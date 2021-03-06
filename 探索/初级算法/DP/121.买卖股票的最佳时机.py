#!/usr/local/bin/python3
# -*- coding:utf-8 -*-
"""
@author: 
@file: 121.买卖股票的最佳时机.py
@time: 2020/2/25 16:47
@desc: 
"""
"""
给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。
如果你最多只允许完成一笔交易（即买入和卖出一支股票），设计一个算法来计算你所能获取的最大利润。
注意你不能在买入股票前卖出股票。
示例 1:
输入: [7,1,5,3,6,4]
输出: 5
解释: 在第 2 天（股票价格 = 1）的时候买入，在第 5 天（股票价格 = 6）的时候卖出，最大利润 = 6-1 = 5 。
     注意利润不能是 7-1 = 6, 因为卖出价格需要大于买入价格。
示例 2:
输入: [7,6,4,3,1]
输出: 0
解释: 在这种情况下, 没有交易完成, 所以最大利润为 0。

"""

class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # if len(prices) == 1 or len(prices) == 0:
        #     return 0
        # else:
        #     min_price = min(prices[0], prices[1])
        #     maxprofit = prices[1] - prices[0]
        #     for i in range(2, len(prices)):
        #         if prices[i] - min_price > maxprofit:
        #             maxprofit = prices[i] - min_price
        #         if min_price > prices[i]:
        #             min_price = prices[i]
        #     if maxprofit < 0:
        #         return 0
        #     return maxprofit
        # dp
        # min_price = float("+inf")
        # max_profit = 0
        # for i in prices:
        #     max_profit = max(i - min_price, max_profit)
        #     min_price = min(i, min_price)
        # return max_profit
        # dp2
        dp_i_0, dp_i_1 = 0, float("-inf")
        for i in prices:
            # 今天未持有 = max(昨天未持有,昨天持有，今天卖了)
            dp_i_0 = max(dp_i_0, dp_i_1 + i)
            # 今天持有 = max(昨天持有，昨天未持有，今天买了) 这里为何只有-i 只因为只允许一次交易 如果今天买的 那么之前收益肯定为0
            dp_i_1 = max(dp_i_1, -i)
        return dp_i_0


a = Solution().maxProfit([7,1,5,3,6,4])
print(a)

