'''
Title     : 309. Best Time to Buy and Sell Stock with Cooldown
Problem   : https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/
'''
'''
1D DP solution, 1 DP for each of the three states: (1) hold (2) sell (3) cool
Reference: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/discuss/151887/Classic-DP-Python-beats-97
'''
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n < 2: return 0
        hold, sell, cool = [0]*n, [0]*n, [0]*n
        hold[0] = -prices[0]
        for i in range(1, n):   # 3 states with 5 state transitions
            hold[i] = max(hold[i-1], cool[i-1]-prices[i])   # sell[i-1]-prices[i] is disallowed here due to the cool-down restriction
            sell[i] = max(sell[i-1], hold[i-1]+prices[i])   # cool[i-1] does not go to sell[i] due to the cool-down restriction on day i+1 for sell[i]
            cool[i] = max(cool[i-1], sell[i-1])
        return sell[-1]