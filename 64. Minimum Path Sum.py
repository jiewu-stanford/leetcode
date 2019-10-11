'''
Title     : 64. Minimum Path Sum
Problem   : https://leetcode.com/problems/minimum-path-sum/
'''
'''
step-by-step traversal iterative solution
Reference: https://leetcode.com/problems/minimum-path-sum/discuss/23466/Simple-python-dp-70ms
'''
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        if not grid: return 0
        r, c = len(grid), len(grid[0])
        for i in range(1, r):
            grid[i][0] += grid[i-1][0]
        for j in range(1, c):
            grid[0][j] += grid[0][j-1]
        for i in range(1, r):
            for j in range(1, c):
                grid[i][j] = min(grid[i-1][j], grid[i][j-1]) + grid[i][j]
        return grid[-1][-1]
'''
most natural 2D DP solution, very similar to traversal but use dp to store partial sum instead of change the grid itself
Reference: https://leetcode.com/problems/minimum-path-sum/discuss/23613/Python-solutions-(O(m*n)-O(n)-space)
'''
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        if not grid: return 0
        r, c = len(grid), len(grid[0])
        dp = [[0]*c for _ in range(r)]
        dp[0][0] = grid[0][0]
        for i in range(1, r):
            dp[i][0] = dp[i-1][0] + grid[i][0]
        for j in range(1, c):
            dp[0][j] = dp[0][j-1] + grid[0][j]    
        for i in range(1, r):
            for j in range(1, c):
                dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]
        return dp[-1][-1]

''' 1D DP solution, ibid. '''
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        if not grid: return 0
        r, c = len(grid), len(grid[0])
        dp = [0]*c
        dp[0] = grid[0][0]
        for j in range(1, c):
            dp[j] = dp[j-1] + grid[0][j]    
        for i in range(1, r):
            dp[0] = dp[0] + grid[i][0]
            for j in range(1, c):
                dp[j] = min(dp[j], dp[j-1]) + grid[i][j]
        return dp[-1]