'''
Title     : 12. Integer to Roman
Problem   : https://leetcode.com/problems/integer-to-roman/
'''
''' Reference: https://leetcode.com/problems/integer-to-roman/discuss/292605/Python-Solution-44ms '''
class Solution:
    def intToRoman(self, num: int) -> str:
        d = {1000: 'M', 900: 'CM', 500: 'D', 400: 'CD', 100: 'C', 90: 'XC', 50: 'L', 40: 'XL', 10: 'X', 9: 'IX', 5: 'V', 4: 'IV', 1: 'I'}
        res = ''
        for n in d:
            while num >= n:
                res += d[n]
                num -= n
        return res

''' Reference: https://leetcode.com/problems/integer-to-roman/discuss/6274/Simple-Solution '''
class Solution:
    def intToRoman(self, num: int) -> str:
        M = ['', 'M', 'MM', 'MMM', 'MMMM']
        C = ['', 'C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM']
        X = ['', 'X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC', ]
        I = ['', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX', ]
        return M[num//1000] + C[(num%1000)//100] + X[(num%100)//10] + I[num%10]