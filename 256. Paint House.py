'''
Title     : 256. Paint House ($$$)
Problem   : https://leetcode.com/problems/paint-house/
          : https://www.lintcode.com/problem/paint-house/
'''
'''
explicit 1D DP solution
Reference: https://blog.csdn.net/danspace1/article/details/87854823
'''
class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        if not costs: return 0
        dp = costs[0][:]
        for i in range(1, len(costs)):
            prev = dp[:]
            for j in range(len(costs[0])):
                dp[j] = costs[i][j] + min(prev[:j] + prev[j+1:])
        return min(dp)

''' implicit DP solution, ibid. '''
class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        red, blue, green = 0, 0, 0   # min cost for the given last color
        for r, b, g in costs:
            red, blue, green = min(blue, green) + r, min(red, green) + b, min(red, blue) + g   # adjacent colors must be distinct
        return min(red, blue, green)