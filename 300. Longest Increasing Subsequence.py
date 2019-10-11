'''
Title     : 300. Longest Increasing Subsequence
Problem   : https://leetcode.com/problems/longest-increasing-subsequence/description/
'''
'''
variant of insertion sort, replace instead of insert
Reference: https://leetcode.com/problems/longest-increasing-subsequence/discuss/74977/Python-nlogn-binary-search-44ms-solution
'''
class Solution(object):
    def lengthOfLIS(self, nums):
        if not nums: return 0
        res = [nums[0]]
        for num in nums:
            if num <= res[0]:
                res[0] = num
            elif num > res[-1]:
                res.append(num)
            else:
                indx = self.binarySearch(res, 0, len(res), num)   # indx = bisect.bisect_left(res, num)
                res[indx] = num
        return len(res)

    def binarySearch(self, nums, l, r, target):
        while l < r:
            mid = (l + r) // 2
            if nums[mid] < target:
                l = mid + 1
            else:
                r = mid   # r = mid - 1 if l <= r
        return l
'''
use patience sort, collect the smallest among the set of tails of all increasing subsequences with the same length
Reference: https://leetcode.com/problems/longest-increasing-subsequence/discuss/74824/JavaPython-Binary-search-O(nlogn)-time-with-explanation
'''
class Solution(object):
    def lengthOfLIS(self, nums):
        if not nums: return 0
        tails = [0] * len(nums)   # tails[i] = the samllest among the tails of all increasing subsequences with length i+1
        length = 0
        for num in nums:
            l, r = 0, length
            while l < r:
                mid = (l + r) // 2
                if tails[mid] < num:
                    l = mid + 1
                else:
                    r = mid
            tails[l] = num   # tails[l-1] < num <= tails[l], update tails[l] with num
            length = max(length, l + 1)
        return length