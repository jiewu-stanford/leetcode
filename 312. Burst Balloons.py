'''
Title     : 312. Burst Balloons
Problem   : https://leetcode.com/problems/burst-balloons/description/
'''
'''
Reference: https://leetcode.com/problems/burst-balloons/discuss/76243/Python-DP-N3-Solutions
Reference: https://leetcode.com/problems/burst-balloons/discuss/76229/For-anyone-that-is-still-confused-after-reading-all-kinds-of-explanations...
'''
'''
bottom-up approach using standard DP, use the trick of padding nums on both sides with [1] to cover the entire range of the original nums (remember boundaries are excluded)
dp[i][j] = the maximum coins we get after bursting all the balloons between i and j (excluding i and j themselves)
'''
class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        n = len(nums)
        dp = [[0]*n for _ in range(n)]
        for gap in range(2, n):
            for left in range(n - gap):
                right = left + gap
                for i in range(left+1, right):
                    dp[left][right] = max(dp[left][right],
                                        dp[left][i] + dp[i][right] + nums[left]*nums[i]*nums[right])
                                        # dp[left][i] = maximum coins of bursting all the balloon on the left side of i
                                        # dp[i][right] = maximum value of bursting all the balloon on the right side of i
                                        # nums[left]*nums[i]*nums[right] = bursting balloon i last when left side and right side are gone
        return dp[0][n-1]

''' top-down approach with recursive helper function '''
class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        n = len(nums)
        dp = [[0]*n for _ in range(n)]

        def helper(left, right):
            if dp[left][right] or right == left + 1:
                return dp[left][right]
            coins = 0
            for i in range(left+1, right):
                coins = max(coins, helper(left,i) + helper(i, right) + nums[left]*nums[i]*nums[right])
            dp[left][right] = coins
            return coins

        return helper(0, n-1)