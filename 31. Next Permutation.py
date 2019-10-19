'''
Title     : 31. Next Permutation
Problem   : https://leetcode.com/problems/next-permutation/description/
'''
'''
scan backward to look for the last ascending position, swap and reverse the descending segment after it for the next permutation (definition of 'lexicographically next greater'...)
Reference: https://leetcode.com/problems/next-permutation/discuss/14068/Python-solution-with-comments
Reference: https://leetcode.com/problems/next-permutation/discuss/14054/Python-solution-with-comments
'''
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        i = j = len(nums)-1
        while i > 0 and nums[i-1] >= nums[i]:
            i -= 1
        if i == 0:
            nums.reverse()
            return
        while nums[i-1] >= nums[j]:
            j -= 1
        nums[i-1], nums[j] = nums[j], nums[i-1]
        nums[i:] = nums[i:][::-1]   # in-place reverse: l = i; r = len(nums)-1
                                    #                   while l < r: nums[l], nums[r] = nums[r], nums[l]; l += 1; r -= 1