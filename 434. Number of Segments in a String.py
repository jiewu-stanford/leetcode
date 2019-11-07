'''
Title     : 434. Number of Segments in a String
Problem   : https://leetcode.com/problems/number-of-segments-in-a-string/
'''
class Solution:
    def countSegments(self, s: str) -> int:
        return len(s.split())

''' Reference: https://leetcode.com/problems/number-of-segments-in-a-string/discuss/91619/Python-One-liner-without-split '''
class Solution:
    def countSegments(self, s: str) -> int:
        return sum(s[i]!=' ' and (i==0 or s[i-1]==' ') for i in range(len(s)))