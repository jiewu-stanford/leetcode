'''
Title     : 81. Search in Rotated Sorted Array II
Problem   : https://leetcode.com/problems/search-in-rotated-sorted-array-ii/
'''
''' modify directly on the 80. solution '''
class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        def helper(nums, l, r, target):
            if l > r: return False
            mid = (l + r) // 2
            if nums[mid] == target:
                return True
            if nums[l] < nums[mid]:   # nums[l] <= nums[mid] in the 80. solution
                if nums[l] <= target < nums[mid]:
                    return helper(nums, l, mid-1, target)
                else:
                    return helper(nums, mid+1, r, target)
            elif nums[l] > nums[mid]:
                if nums[mid] < target <= nums[r]:
                    return helper(nums, mid+1, r, target)
                else:
                    return helper(nums, l, mid-1, target)
            else:
                return helper(nums, l+1, r, target)   # skip repeated number
        
        return helper(nums, 0, len(nums)-1, target)

''' modify directly on the 80. solution '''
class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        l, r = 0, len(nums)-1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return True
            while l < mid and nums[l] == nums[mid]:   # skip repeated number
                l += 1
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
        return False