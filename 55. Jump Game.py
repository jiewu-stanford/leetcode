'''
Title     : 55. Jump Game
Problem   : https://leetcode.com/problems/jump-game/
'''
''' find the max reach iteratively '''
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        reach = 0
        for i in range(len(nums)):
            if reach >= i: reach = max(reach, i+nums[i])   # reach >= i ensures that i is within reach thus nums[i] steps can be added
        return reach >= len(nums)-1

''' traverse backward to find the smallest starting index from which the end can be reached '''
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        start = n - 1
        for i in range(n-1, -1, -1):
            if i + nums[i] >= start: start = i
        return start <= 0