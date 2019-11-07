'''
Title     : 448. Find All Numbers Disappeared in an Array
Problem   : https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/
'''
''' Reference: https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/discuss/92955/Python-4-lines-with-short-explanation '''
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for num in nums:
            indx = abs(num) - 1
            nums[indx] = -abs(nums[indx])
        return [i+1 for i, num in enumerate(nums) if num > 0]