'''
Title     : 171. Excel Sheet Column Number
Problem   : https://leetcode.com/problems/excel-sheet-column-number/
'''
class Solution:
    def titleToNumber(self, s: str) -> int:
        res = 0
        for c in s:
            res = res*26 + ord(c) - ord('A') + 1
        return res
        # return reduce(lambda x, y: 26*x+ord(y)-64, s, 0)