'''
Title     : 164. Maximum Gap
Problem   : https://leetcode.com/problems/maximum-gap/
'''
'''
bucket sort, bucket size provides a upper bound for the differences within bucket, thus max difference can only occur between adjacent filled buckets
also note that the bucket size is defined as the average difference hence it is impossible for all differences to be smaller than bucket size
in one sentence: max difference >= average difference = bucket size
Reference: https://leetcode.com/problems/maximum-gap/discuss/50650/Python-bucket-sort-from-official-solution
'''
class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        if len(nums) < 2 or max(nums)==min(nums): return 0
        maxN, minN, lenN = max(nums), min(nums), len(nums)
        bucketSize = (maxN-minN)//(lenN-1) or 1
        buckets = [[None, None] for _ in range((maxN-minN)//bucketSize+1)]
        for num in nums:   # sort nums into buckets, keeping record of min and max within each bucket
            bucketId = (num-minN)//bucketSize
            buckets[bucketId][0] = num if buckets[bucketId][0] is None else min(num, buckets[bucketId][0])
            buckets[bucketId][1] = num if buckets[bucketId][1] is None else max(num, buckets[bucketId][1])
        nonEmpty = [bucket for bucket in buckets if bucket[0] is not None]   # get rid of empty buckets
        return max(nonEmpty[i][0]-nonEmpty[i-1][1] for i in range(1,len(nonEmpty)))
'''
use linear radix sort (https://www.youtube.com/watch?v=YXFI4osELGU) and then one-pass to find the max difference
Reference: https://leetcode.com/problems/maximum-gap/discuss/50649/Simple-radix-sort-solution-in-python
'''
class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        def radixsort(nums):
            indx, bits = 0, 32
            while indx < bits:
                zeros, ones = [], []
                for num in nums:
                    if num & (1 << indx): ones.append(num)
                    else: zeros.append(num)
                nums = zeros + ones
                indx += 1
            return nums

        nums = radixsort(nums)
        return max([b - a for a, b in zip(nums, nums[1:])] or [0])