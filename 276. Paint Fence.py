'''
Title     : 276. Paint Fence ($$$)
Problem   : https://leetcode.com/problems/paint-fence/
          : https://www.lintcode.com/problem/paint-fence/
'''
'''
the induction reduces to considering the last two posts: diff = # ways when they are of different colors, same = # ways when they are the same
Reference (induction step): https://www.geeksforgeeks.org/painting-fence-algorithm/
Reference (clean code): http://www.voidcn.com/article/p-cqzythcg-qp.html
'''
class Solution:
    def numWays(self, n, k):
        if n == 0: return 0
        elif n == 1: return k
        sameColor, diffColor = k, k*(k-1)   # for n == 2
        for _ in range(2, n):
            tmp = diffColor
            diffColor = (sameColor + diffColor) * (k-1)
            sameColor = tmp
        return sameColor + diffColor
'''
the induction can be further deduced to T(n) = (k-1)[T(n-1) + T(n-2)] where 'T' is Total = sameColor + diffColor
Reference (induction step): https://codereview.stackexchange.com/questions/63614/count-number-of-ways-to-paint-a-fence-with-n-posts-using-k-colors
Reference (clean code): https://github.com/KrisYu/LeetCode-CLRS-Python/blob/master/276.%20Paint%20Fence.md
'''
class Solution:
    def numWays(self, n, k):
        if n == 0: return 0
        elif n == 1: return k
        elif n == 2: return k*k
        else:
            dp = [0 for _ in range(n+1)]
            dp[0] = 0
            dp[1] = k
            dp[2] = k*k
            for i in range(3, n+1):
                dp[i] = (dp[i-1] + dp[i-2])*(k-1)
            return dp[-1]