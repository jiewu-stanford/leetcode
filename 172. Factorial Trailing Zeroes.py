'''
Title     : 172. Factorial Trailing Zeroes
Problem   : https://leetcode.com/problems/factorial-trailing-zeroes/
'''
''' add a trailing zero every time a factor of 5 is multipled hence number of trailing 0s = number of 5 factors (https://en.wikipedia.org/wiki/Trailing_zero#Factorial)'''
class Solution:
    def trailingZeroes(self, n: int) -> int:
        res = 0
        while n > 0:
            n = n // 5
            res += n
        return res

''' recursive solution '''
class Solution:
    def trailingZeroes(self, n: int) -> int:
        return 0 if n < 5 else n//5 + self.trailingZeroes(n//5)