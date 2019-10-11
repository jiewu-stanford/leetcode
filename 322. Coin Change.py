'''
Title     : 322. Coin Change
Problem   : https://leetcode.com/problems/coin-change/description/
'''
'''
1D DP solution
Reference: https://leetcode.com/problems/coin-change/discuss/77372/Clean-dp-python-code
'''
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount+1)
        dp[0] = 0
        for i in range(1, amount+1):
            for coin in coins:
                if coin > i:
                    continue
                else:
                    dp[i] = min(dp[i], dp[i-coin]+1)
        return dp[-1] if dp[-1]!=float('inf') else -1
'''
BFS iterative solution
Reference: https://leetcode.com/problems/coin-change/discuss/77361/Fast-Python-BFS-Solution
'''
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        balances = visited = {0}
        n = 0
        while balances:
            if amount in balances:
                return n
            balances = {balance+coin for balance in balances for coin in coins
                        if balance+coin <= amount and balance+coin not in visited}
            visited |= balances   # s |= t return set s with elements added from t, equivalent to s.update(t)
            n += 1
        return -1