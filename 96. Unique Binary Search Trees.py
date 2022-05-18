'''
Title     : 96. Unique Binary Search Trees
Problem   : https://leetcode.com/problems/unique-binary-search-trees/description/
'''
'''
1D DP solution
Reference: https://leetcode.com/problems/unique-binary-search-trees/discuss/164915/Python-solution
'''
class Solution(object):
    def numTrees(self, n):
        dp = [0]*(n+1)
        dp[0] = 1
        for i in range(1, n+1):
            for j in range(i):
                dp[i] += dp[j] * dp[i-(j+1)]   # choode node j as the root, leaving left half 0,1,...,j-1 and right half j+1,j+2,...,i-1
        return dp[n]