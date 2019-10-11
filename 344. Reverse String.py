'''
Title     : 344. Reverse String (XXX)
Problem   : https://leetcode.com/problems/reverse-string/
'''
class Solution:
    def reverseString(self, s: List[str]) -> None:
        return s[::-1]

class Solution:
    def reverseString(self, s: List[str]) -> None:
        return ''.join(reversed(list(s)))

''' recursive solution '''
class Solution:
    def reverseString(self, s: List[str]) -> None:
        if len(s) <= 1: return s
        n = len(s)
        return self.reverseString(s[n//2:]) + self.reverseString(s[:n//2])
