'''
Title     : 277. Find the Celebrity ($$$)
Problem   : https://leetcode.com/problems/find-the-celebrity/
          : https://www.lintcode.com/problem/find-the-celebrity/description
'''
class Celebrity:
    def knows(self, a: int, b: int) -> bool: pass

class Solution:
    def findCelebrity(self, n):
        candidate = 0
        for ii in range(1, n):
            if Celebrity.knows(candidate, ii):
                candidate = ii
        for ii in range(n):
            if ii!=candidate and Celebrity.knows(candidate,ii) or not Celebrity.knows(ii,candidate):
                return -1
        return candidate