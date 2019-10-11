'''
Title     : 324. Wiggle Sort II
Problem   : https://leetcode.com/problems/wiggle-sort-ii/
'''
''' use [::-1] for reversed order, the problem statement itself is ambiguous '''
class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        nums.sort()
        L = len(nums)
        mid = L//2 if L % 2 == 0 else L//2+1
        nums[::2], nums[1::2] = nums[:mid][::-1], nums[mid:][::-1]