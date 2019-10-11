'''
Title     : 169. Majority Element (XXX)
Problem   : https://leetcode.com/problems/majority-element/
'''
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        return None if not nums else sorted(nums)[len(nums)//2]