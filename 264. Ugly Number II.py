'''
Title     : 264. Ugly Number II
Problem   : https://leetcode.com/problems/ugly-number-ii/
'''
'''
straightforward step-by-step implementation
Reference: https://leetcode.com/problems/ugly-number-ii/discuss/69384/My-expressive-Python-solution
'''
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        ugly = [1]
        i2, i3, i5 = 0, 0, 0   # index of multiples of prime 2, 3, 5
        while n > 1:
            u2, u3, u5 = 2*ugly[i2], 3*ugly[i3], 5*ugly[i5]
            umin = min(u2, u3, u5)
            if umin == u2: i2 += 1
            if umin == u3: i3 += 1
            if umin == u5: i5 += 1
            ugly.append(umin)
            n -= 1
        return ugly[-1]