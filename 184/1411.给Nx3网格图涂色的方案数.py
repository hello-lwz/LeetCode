#!/usr/local/bin/python3
# -*- coding:utf-8 -*-
"""
@author: 
@file: 1411.给Nx3网格图涂色的方案数.py
@time: 2020/4/22 10:31
@desc: 
"""
"""
你有一个 n x 3 的网格图 grid ，你需要用 红，黄，绿 三种颜色之一给每一个格子上色，且确保相邻格子颜色不同（也就是有相同水平边或者垂直边的格子颜色不同）。
给你网格图的行数 n 。
请你返回给 grid 涂色的方案数。由于答案可能会非常大，请你返回答案对 10^9 + 7 取余的结果。


示例 1：

输入：n = 1
输出：12
解释：总共有 12 种可行的方法：
示例 2：

输入：n = 2
输出：54
示例 3：

输入：n = 3
输出：246
示例 4：

输入：n = 7
输出：106494
示例 5：

输入：n = 5000
输出：30228214
 

提示：

n == grid.length
grid[i].length == 3
1 <= n <= 5000
"""



class Solution(object):
    def numOfWays(self, n):
        """
        :type n: int
        :rtype: int
        """
        """
        ABC 类：三个颜色互不相同，一共有 66 种：012, 021, 102, 120, 201, 210；
        ABA 类：左右两侧的颜色相同，也有 66 种：010, 020, 101, 121, 202, 212。
        这样我们就可以把 1212 种 \textit{type}type 浓缩成了 22 种，尝试写出这两类之间的递推式。我们用 f[i][0]f[i][0] 表示 ABC 类，f[i][1]f[i][1] 表示 ABA 类。在计算时，我们可以将任意一种满足要求的涂色方法带入第 i - 1 行，并检查第 i 行的方案数，这是因为同一类的涂色方法都是等价的：
        第 i - 1 行是 ABC 类，第 i 行是 ABC 类：以 012 为例，那么第 i 行只能是120 或 201，方案数为 22；
        第 i - 1 行是 ABC 类，第 i 行是 ABA 类：以 012 为例，那么第 i 行只能是 101 或 121，方案数为 22；
        第 i - 1 行是 ABA 类，第 i 行是 ABC 类：以 010 为例，那么第 i 行只能是 102 或 201，方案数为 2；
        第 i - 1 行是 ABA 类，第 i 行是 ABA 类：以 010 为例，那么第 i 行只能是 101，121 或 202，方案数为 3。
        因此我们就可以写出递推式：
        
        f[i][0]=2∗f[i−1][0]+2∗f[i−1][1]
        f[i][1]=2∗f[i−1][0]+3∗f[i−1][1]
        
        """
        
        mod = 10 ** 9 + 7
        f1 = f2 = 6
        for i in range(2, n+1):
            f1, f2 = (2*f1 + 2*f2) % mod , (2*f1 + 3*f2) % mod
        return (f1+f2)%mod



a = Solution().numOfWays(1)
print(a)