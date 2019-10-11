'''
Title     : 228. Summary Ranges
Problem   : https://leetcode.com/problems/summary-ranges/description/
'''
''' Reference: https://leetcode.com/problems/summary-ranges/discuss/63193/6-lines-in-Python '''
class Solution(object):
    def summaryRanges(self, nums):
        ranges = []
        for num in nums:
            if not ranges or num > ranges[-1][-1]+1:
                ranges += [],
            ranges[-1][1:] = num,   # , converts int to tuple to become iterable
        return ['->'.join(map(str, range)) for range in ranges]

''' Reference: https://leetcode.com/problems/summary-ranges/discuss/63393/7-line-Python-implementation '''
class Solution(object):
    def summaryRanges(self, nums):
        start, res = 0, []
        printout = lambda start, end: str(start) + '->' + str(end) if start != end else str(start)
        for i in range(1, len(nums)+1):
            if i == len(nums) or nums[i]-nums[i-1]!=1:
                res.append(printout(nums[start], nums[i-1]))
                start = i
        return res