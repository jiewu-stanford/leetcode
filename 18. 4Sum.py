'''
Title     : 18. 4Sum
Problem   : https://leetcode.com/problems/4sum/
'''
''' pair up to convert to the 2-sum problem '''
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        pair_nums = {}
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                pair_num = nums[i] + nums[j]
                if pair_num in pair_nums:
                    pair_nums[pair_num].append((i, j))
                else:
                    pair_nums[pair_num] = [(i, j)]
                    
        quadruplets = set()
        for key, val in pair_nums.items():
            dif = target - key
            if dif in pair_nums:
                pair1, pair2 = val, pair_nums[dif]
                for i, j in pair1:
                    for k, l in pair2:
                        quad = [i, j, k, l]
                        if len(set(quad)) != len(quad): continue
                        quadruplet = [nums[i], nums[j], nums[k], nums[l]]
                        quadruplet.sort()
                        quadruplets.add(tuple(quadruplet))
        return list(quadruplets)

''' iterative solution, more comprehensible but much slower '''
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        quadruplets = []
        L = len(nums)
        for i in range(L-3):
            if i > 0 and nums[i-1] == nums[i]: continue
            for j in range(i+1, L-2):
                if j > i + 1 and nums[j-1] == nums[j]: continue
                dif = target - nums[i] - nums[j]
                l, r = j+1, L-1
                while l < r:
                    if nums[l] + nums[r] == dif:
                        quadruplets.append((nums[i], nums[j], nums[l], nums[r]))
                        r -= 1
                        l += 1
                        while l < r and nums[l-1] == nums[l]:
                            l += 1
                        while l < r and nums[r] == nums[r+1]:
                            r -= 1
                    elif nums[l] + nums[r] > dif:
                        r -= 1
                    else:
                        l += 1
        return quadruplets
'''
combine the solution of 1. Two Sum and 15. 3Sum
Reference: https://programmer.help/blogs/leetcode-2sum-3sum-4sum-python.html
'''
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        if len(nums) < 4: return []
        nums.sort()
        
        def threeSum(nums, target):   # the 15. solution
            def twoSum(nums, target, num, triplets):   # the 1. solution
                l, r, tgt = 0, len(nums)-1, target-num
                while l != r:
                    if nums[l] + nums[r] < tgt:
                        l += 1
                    elif nums[l] + nums[r] > tgt:
                        r -= 1
                    else:
                        triplet = [num, nums[l], nums[r]]
                        l += 1
                        while l != r and nums[l-1] == nums[l]:
                            l += 1
                        triplets.append(triplet)
                return triplets
            result = []
            for i in range(len(nums)-2):
                if i > 0 and nums[i-1] == nums[i]:
                    continue
                else:
                    remnant = nums[i+1:]
                    result = twoSum(remnant, target, nums[i], result)
            return result
        
        res = []
        for i in range(len(nums)-3):
            if i > 0 and nums[i-1] == nums[i]:
                continue
            num = nums[i]
            trisum = target - num
            rem = nums[i+1:]
            triples = threeSum(rem, trisum)
            if len(triples) > 0:
                for triple in triples:
                    triple.append(num)
                    res.append(triple)
        return res