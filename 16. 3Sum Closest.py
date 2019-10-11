'''
Title     : 16. 3Sum Closest
Problem   : https://leetcode.com/problems/3sum-closest/
'''
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        L = len(nums)
        nums.sort()
        min_diff = float('inf')
        closest_sum = 0
        for i in range(L - 2):
            if i > 0 and nums[i-1] == nums[i]: continue
            l, r = i+1, L-1
            while l < r:
                trisum = nums[i] + nums[l] + nums[r]
                dif = abs(target - trisum)
                if dif == 0:
                    return target
                if dif < min_diff:
                    min_diff = dif
                    closest_sum = trisum
                if trisum < target:
                    l += 1
                else:
                    r -= 1
        return closest_sum