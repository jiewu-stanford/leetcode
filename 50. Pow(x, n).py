'''
Title     : 50. Pow(x, n) (XXX)
Problem   : https://leetcode.com/problems/powx-n/
'''
'''
recursive solution
Reference: https://leetcode.com/problems/powx-n/discuss/19560/Shortest-Python-Guaranteed
'''
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        elif n < 0:
            return 1/self.myPow(x, -n)
        elif n % 2:
            return x*self.myPow(x, n-1)
        return self.myPow(x*x, n//2)