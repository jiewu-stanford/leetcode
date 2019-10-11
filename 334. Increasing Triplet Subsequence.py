'''
Title     : 334. Increasing Triplet Subsequence
Problem   : https://leetcode.com/problems/increasing-triplet-subsequence/description/
'''
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        if len(nums) < 3: return False
        n1 = n2 = float('inf')
        for num in nums:
            if num <= n1:
                n1 = num
            elif num <= n2:
                n2 = num
            else:
                return True   # i.e. num > n1 AND num > n2 thus (n1, n2, num) form a triplet
        return False