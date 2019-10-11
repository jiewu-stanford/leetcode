'''
Title     : 29. Divide Two Integers (XXX)
Problem   : https://leetcode.com/problems/divide-two-integers/
'''
class Solution:
    def divide(self, dividend, divisor):
        maxInt = 2**31 - 1
        if divisor == 0:
            return maxInt
        if dividend == 0:
            return 0
        negative = (dividend > 0) ^ (divisor > 0)
        dividend, divisor = abs(dividend), abs(divisor)
        res = 0
        while dividend >= divisor:
            x = divisor
            i = 1
            while dividend >= x + x:
                x += x
                i += i
            dividend -= x
            res += i
        res = maxInt if not negative and res > maxInt else res
        return -res if negative else res