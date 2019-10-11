'''
Title     : 233. Number of Digit One
Problem   : https://leetcode.com/problems/number-of-digit-one/
'''
'''
iterative solution with illustrative examples, start counting from last digit
Reference: https://leetcode.com/problems/number-of-digit-one/discuss/64382/JavaPython-one-pass-solution-easy-to-understand
'''
class Solution:
    def countDigitOne(self, n: int) -> int:
        if n <= 0: return 0
        elif 1 <= n <= 9: return 1
        q, x, res = n, 1, 0
        while q > 0:
            digit = q % 10
            q //= 10
            res += q * x           # e.g. n = 312 has 3*10 numbers (x = 10) with '1' in the 10s position and a digit < 3 in the 100s position
            if digit == 1:
                res += n % x + 1   # e.g. n = 312 has 2 + 1 numbers with '1' in the 10s position and digit == 3 in the 100s position
            elif digit > 1:
                res += x           # e.g. n = 322 has 2 numbers with '1' in the 10s position and digit == 3 in the 100s position
            x *= 10
        return res
'''
recursive solution, start counting from leading digit
Reference: https://leetcode.com/problems/number-of-digit-one/discuss/64462/Python-recursive-solution-(with-comments)
'''
class Solution:
    def countDigitOne(self, n: int) -> int:
        if n <= 0: return 0
        elif 1 <= n <= 9: return 1
        q, x = n, 1
        while q > 9:
            x *= 10; q //= 10
        if q == 1:
            return self.countDigitOne(x-1) + self.countDigitOne(n-x) + (n-x+1)
            # e.g. n = 132, total = #(0--99) + #(100--132 with '1' in 10s and 1s position) + #(100--132 with '1' in 100s position)
        else:
            return self.countDigitOne(x-1)*q + self.countDigitOne(n-q*x) + x
            # e.g. n = 232, total = #(0--99 and 100--199 with '1' in 10s and 1s position) + #(200--232 with '1' in 10s and 1s position) + #(100-199 with '1' in 100s position)