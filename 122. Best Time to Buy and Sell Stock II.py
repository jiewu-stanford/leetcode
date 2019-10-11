'''
Title     : 122. Best Time to Buy and Sell Stock II
Problem   : https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/
'''
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        return sum(max(prices[i+1]-prices[i],0) for i in range(len(prices)-1))   # buy today and sell tomorrow if profitable and do nothing otherwise
        # return sum(i-j for i,j in zip(prices[1:], prices[:-1]) if i-j > 0)