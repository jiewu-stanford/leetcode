'''
Title     : 349. Intersection of Two Arrays
Problem   : https://leetcode.com/problems/intersection-of-two-arrays/description/
'''
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return list(set(nums1) & set(nums2))

''' brute force search '''
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        for i in nums1:
            if i in nums2 and i not in res:
                res.append(i)
        return res