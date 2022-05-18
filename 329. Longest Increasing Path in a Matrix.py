'''
Title     : 329. Longest Increasing Path in a Matrix
Problem   : https://leetcode.com/problems/longest-increasing-path-in-a-matrix/
'''
'''
recursive DFS helper function
Reference: https://leetcode.com/problems/longest-increasing-path-in-a-matrix/discuss/78334/Python-solution-memoization-dp-288ms
'''
class Solution(object):
    def longestIncreasingPath(self, matrix):
        def dfs(i, j):
            if not dp[i][j]:
                val = matrix[i][j]
                dp[i][j] = 1 + max(
                    dfs(i-1, j) if i > 0 and val > matrix[i-1][j] else 0,
                    dfs(i+1, j) if i < r-1 and val > matrix[i+1][j] else 0,
                    dfs(i, j-1) if j > 0 and val > matrix[i][j-1] else 0,
                    dfs(i, j+1) if j < c-1 and val > matrix[i][j+1] else 0)
            return dp[i][j]

        if not matrix: return 0
        r, c = len(matrix), len(matrix[0])
        dp = [[0]*c for _ in range(r)]
        res = 0
        for i in range(r):
            for j in range(c):
                res = max(res, dfs(i,j))
        return res