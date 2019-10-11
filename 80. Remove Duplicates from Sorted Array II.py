'''
Title     : 80. Remove Duplicates from Sorted Array II
Problem   : https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/
'''
''' compare 26. and 80. '''
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) <= 2: return len(nums)
        prev, curr = 1, 2
        while curr < len(nums):
            if nums[prev-1]==nums[curr] and nums[prev]==nums[curr]:
                curr += 1
            else:
                prev += 1
                nums[prev] = nums[curr]
                curr += 1
        return prev + 1