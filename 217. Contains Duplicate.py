'''
Title     : 217. Contains Duplicate (XXX)
Problem   : https://leetcode.com/problems/contains-duplicate/
'''
''' use set() '''
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(nums) > len(set(nums))

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        s = set()
        for num in nums:
            if num not in s: s.add(num)
            else: return True
        return False

''' use dictionary '''
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        d = {}
        for num in nums:
            if num not in d: d[num] = 1
            else: return True
        return False

''' use sort() '''
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i-1] == nums[i]:
                return True
        return False