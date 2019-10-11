'''
Title     : 123. Best Time to Buy and Sell Stock III
Problem   : https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/
'''
'''
maintain and update 4 variables throughout the scan: oneBuy, oneBuyoneSell, twoBuyoneSell, twoBuytwoSell
Reference: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/discuss/39611/Is-it-Best-Solution-with-O(n)-O(1)
'''
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n < 2: return 0
        oneBuy, oneBuyoneSell, twoBuyoneSell, twoBuytwoSell = -float('inf'), 0, -float('inf'), 0
        for i in range(n):
            # be careful about the order of update, which is determined by the fact that all variables on the right-hand side should refer to those of yesterday
            twoBuytwoSell = max(twoBuytwoSell, twoBuyoneSell + prices[i])
            twoBuyoneSell = max(twoBuyoneSell, oneBuyoneSell - prices[i])
            oneBuyoneSell = max(oneBuyoneSell, oneBuy + prices[i])
            oneBuy = max(oneBuy, -prices[i])
        return max(oneBuyoneSell, twoBuytwoSell)
'''
two-pass solution, one from beginning one from end, inspired by the idea that one cannot buy the second without selling the first
Reference: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/discuss/39743/Python-DP-solution-120ms
'''
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n < 2: return 0
        profits, maxGain, currMin = [], 0, prices[0]
        for i in range(n):
            maxGain = max(maxGain, prices[i]-currMin)
            profits.append(maxGain)
            currMin = min(currMin, prices[i])
        
        totalMax, maxGain, currMax = 0, 0, prices[-1]
        for i in range(n-1, -1, -1):
            maxGain = max(maxGain, currMax-prices[i])
            totalMax = max(totalMax, maxGain+profits[i])   # profits[i] is the max profit over [0:i] thus no overlap
            currMax = max(currMax, prices[i])
            
        return totalMax
'''
the explicit DP version of the two-pass solution
Reference: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/discuss/39661/Python-DP-intuitive-solution
'''
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n < 2: return 0
        forwardPass = [0] * len(prices)
        backwardPass = [0] * len(prices)

        currMin = prices[0]
        for i in range(1, n):
            forwardPass[i] = max(forwardPass[i-1], prices[i]-currMin)   # maxGain = max(maxGain, prices[i]-currMin)
            currMin = min(currMin, prices[i])

        currMax = prices[-1]
        for i in range(n-2, -1, -1):
            backwardPass[i] = max(backwardPass[i+1], currMax-prices[i])   # maxGain = max(maxGain, currMax-prices[i])
            currMax = max(currMax, prices[i])

        profits = [i+j for i,j in zip(forwardPass, backwardPass)]   # totalMax = max(totalMax, maxGain+profits[i])
        return max(profits)