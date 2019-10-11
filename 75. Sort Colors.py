'''
Title     : 75. Sort Colors
Problem   : https://leetcode.com/problems/sort-colors/
'''
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        i, first, last = 0, 0, len(nums)-1
        while i <= last:
            if nums[i] == 0:
                nums[first], nums[i] = nums[i], nums[first]
                first += 1
                i += 1
            elif nums[i] == 2:
                nums[last], nums[i] = nums[i], nums[last]
                last -= 1   # don't i += 1 as we need to compare swapped nums[last] and swap it again if necessary
            elif nums[i] == 1:
                i += 1