'''
Title     : 221. Maximal Square
Problem   : https://leetcode.com/problems/maximal-square/description/
'''
'''
2D DP, the incremental step uses min() to find the overlap of the three squares to the left (i,j-1), above (i-1,j) and upleft (i-1,j-1) of the current position (i,j)
dp[i][j] = max square length with bottom right corner at (i,j), dp[i][j] = 1 for matrix[i][j] == '1' since cell (i,j) itself is a square
Reference: https://leetcode.com/problems/maximal-square/discuss/164120/Python-or-DP-tm
'''
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix: return 0
        r, c = len(matrix), len(matrix[0])
        dp = [[0 if matrix[i][j] == '0' else 1 for j in range(c)] for i in range(r)]
        for i in range(1, r):
            for j in range(1, c):
                if matrix[i][j] == '1':
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1   # min() to find the overlap of three squares, +1 is extending the overlap square to (i,j)
                else:
                    dp[i][j] = 0
        res = max(max(row) for row in dp)
        return res**2