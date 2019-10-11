'''
Title     : 70. Climbing Stairs
Problem   : https://leetcode.com/problems/climbing-stairs/
'''
'''
essentially Fibonacci number calculation, top-down DP, but TLE
Reference: https://leetcode.com/problems/climbing-stairs/discuss/25313/Python-different-solutions-(bottom-up-top-down)
'''
class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1: return 1
        if n == 2: return 2
        return self.climbStairs(n-1) + self.climbStairs(n-2)

''' bottom-up DP, O(n) space, ibid. '''
class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1: return 1
        dp = [0]*n
        dp[0], dp[1] = 1, 2
        for i in range(2, n):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[-1]

''' bottom-up DP, constant space, ibid. '''
class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1: return 1
        a, b = 1, 2
        for i in range(2, n):
            tmp = b
            b = a + b
            a = tmp
        return b

''' top-down DP with memo using list, ibid. '''
class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1: return 1
        dp = [0]*n
        dp[0], dp[1] = 1, 2
        return self.helper(n-1, dp)
    
    def helper(self, n, dp):
        if dp[n] < 1:
            dp[n] = self.helper(n-1, dp) + self.helper(n-2, dp)
        return dp[n]