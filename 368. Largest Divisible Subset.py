'''
Title     : 368. Largest Divisible Subset
Problem   : https://leetcode.com/problems/largest-divisible-subset/description/
'''
'''
brute force iterative solution
Reference: https://leetcode.com/problems/largest-divisible-subset/discuss/193011/easily-understandable-python-solution-with-explanation
'''
class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        subsets = [[nums[i]] for i in range(len(nums))]   # num is a factor of itself
        for i in range(1, len(nums)):
            for j in range(i-1, -1, -1):
                if nums[i] % nums[j] == 0:   # then all factors of nums[j] are factors of nums[i]
                    if len(subsets[j]) + 1 > len(subsets[i]):
                        subsets[i] = list(subsets[j])
                        subsets[i].append(nums[i])
        res, maxLen = [], 0
        for subset in subsets:
            if len(subset) > maxLen:
                res = subset
                maxLen = len(subset)
        return res
'''
recursive solution + list comprehension
Reference: https://leetcode.com/problems/largest-divisible-subset/discuss/84002/4-lines-in-Python
'''
class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        subsets = {-1: set()}
        for num in sorted(nums):
            subsets[num] = max((subsets[k] for k in subsets if num % k == 0), key=len) | {num}   # do not forget to take union with itself
        return list(max(subsets.values(), key=len))