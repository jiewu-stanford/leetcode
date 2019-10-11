'''
Title     : 154. Find Minimum in Rotated Sorted Array II
Problem   : https://leetcode.com/problems/find-minimum-in-rotated-sorted-array-ii/
'''
'''
just add the step of jumping over repeated number in 153. solution
Reference: https://leetcode.com/problems/find-minimum-in-rotated-sorted-array-ii/discuss/241815/Python-solution
'''
class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]
        first, last = 0, len(nums)-1
        while first < last:
            mid = (first + last) // 2
            if nums[mid] > nums[last]:
                first = mid + 1
            elif nums[mid] < nums[last]:
                last = mid
            else:
                last -= 1   # skip repeated number
        return nums[first]