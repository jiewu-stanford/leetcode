'''
Title     : 35. Search Insert Position
Problem   : https://leetcode.com/problems/search-insert-position/
'''
''' clear O(n) solution without using binary search '''
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        return len([num for num in nums if num < target])
'''
O(logn) binary search solution with duplicate handler
Reference: https://leetcode.com/problems/search-insert-position/discuss/15378/A-fast-and-concise-python-solution-40ms-binary-search
'''
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] < target:
                l = mid + 1
            else:
                if nums[mid] == target and nums[mid-1] != target:
                    return mid
                else:
                    r = mid - 1
        return l