'''
Title     : 128. Longest Consecutive Sequence
Problem   : https://leetcode.com/problems/longest-consecutive-sequence/description/
'''
'''
to qualify for the start of the sequence: n in set while n-1 not in set, to qualify for the end of the sequence: n in set while n+1 not in set
Reference: https://leetcode.com/problems/longest-consecutive-sequence/discuss/41057/Simple-O(n)-with-Explanation-Just-walk-each-streak
'''
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        longest = 0
        for n in nums:
            if n - 1 not in nums:   # start of the sequence
                m = n + 1
                while m in nums:   # find end of the sequence
                    m += 1
                longest = max(longest, m - n)
        return longest
'''
use set and .remove() to avoid repetitive end point identification
Reference: https://leetcode.com/problems/longest-consecutive-sequence/discuss/41202/Python-O(n)-solution-using-sets
'''
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        longest = 0
        while nums:
            first = last = nums.pop()
            while first-1 in nums:
                first -= 1
                nums.remove(first)
            while last+1 in nums:
                last += 1
                nums.remove(last)
            longest = max(longest, last-first+1)
        return longest