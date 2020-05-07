#!/usr/local/bin/python3
# -*- coding:utf-8 -*-
"""
@author: 
@file: 599. 两个列表的最小索引总和.py
@time: 2020/5/6 15:21
@desc: 
"""
from typing import List

"""
假设Andy和Doris想在晚餐时选择一家餐厅，并且他们都有一个表示最喜爱餐厅的列表，每个餐厅的名字用字符串表示。
你需要帮助他们用最少的索引和找出他们共同喜爱的餐厅。 如果答案不止一个，则输出所有答案并且不考虑顺序。 你可以假设总是存在一个答案。
示例 1:
输入:
["Shogun", "Tapioca Express", "Burger King", "KFC"]
["Piatti", "The Grill at Torrey Pines", "Hungry Hunter Steakhouse", "Shogun"]
输出: ["Shogun"]
解释: 他们唯一共同喜爱的餐厅是“Shogun”。
示例 2:
输入:
["Shogun", "Tapioca Express", "Burger King", "KFC"]
["KFC", "Shogun", "Burger King"]
输出: ["Shogun"]
解释: 他们共同喜爱且具有最小索引和的餐厅是“Shogun”，它有最小的索引和1(0+1)。
提示:
两个列表的长度范围都在 [1, 1000]内。
两个列表中的字符串的长度将在[1，30]的范围内。
下标从0开始，到列表的长度减1。
两个列表都没有重复的元素。
"""


class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:

        d = {x: list1.index(x) + list2.index(x) for x in set(list1) & set(list2)}
        return [x for x in d if d[x] == min(d.values())]
        # like_all = set(list1) & set(list2)
        # result = []
        # min_index = len(list1) + len(list2) - 2
        # if len(like_all) == 1:
        #     return list(like_all)
        # for like_restaurant in like_all:
        #     current_index = list1.index(like_restaurant) + list2.index(like_restaurant)
        #     if current_index < min_index:
        #         result = []
        #         result.append(like_restaurant)
        #         min_index = current_index
        #     elif current_index == min_index:
        #         result.append(like_restaurant)
        # return result


a = Solution().findRestaurant(["Shogun", "Tapioca Express", "Burger King", "KFC"],
["KFC",  "The Grill at Torrey Pines", "Hungry Hunter Steakhouse","Shogun"])
print(a),