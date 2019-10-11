'''
Title     : 283. Move Zeroes
Problem   : https://leetcode.com/problems/move-zeroes/
'''
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        count = nums.count(0)
        nums[:] = [i for i in nums if i != 0]
        if count:
            nums += [0]*count