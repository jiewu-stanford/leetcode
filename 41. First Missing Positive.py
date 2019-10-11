'''
Title     : 41. First Missing Positive
Problem   : https://leetcode.com/problems/first-missing-positive/
'''
''' always sort first to make problem simpler! '''
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums.sort()
        res = 1
        for num in nums:
            if num == res:
                res += 1
        return res
'''
faster but less comprehensible, since manipulating both index i and value num[i-1]
to comprehend it is better to think of the non-missiong case [-1, 0, 1, 2, 3] --> [-1, 0, inf, inf, inf]
Reference: https://leetcode.com/problems/first-missing-positive/discuss/231337/Python-solution
'''
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        L = len(nums)
        for _, n in enumerate(nums):
            if n <= 0:
                continue
            else:
                while 0 < n <= L:
                    tmp = nums[n-1]
                    nums[n-1] = float('inf')
                    n = tmp
        for i in range(L):
            if nums[i] != float('inf'):
                return i + 1
        return L + 1