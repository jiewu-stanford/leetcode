'''
Title     : 376. Wiggle Subsequence
Problem   : https://leetcode.com/problems/wiggle-subsequence/
'''
''' direct implementation '''
class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        if not nums: return 0
        prev, length = 0, 0
        for i in range(len(nums)-1):
            dif = nums[i+1] - nums[i]
            if dif != 0 and length == 0:
                length = 1
            elif dif*prev < 0:
                length += 1
            if dif != 0: prev = dif
        return length + 1
'''
zip into and examine local triplet
Reference: https://leetcode.com/problems/wiggle-subsequence/discuss/84921/3-lines-O(n)-Python-with-explanationproof
'''
import itertools
class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        if not nums: return 0
        norepeat = [num for num, _ in itertools.groupby(nums)]
        if len(norepeat) < 2:
            return len(norepeat)
        triplets = zip(norepeat, norepeat[1:], norepeat[2:])
        return 2 + sum(a<b>c or a>b<c for a,b,c in triplets)