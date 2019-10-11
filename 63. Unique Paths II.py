'''
Title     : 63. Unique Paths II
Problem   : https://leetcode.com/problems/unique-paths-ii/
'''
'''
most natural 2D DP solution, O(m*n) space
Reference: https://leetcode.com/problems/unique-paths-ii/discuss/23410/Python-different-solutions-(O(m*n)-O(n)-in-place)
'''
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if not obstacleGrid: return 0
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[1]*n for _ in range(m)]
        
        dp[0][0] = 1 - obstacleGrid[0][0]
        for i in range(1, m):
            dp[i][0] = dp[i-1][0] * (1 - obstacleGrid[i][0])
        for j in range(1, n):
            dp[0][j] = dp[0][j-1] * (1 - obstacleGrid[0][j])
        
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = (dp[i-1][j] + dp[i][j-1]) * (1 - obstacleGrid[i][j])
        return dp[-1][-1]

''' 1D DP solution, O(n) space, ibid. '''
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if not obstacleGrid: return 0
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [1]*n
        
        dp[0] = 1 - obstacleGrid[0][0]
        for j in range(1, n):
            dp[j] = dp[j-1] * (1 - obstacleGrid[0][j])
        
        for i in range(1, m):
            dp[0] *= (1 - obstacleGrid[i][0])
            for j in range(1, n):
                dp[j] = (dp[j] + dp[j-1]) * (1 - obstacleGrid[i][j])
        return dp[-1]
'''
recursive function instead of DP, with memo
Reference: https://leetcode.com/problems/unique-paths-ii/discuss/23434/Python-recursive-solution-with-cache-54ms
'''
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if not obstacleGrid: return 0
        r, c = len(obstacleGrid)-1, len(obstacleGrid[0])-1
        cache = {}
        return self.helper(obstacleGrid, r, c, cache)
    
    def helper(self, obstacleGrid, i, j, cache):
        if (i, j) in cache:
            return cache[(i, j)]
        elif i < 0 or j < 0 or obstacleGrid[i][j] == 1:
            return 0
        elif i == 0 and j == 0:
            return 1
        else:
            cache[(i, j)] = self.helper(obstacleGrid, i-1, j, cache) + self.helper(obstacleGrid, i, j-1, cache)
        return cache[(i, j)]