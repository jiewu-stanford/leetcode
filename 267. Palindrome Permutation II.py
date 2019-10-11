'''
Title     : 267. Palindrome Permutation II ($$$)
Problem   : https://leetcode.com/problems/palindrome-permutation-ii/
          : https://www.lintcode.com/problem/palindrome-permutation-ii/description
'''
'''
first collect all characters and their number of repetitions, then form unique permutations using itertools.permutations() function and set()
Reference: https://www.itread01.com/content/1521787096.html
'''
import collections, itertools
class Solution:
    def generatePalindromes(self, s):
        count = collections.Counter(s)
        oddChars = tuple(key for key, val in count.items() if val % 2)
        halfChars = ''.join(key*(val//2) for key, val in count.items())
        if len(oddChars) < 2:   # only one odd repetition is allowed for any palindrome
            if len(set(halfChars)) > 1:
                res = [''.join(halfPalin + oddChars + halfPalin[::-1]) for halfPalin in set(itertools.permutations(halfChars))]
            else:
                res = [''.join((halfChars,) + oddChars + (halfChars,))]
        else:
            res = []
        return res