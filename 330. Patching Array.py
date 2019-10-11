'''
Title     : 330. Patching Array
Problem   : https://leetcode.com/problems/patching-array/description/
'''
'''
induction step: if we have covered range [1 -> K], then adding the missing (K+1) can extend the range to [1 -> 2*K + 1] since K + (K + 1) = 2*K + 1
Reference: https://leetcode.com/problems/patching-array/discuss/78495/Share-my-thinking-process
Reference: https://leetcode.com/problems/patching-array/discuss/78488/Solution-%2B-explanation
'''
class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        patch, miss, i = 0, 1, 0
        while miss <= n:
            if i < len(nums) and nums[i] <= miss:   # loop till miss = max of the covered range + 1 = (K+1)
                                                    
                miss += nums[i]
                i += 1
            else:              # if nums[i] > miss then nums[i] is out of range even after patching miss e.g. 23 in [1,2,4,23,43]
                miss += miss   # thus patch miss and lift miss from (K+1) to (2K+2) for the remaining numbers in nums
                patch += 1
        return patch