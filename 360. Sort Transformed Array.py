'''
Title     : 360. Sort Transformed Array ($$$)
Problem   : https://leetcode.com/problems/sort-transformed-array/description/
          : https://www.lintcode.com/problem/sort-transformed-array/description
'''
'''
just how to implement sort(), below is an O(1) implementation based on the curvature of y = ax^2 + bx + c
Reference: https://www.jasonjson.com/archivers/sort-transformed-array
'''
class Solution:
    def sortTransformedArray(self, nums, a, b, c):
        nums = [a*num*num + b*num + c for num in nums]
        res = [0] * len(nums)
        l, r = 0, len(nums)-1
        left, right = l, r
        while l <= r:
            if a > 0:
                if nums[l] < nums[r]:
                    res[right] = nums[r]
                    r -= 1
                else:
                    res[right] = nums[l]
                    l += 1
                right -= 1
            else:
                if nums[l] < nums[r]:
                    res[left] = nums[l]
                    l += 1
                else:
                    res[left] = nums[r]
                    r -= 1
                left += 1
        return res