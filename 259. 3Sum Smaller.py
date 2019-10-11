'''
Title     : 259. 3Sum Smaller ($$$)
Problem   : https://leetcode.com/problems/3sum-smaller/
          : https://www.lintcode.com/problem/3sum-smaller/description
'''
class Solution:
    def threeSumSmaller(self, nums, target):
        nums.sort()
        count = 0
        for k in range(len(nums)):
            i, j = 0, k-1
            while i < j:
                if nums[i] + nums[j] + nums[k] < target:
                    count += j - i   # if (i,j,k) is a valid triplet so are (i,i+1,k), ... (i,j-1,k)
                    i += 1
                else:
                    j -= 1
        return count