'''
Title     : 34. Find First and Last Position of Element in Sorted Array
Problem   : https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
'''
'''
use the built-in methods bisect_left and bisect_right in the bisect module
Reference: https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/discuss/236386/Python-solution
'''
import bisect
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums: return [-1, -1]
        left = bisect.bisect_left(nums, target)
        right = bisect.bisect_right(nums, target)
        if 0 <= left < len(nums) and nums[left] == target:
            return [left, right-1]
        else:
            return [-1, -1]

''' recursive solution with helper function, ibid. '''
class Solution(object):
    def searchRange(self, nums, target):
        if not nums: return [-1, -1]
        left = self.binarySearch(nums, target, True)
        right = self.binarySearch(nums, target, False)
        if 0 <= left < len(nums) and nums[left] == target:
            return [left, right-1]
        else:
            return [-1, -1]
        
    def binarySearch(self, nums, target, fromLeft=True):
        l, r = 0, len(nums)
        while l < r:
            mid = (l + r) // 2
            if nums[mid] == target:
                if fromLeft: r = mid
                else: l = mid + 1
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid
        return l
'''
the fromLeft = True/False option can be implemented with -0.5/+0.5 trick thanks to the ascending order
Reference: https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/discuss/14713/Search-for-the-position-target-0.5-and-target%2B0.5-a-simple-python-code-with-a-little-trick
'''
class Solution(object):
    def searchRange(self, nums, target):
        if not nums: return [-1, -1]
        left = self.binarySearch(nums, target-0.5)
        nums.append(0)
        right = self.binarySearch(nums, target+0.5)
        if nums[left] == target:
            return [left, right-1]
        else:
            return [-1, -1]

    def binarySearch(self, nums, target):
        l, r = 0, len(nums)-1
        while l < r:
            mid = (l + r) // 2
            if nums[mid] > target:
                r = mid
            else:
                l = mid + 1
        return l
'''
iterative solution without using helper function, two passes explicitly spelling out the helper function steps
Reference: https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/discuss/14706/Beats-100-Python-submission
'''
class Solution(object):
    def searchRange(self, nums, target):
        if not nums: return [-1, -1]
        l, r = 0, len(nums)-1
        while l < r:
            mid = (l + r) // 2
            if nums[mid] < target: l = mid + 1
            else: r = mid
        
        if nums[l] != target: return [-1, -1]
        else: left = l
        
        l, r = left, len(nums)-1
        while l < r:
            mid = (l + r) // 2 + 1
            if nums[mid] == target: l = mid   # <- l = mid + 1, since +1 in mid
            else: r = mid - 1                 # <- r = mid, -1 to break the while loop
        right = l
        return [left, right]