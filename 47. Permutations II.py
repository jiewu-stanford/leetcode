'''
Title     : 47. Permutations II
Problem   : https://leetcode.com/problems/permutations-ii/
'''
'''
adapt the 46. solution by inserting a break whenever the number is inserted before its duplicate (duplication happens when we insert both before and after)
Reference: https://leetcode.com/problems/permutations-ii/discuss/18602/9-line-python-solution-with-1-line-to-handle-duplication-beat-99-of-others-%3A-)
'''
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        perms = [[]]
        for num in nums:
            newperms = []
            for perm in perms:
                for i in range(len(perm)+1):
                    newperms.append(perm[:i] + [num] + perm[i:])
                    if i < len(perm) and perm[i] == num: break   # avoid inserting a number after any of its duplicates e.g. add '1' to [1, 2] only before 1 but not after it i.e. ['1', 1, 2] not [1, '1', 2]
            perms = newperms
        return perms
'''
a clever way of finding the first index of the new number to be inserted so as to avoid inserting a number after any of its duplicates
Reference: https://leetcode.com/problems/permutations-ii/discuss/18616/6-lines-Python-Ruby
'''
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        perms = [[]]
        for num in nums:
            newperms = []
            for perm in perms:
                for i in range((perm+[num]).index(num)+1):
                    newperms.append(perm[:i] + [num] + perm[i:])
            perms = newperms
        return perms
'''
DFS recursive helper function with sorted version of nums
Reference: https://leetcode.com/problems/permutations-ii/discuss/18649/Python-easy-to-understand-backtracking-solution
'''
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        self.helper(nums, [], res)
        return res

    def helper(self, nums, acc, res):
        if not nums:
            res.append(acc)
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]: continue   # only add after duplicate by skipping repetition
            self.helper(nums[:i]+nums[i+1:], acc+[nums[i]], res)