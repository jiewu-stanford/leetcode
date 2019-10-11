'''
Title     : 265. Paint House II ($$$)
Problem   : https://leetcode.com/problems/paint-house-ii/
          : https://www.lintcode.com/problem/paint-house-ii/
'''
'''
most naturally 2D DP solution
Reference: https://github.com/shiyanhui/Algorithm/blob/master/LeetCode/Python/265%20Paint%20House%20II.py
'''
class Solution:
    def minCostII(self, costs: List[List[int]]) -> int:
        if not costs: return 0
        r, c = len(costs), len(costs[0])
        dp = [[0] * c for _ in range(r + 1)]
        for i, row in enumerate(costs, 1):
            for j, cost in enumerate(row):
                dp[i][j] = min(dp[i-1][:j] + dp[i-1][j+1:] or [0]) + cost
        return min(dp[r][:] or [0])

''' equivalent 1D DP solution, ibid. '''
class Solution:
    def minCostII(self, costs: List[List[int]]) -> int:
        if not costs: return 0
        r, c = len(costs), len(costs[0])
        dp = [0] * c
        for cost in costs:
            dp = [min(dp[:j] + dp[j+1:] or [0]) + cost[j] for j in range(c)]
        return min(dp or [0])

''' O(n*k)-time solution, keep all second min, ibid. '''
class Solution:
    def minCostII(self, costs: List[List[int]]) -> int:
        if not costs: return 0
        min1, min2 = -1, -1   # first min and second min index
        for i, row in enumerate(costs):
            premin1, premin2, min1, min2 = min1, min2, -1, -1   # reset first min, second min when starting a new row
            for j, cost in enumerate(row):
                if j != premin1:
                    row[j] += 0 if premin1 < 0 else costs[i-1][premin1]
                else:
                    row[j] += 0 if premin2 < 0 else costs[i-1][premin2]
                if min1 < 0 or row[j] < row[min1]:
                    min1, min2 = j, min1
                elif min2 < 0 or row[j] < row[min2]:
                    min2 = j
        return costs[-1][min1]