'''
Title     : 188. Best Time to Buy and Sell Stock IV
Problem   : https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/
'''
'''
generalization from the oneBuy, oneBuyoneSell, twoBuyoneSell, twoBuytwoSell update pattern in the 123. solution
Reference: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/discuss/54230/Short-python-solution-from-weijiac's-Best-Time-to-Buy-and-Sell-Stock-III
'''
class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        if n < 2: return 0
        if k >= n // 2:   # more than enough transactions allowed, reduced to the 122. solution
            return sum(i-j for i,j in zip(prices[1:], prices[:-1]) if i-j > 0)
        
        hold, sell = [-float('inf')]*(k+1), [0]*(k+1)
        for i in range(n):
            for j in range(1, k+1):
                sell[j] = max(sell[j], hold[j]+prices[i])   # oneBuy + prices[i], twoBuyoneSell + prices[i]
                hold[j] = max(hold[j], sell[j-1]-prices[i])

        return sell[k]
'''
2D DP solution combining the two 1D DP for hold and sell
Reference: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/discuss/54135/Python-solution-with-detailed-explanation
'''
class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        if n < 2: return 0
        if k >= n // 2:
            return sum(i-j for i,j in zip(prices[1:], prices[:-1]) if i-j > 0)

        dp = [[0]*n for _ in range(k+1)]   # sell = [0]*(k+1)
        for j in range(1, k+1):
            hold = -prices[0]
            for i in range(1, n):
                dp[j][i] = max(dp[j][i-1], hold+prices[i])   # sell[j] = max(sell[j], hold[j]+prices[i])
                hold = max(hold, dp[j-1][i-1]-prices[i])   # hold[j] = max(hold[j], sell[j-1]-prices[i])
        
        return dp[k][-1]
'''
another 2D DP solution, using a different variable 'presentSell' in place of 'hold'
Reference: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/discuss/54131/Well-explained-Python-DP-with-comments
'''
class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        if n < 2: return 0
        if k >= n // 2:
            return sum(i-j for i,j in zip(prices[1:], prices[:-1]) if i-j > 0)

        dp = [[0]*n for _ in range(k+1)]
        for j in range(1, k+1):
            presentSell = 0
            for i in range(1, n):
                presentSell = max(dp[j-1][i-1] + prices[i]-prices[i-1],   # buy on day i-1 and sell on day i
                                  dp[j-1][i-1],   # buy on day i and sell on the same day i
                                  presentSell + prices[i]-prices[i-1])    # cancel sell on i-1 and sell instead on day i
                dp[j][i] = max(dp[j][i-1], presentSell)   # all sell completed by day i-1 vs. all sell completed by day i

        return dp[k][-1]