'''
Title     : 162. Find Peak Element
Problem   : https://leetcode.com/problems/find-peak-element/
'''
'''
it is equivalent to finding local maxima, simply change the stop condition of binary search (== target) to (< and >)
note that we do not need to sort the list because it is locally ascending right before local maxima and locally descending right after
'''
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1
        while l < r:   # l <= r will make nums[mid+1] index out of bound
            mid = (l + r) // 2
            if nums[mid-1] < nums[mid] > nums[mid+1]:
                return mid
            elif nums[mid] <= nums[mid+1]:
                l = mid + 1
            else:
                r = mid - 1
        return l