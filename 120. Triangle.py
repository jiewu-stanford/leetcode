'''
Title     : 120. Triangle
Problem   : https://leetcode.com/problems/triangle/description/
'''
'''
2D DP top-down solution, O(n^2/2) space
Reference: https://leetcode.com/problems/triangle/discuss/38735/Python-easy-to-understand-solutions-(top-down-bottom-up)
'''
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        if not triangle: return
        dp = [[0 for _ in range(len(line))] for line in triangle]
        dp[0][0] = triangle[0][0]
        for i in range(1, len(triangle)):
            for j in range(len(triangle[i])):
                if j == 0:
                    dp[i][j] = dp[i-1][j] + triangle[i][j]
                elif j == len(triangle[i])-1:
                    dp[i][j] = dp[i-1][j-1] + triangle[i][j]
                else:
                    dp[i][j] = min(dp[i-1][j-1], dp[i-1][j]) + triangle[i][j]
        return min(dp[-1])

''' top-down and in-place calculation, ibid. '''
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        if not triangle: return
        for i in range(1, len(triangle)):
            for j in range(len(triangle[i])):
                if j == 0:
                    triangle[i][j] = triangle[i-1][j] + triangle[i][j]
                elif j == len(triangle[i]) - 1:
                    triangle[i][j] = triangle[i-1][j-1] + triangle[i][j]
                else:
                    triangle[i][j] = min(triangle[i-1][j-1], triangle[i-1][j]) + triangle[i][j]
        return min(triangle[-1])

''' 1D DP bottom-up solution, O(n) space, ibid. '''
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        if not triangle: return
        dp = triangle[-1]
        for i in range(len(triangle)-2, -1, -1):
            for j in range(len(triangle[i])):
                dp[j] = min(dp[j+1], dp[j]) + triangle[i][j]   # dp[j+1] from the row beneath it
        return dp[0]

''' bottom-up and in-place calculation, ibid. '''
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        if not triangle: return
        for i in range(len(triangle)-2, -1, -1):
            for j in range(len(triangle[i])):
                triangle[i][j] = min(triangle[i+1][j+1], triangle[i+1][j]) + triangle[i][j]
        return triangle[0][0]