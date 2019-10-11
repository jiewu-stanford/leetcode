'''
Title     : 33. Search in Rotated Sorted Array
Problem   : https://leetcode.com/problems/search-in-rotated-sorted-array/
'''
''' user recursive helper function '''
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def helper(nums, l, r, target):
            if l > r: return -1
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            if nums[l] <= nums[mid]:    # ascending towards center
                if nums[l] <= target < nums[mid]:
                    return helper(nums, l, mid-1, target)
                else:
                    return helper(nums, mid+1, r, target)
            else:                       # descending towards center
                if nums[mid] < target <= nums[r]:
                    return helper(nums, mid+1, r, target)
                else:
                    return helper(nums, l, mid-1, target)
        
        return helper(nums, 0, len(nums)-1, target)

''' iterative solution '''
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            if nums[l] <= nums[mid]:
                if nums[l] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
        return -1