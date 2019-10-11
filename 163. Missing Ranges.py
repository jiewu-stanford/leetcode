'''
Title     : 163. Missing Ranges ($$$)
Problem   : https://leetcode.com/problems/missing-ranges/description/
          : https://www.lintcode.com/problem/missing-ranges/description
'''
''' Reference: https://www.cnblogs.com/lightwindy/p/9640454.html '''
class Solution:
    def findMissingRanges(self, nums, lower, upper):
        ranges = []
        prev = lower - 1
        for i in range(len(nums)+1):
            if i == len(nums): curr = upper + 1
            else: curr = nums[i]
            if curr - prev > 1:
                ranges.append(self.printout(prev+1, curr-1))
            prev = curr
        return ranges
        
    def printout(self, lower, upper):
        if lower == upper:
            return '{}'.format(lower)
        else:
            return '{}->{}'.format(lower, upper)