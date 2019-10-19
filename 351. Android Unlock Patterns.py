'''
Title     : 351. Android Unlock Patterns ($$$)
Problem   : https://leetcode.com/problems/android-unlock-patterns/description/
          : https://www.lintcode.com/problem/android-unlock-patterns/description
'''
'''
1D DP solution
Reference: https://www.cnblogs.com/lightwindy/p/9656168.html
'''
class Solution:
    def numberOfPatterns(self, m, n):
        def merge(used, i):
            return used | (1 << i)
        def number_of_keys(i):
            number = 0
            while i > 0:
                i &= i - 1
                number += 1
            return number
        def contain(used, i):
            return bool(used & (1 << i))
        def convert(i, j):
            return 3*i + j

        dp = [[0]*9 for _ in range(1 << 9)]   # dp[i][j] = number of ways ending at j
        for i in range(9):
            dp[merge(0, i)][i] = 1
        res = 0
        for used in range(len(dp)):
            num = number_of_keys(used)
            if num > n: continue
            for i in range(9):
                if not contain(used, i): continue
                if m <= num <= n:
                    res += dp[used][i]
                x1, y1 = divmod(i, 3)
                for j in range(9):
                    if contain(used, j): continue
                    x2, y2 = divmod(j, 3)
                    if ((x1 == x2 and abs(y1 - y2) == 2) or
                        (y1 == y2 and abs(x1 - x2) == 2) or
                        (abs(x1-x2)==2 and abs(y1-y2)==2)) and not contain(used, convert((x1+x2)//2, (y1+y2)//2)): continue
                    dp[merge(used, j)][j] += dp[used][i]
        return res