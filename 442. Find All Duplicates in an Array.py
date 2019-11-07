'''
Title     : 442. Find All Duplicates in an Array
Problem   : https://leetcode.com/problems/find-all-duplicates-in-an-array/
'''
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        res, nset = [], set()
        for num in nums:
            if num not in nset:
                nset.add(num)
            else:
                res.append(num)
        return res