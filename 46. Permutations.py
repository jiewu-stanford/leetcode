'''
Title     : 46. Permutations
Problem   : https://leetcode.com/problems/permutations/
'''
''' there is actually a built-in function for this '''
import itertools
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        return list(itertools.permutations(nums))
'''
step-by-step build-up by adding n to the permutations of 1,2,...,n-1
Reference: https://leetcode.com/problems/permutations/discuss/18237/My-AC-simple-iterative-javapython-solution
'''
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        perms = [[]]
        for num in nums:
            newperms = []
            for perm in perms:
                for i in range(len(perm)+1):
                    newperms.append(perm[:i] + [num] + perm[i:])
            perms = newperms
        return perms
'''
recursive solution using the same step-by-step construction steps
Reference: https://leetcode.com/problems/permutations/discuss/18570/A-python-code-for-permutation
'''
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 2: return [nums]
        res = []
        for perm in self.permute(nums[:-1]):
            res += [perm[:i] + [nums[-1]] + perm[i:] for i in range(len(perm)+1)]
        return res