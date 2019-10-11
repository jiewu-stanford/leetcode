'''
Title     : 26. Remove Duplicates from Sorted Array
Problem   : https://leetcode.com/problems/remove-duplicates-from-sorted-array/
'''
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums: return 0
        prev, curr = 0, 1
        while curr < len(nums):
            if nums[prev] == nums[curr]:
                curr += 1
            else:
                prev += 1
                nums[prev] = nums[curr]
        return prev + 1