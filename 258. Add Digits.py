'''
Title     : 258. Add Digits (XXX)
Problem   : https://leetcode.com/problems/add-digits/
'''
class Solution:
    def addDigits(self, num: int) -> int:
        if num == 0: return 0
        r = num % 9
        return r if r else 9