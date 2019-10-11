'''
Title     : 15. 3Sum
Problem   : https://leetcode.com/problems/3sum/
'''
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        L = len(nums)
        if L < 3: return []
        nums.sort()
        triplets = list()
        for i in range(L - 2):
            if nums[i] > 0: break   # smallest one must < 0 for trisum = 0
            if i > 0 and nums[i-1] == nums[i]: continue
            l, r = i+1, L-1
            while l < r:
                trisum = nums[i] + nums[l] + nums[r]
                if trisum == 0:
                    triplets.append([nums[i], nums[l], nums[r]])
                    l += 1
                    while l < r and nums[l-1] == nums[l]:   # if i > 0 and nums[i-1] == nums[i]
                        l += 1
                elif trisum < 0:
                    l += 1
                else:
                    r -= 1
        return triplets