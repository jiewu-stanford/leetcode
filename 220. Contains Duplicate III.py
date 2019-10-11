'''
Title     : 220. Contains Duplicate III
Problem   : https://leetcode.com/problems/contains-duplicate-iii/
'''
''' brute force is the shortest, nonetheless TLE! '''
class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        for i in range(0, len(nums)):
            for j in range(i+1, i+k+1):   # indx_diff <= k
                if j < len(nums) and abs(nums[i]-nums[j]) <= t:   # num_diff <= t
                    return True
        return False
'''
the condition puts equal weighting on index and value i.e. num_diff <= t and indx_diff <= k thus we can swap the two conditions, and it passes TLE!
Reference: https://leetcode.com/problems/contains-duplicate-iii/discuss/61706/Python-without-dictionary
'''
class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        indx = sorted(range(len(nums)), key=lambda x: nums[x])
        for i in range(len(nums)-1):
            j = i + 1
            while j < len(nums) and nums[indx[j]]-nums[indx[i]] <= t:   # num_diff <= t
                if abs(indx[i]-indx[j]) <= k: return True   # indx_diff <= k
                j += 1
        return False
'''
use bubble sort, place numbers into buckets of width t
Reference: https://leetcode.com/problems/contains-duplicate-iii/discuss/61731/O(n)-Python-using-buckets-with-explanation-10-lines
Reference: https://leetcode.com/problems/contains-duplicate-iii/discuss/61756/Python-OrderedDict
'''
class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        if k < 1 or t < 0: return False
        buckets = {}
        for i, num in enumerate(nums):
            bucketId = num//t if t else num
            for j in (bucketId-1, bucketId, bucketId+1):   # the candidate number can only be in the same bucket or adjacent buckets
                if j in buckets and abs(buckets[j] - nums[i]) <= t:
                    return True
            if len(buckets) == k:
                del buckets[nums[i-k]//t if t else nums[i-k]]   # remove buckets that are out of k index bound
            buckets[bucketId] = nums[i]
        return False
'''
use ordereddict() to enforce num_diff <= t condition
Reference: https://leetcode.com/problems/contains-duplicate-iii/discuss/61756/Python-OrderedDict
'''
import collections
class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        if k < 1 or t < 0: return False
        buckets = collections.OrderedDict()
        for num in nums:
            bucketId = num//t if t else num
            for j in (buckets.get(bucketId-1), buckets.get(bucketId), buckets.get(bucketId+1)):
                if j is not None and abs(num - j) <= t:
                    return True
            if len(buckets) == k:
                buckets.popitem(False)
            buckets[bucketId] = num
        return False