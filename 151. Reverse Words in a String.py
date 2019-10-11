'''
Title     : 151. Reverse Words in a String (XXX)
Problem   : https://leetcode.com/problems/reverse-words-in-a-string/
'''
class Solution:
    def reverseWords(self, s: str) -> str:
        return ' '.join(s.split()[::-1])
        # return ' '.join(reversed(s.split()))