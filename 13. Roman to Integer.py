'''
Title     : 13. Roman to Integer
Problem   : https://leetcode.com/problems/roman-to-integer/
'''
''' Reference: https://leetcode.com/problems/roman-to-integer/discuss/6542/4-lines-in-Python '''
class Solution:
    def romanToInt(self, s: str) -> int:
        d = {'M':1000, 'D':500, 'C':100, 'L':50, 'X':10, 'V':5, 'I':1}
        res, p = 0, 'I'
        for c in s[::-1]:
            res = res - d[c] if d[c] < d[p] else res + d[c]   # res - d[c] case e.g. IV = 4 = 5 - 1
            p = c
        return res