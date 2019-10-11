'''
Title     : 400. Nth Digit
Problem   : https://leetcode.com/problems/nth-digit/
'''
''' Reference: https://leetcode.com/problems/nth-digit/discuss/88375/Short-Python%2BJava '''
class Solution:
    def findNthDigit(self, n: int) -> int:
        n -= 1
        for digit in range(1, 11):
            tens = 10**(digit - 1)
            if n < 9*tens*digit:   # next check whether in same length 10-99, 100-999, 1000-9999 etc.
                return int(str(tens + n//digit)[n % digit])   # the number containing the nth digit is tens + n//digit
            n -= 9*tens*digit