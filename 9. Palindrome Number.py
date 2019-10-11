'''
Title     : 9. Palindrome Number
Problem   : https://leetcode.com/problems/palindrome-number/
'''
''' convert to string and reverse it '''
class Solution:
    def isPalindrome(self, x: int) -> bool:
        return x >= 0 and x == int(str(x)[::-1])