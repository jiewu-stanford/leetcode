'''
Title     : 189. Rotate Array
Problem   : https://leetcode.com/problems/rotate-array/
'''
''' straightforward implementation of the rotation step by step via appendleft() '''
import collections
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        d = collections.deque(nums)
        k %= len(nums)
        for _ in range(k):
            d.appendleft(d.pop())
        nums[:] = list(d)
        
''' explore the structure after rotation, and faster '''
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        l = len(nums)
        nums[:] = nums[l-(k%l):] + nums[:l-(k%l)]