'''
Title     : 375. Guess Number Higher or Lower II
Problem   : https://leetcode.com/problems/guess-number-higher-or-lower-ii/description/
'''
'''
dp[low][high] = the minimum cost to guarantee a win for any pick of number to be guessed in the range of low to high
Reference: https://leetcode.com/problems/guess-number-higher-or-lower-ii/discuss/173704/Python-DP-with-explaination
'''
class Solution:
    def getMoneyAmount(self, n: int) -> int:
        dp = [[0]*(n+1) for _ in range(n+1)]
        for low in range(n-1, 0, -1):
            for high in range(low+1, n+1):
                dp[low][high] = float('inf')
                for i in range(low, high):
                    # min is to minimize cost, max is to account for the worse (not best strategy!) case scenario for guarantee to win
                    dp[low][high] = min(dp[low][high], i + max(dp[low][i-1], dp[i+1][high]))
        return dp[1][n]