'''
Title     : 278. First Bad Version
Problem   : https://leetcode.com/problems/first-bad-version/
'''
# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
def isBadVersion(version): pass

class Solution:
    def firstBadVersion(self, n):
        l, r = 0, n - 1
        while l <= r:
            mid = (l + r) // 2
            if isBadVersion(mid) == False:
                l = mid + 1
            else:
                r = mid - 1
        return l