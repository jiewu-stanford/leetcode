'''
Title     : 280. Wiggle Sort ($$$)
Problem   : https://leetcode.com/problems/wiggle-sort/
          : https://www.lintcode.com/problem/wiggle-sort/description    
'''
class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        for i in range(len(nums)-1):
            if i % 2 == 1 and nums[i] < nums[i+1]:
                nums[i], nums[i+1] = nums[i+1], nums[i]
            elif i % 2 == 0 and nums[i] > nums[i+1]:
                nums[i], nums[i+1] = nums[i+1], nums[i]