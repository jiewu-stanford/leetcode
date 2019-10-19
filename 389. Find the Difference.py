'''
Title     : 389. Find the Difference
Problem   : https://leetcode.com/problems/find-the-difference/
'''
'''
convert to ASCII number and do arithmetic
Reference: https://leetcode.com/problems/find-the-difference/discuss/86946/1-liners-Python-%2B-Ruby
'''
class Solution(object):
    def findTheDifference(self, s, t):
        return chr(sum(map(ord, t)) - sum(map(ord, s)))
'''
user Counter() to count each character
Reference: https://leetcode.com/problems/find-the-difference/discuss/86845/1-liners-and-2-liner-in-Python
'''
from collections import Counter
class Solution(object):
    def findTheDifference(self, s, t):
        return list((Counter(t) - Counter(s)))[0]