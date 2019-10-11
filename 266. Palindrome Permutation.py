'''
Title     : 266. Palindrome Permutation ($$$)
Problem   : https://leetcode.com/problems/palindrome-permutation/
          : https://www.lintcode.com/problem/palindrome-permutation/description
'''
class Solution(object):
    def canPermutePalindrome(self, s: str) -> bool:
        d = {}
        for i in s:
            d[i] = d.get(i, 0) + 1
        count = 0
        for i in d.values():
            if i % 2 != 0:
                count += 1
            if count > 1:   # only one odd repetition is allowed
                return False
        return True