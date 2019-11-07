'''
Title     : 415. Add Strings
Problem   : https://leetcode.com/problems/add-strings/
'''
''' Reference: https://leetcode.com/problems/add-strings/discuss/90455/Python-solution-using-zip_longest() '''
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        res, carry, digit = '', 0, 0
        num1, num2 = list(num1), list(num2)
        while num1 or num2 or carry:
            a, b = 0, 0
            if num1:
                a = int(num1[-1])
                num1.pop()
            if num2:
                b = int(num2[-1])
                num2.pop()
            carry, digit = divmod(a + b + carry, 10)   # carry, digit = (a + b + carry) // 10, (a + b + carry) % 10
            res = str(digit) + res
        return res