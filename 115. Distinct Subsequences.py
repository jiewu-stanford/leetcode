'''
Title     : 115. Distinct Subsequences
Problem   : https://leetcode.com/problems/distinct-subsequences/
'''
'''
2D DP solution, dp[i][j] = number of distinct s[:i] subsequences == t[:j]
Reference: https://leetcode.com/problems/distinct-subsequences/discuss/37322/Python-dp-solutions-(O(m*n)-O(n)-space).
'''
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        l1, l2 = len(s)+1, len(t)+1
        dp = [[0] * l2 for _ in range(l1)]
        for i in range(l1):
            dp[i][0] = 1   # i = 0 means empty t, thus having only empty subsequence equal to t
        
        for i in range(1, l1):
            for j in range(1, l2):
                dp[i][j] = dp[i-1][j] + dp[i-1][j-1]*(s[i-1]==t[j-1])
        return dp[-1][-1]

''' using 1D DP instead of 2D, update dp[i][:] row by row, ibid. '''
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        l1, l2 = len(s)+1, len(t)+1
        dp = [0] * l2
        dp[0] = 1
        
        for i in range(1, l1):
            predp = dp[:]
            for j in range(1, l2):
                dp[j] = predp[j] + predp[j-1]*(s[i-1]==t[j-1])
        return dp[-1]