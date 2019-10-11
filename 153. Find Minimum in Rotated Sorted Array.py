'''
Title     : 153. Find Minimum in Rotated Sorted Array
Problem   : https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
'''
class Solution(object):
    def findMin(self, nums):
        if len(nums) == 1: return nums[0]
        first, last = 0, len(nums)-1
        while first < last:
            mid = (first + last) // 2
            if nums[mid] > nums[last]:
                first = mid + 1
            else:
                last = mid
        return nums[first]