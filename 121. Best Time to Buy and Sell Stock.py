'''
Title     : 121. Best Time to Buy and Sell Stock
Problem   : https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
'''
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n < 2: return 0
        maxGain, lowPrice = 0, prices[0]
        for i in range(1, n):
            lowPrice = min(lowPrice, prices[i])
            maxGain = max(maxGain, prices[i]-lowPrice)
        return maxGain
'''
1D DP solution, dp[i] = profit accumulated up to day i
Reference: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/discuss/39138/Python-DP-solution
'''
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n < 2: return 0
        dp = [0] * n
        for i in range(1, n):
            dp[i] = max(0, dp[i-1] + prices[i]-prices[i-1])  # profit accumulated up to yesterday + today's profit
        return max(dp)