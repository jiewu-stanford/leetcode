'''
Title     : 62. Unique Paths
Problem   : https://leetcode.com/problems/unique-paths/
'''
'''
most natural 2D DP solution, O(m*n) space
Reference: https://leetcode.com/problems/unique-paths/discuss/22975/Python-easy-to-understand-solutions-(math-dp-O(m*n)-and-O(n)-space)
'''
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if not m or not n: return 0
        dp = [[1]*n for _ in range(m)]
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[-1][-1]

''' 1D DP solution, update row by row, O(n) space, ibid. '''
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if not m or not n: return 0
        dp = [1]*n
        for i in range(1, m):
            for j in range(1, n):
                dp[j] += dp[j-1]
        return dp[-1]

''' as a side note this is merely a combinatorial problem C(m+n-2, n-1), ibid. '''
from math import factorial
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if not m or not n: return 0
        return int(factorial(m+n-2)/(factorial(n-1)*factorial(m-1)))