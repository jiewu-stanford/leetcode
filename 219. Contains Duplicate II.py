'''
Title     : 219. Contains Duplicate II
Problem   : https://leetcode.com/problems/contains-duplicate-ii/
'''
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        d = {}
        for i, num in enumerate(nums):
            if num in d and i - d[num] <= k:
                return True
            d[num] = i
        return False
''' 
maintain a running set of k distinct elements and check iteratively
Reference: https://leetcode.com/problems/contains-duplicate-ii/discuss/61396/Use-hashset-40ms-python-beat-94
'''
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if len(nums) <= k: return len(nums) > len(set(nums))
        s = set(nums[:k])
        if len(s) < k:
            return True
        else:
            for i in range(k, len(nums)):
                s.add(nums[i])
                if len(s) == k: return True
                else: s.remove(nums[i-k])
        return False