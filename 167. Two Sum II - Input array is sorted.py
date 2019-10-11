'''
Title     : 167. Two Sum II - Input array is sorted
Problem   : https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
'''
''' just modify on top of the 1. solution '''
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if len(nums) < 2: return []
        d = {}
        for i, val in enumerate(nums):
            diff = target - val
            if diff in d:
                return [d[diff]+1, i+1]   # return [i, d[diff]] in the 1. solution
            else:
                d[val] = i
'''
two pointers + search from both ends
Reference: Reference: https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/discuss/51249/Python-different-solutions-(two-pointer-dictionary-binary-search)
'''
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if len(nums) < 2: return []
        l, r = 0, len(nums)-1
        while l < r:
            s = nums[l] + nums[r]
            if s == target:
                return [l+1, r+1]
            elif s < target:
                l += 1
            else:
                r -= 1

''' can expedite the search using binary search, enabled by sorted '''
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if len(nums) < 2: return []
        for i in range(len(nums)):
            l, r = i+1, len(nums)-1   # +1 to ensure mid = (l+r)//2 > i
            tmp = target - nums[i]
            while l <= r:
                mid = (l + r) // 2
                if nums[mid] == tmp:
                    return [i+1, mid+1]
                elif nums[mid] < tmp:
                    l = mid + 1
                else:
                    r = mid - 1