'''
Title     : 325. Maximum Size Subarray Sum Equals k ($$$)
Problem   : https://leetcode.com/problems/maximum-size-subarray-sum-equals-k/
          : https://www.lintcode.com/problem/maximum-size-subarray-sum-equals-k/description
'''
'''
the idea is that [i:j] subarray sum = cumulative sum up to j - cumulative sum up to i
in case cumulative sum to 0 then we should count the length from start i.e. i - dic[0] = i + 1
Reference: http://www.voidcn.com/article/p-pbvzylrp-qp.html
'''
class Solution(object):
    def maxSubArrayLen(self, nums, k):
        res, acc = 0, 0
        d = {0: -1}
        for i in range(len(nums)):
            acc += nums[i]
            if acc not in d:
                d[acc] = i
            if acc - k in d:
                res = max(res, i-d[acc-k])
        return res