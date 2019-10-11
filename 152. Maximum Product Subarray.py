'''
Title     : 152. Maximum Product Subarray
Problem   : https://leetcode.com/problems/maximum-product-subarray/description/
'''
'''
max product subarray must reach one or both ends hence is either prefix product or suffix product or both
Reference: https://leetcode.com/problems/maximum-product-subarray/discuss/183483/In-Python-it-can-be-more-concise-PythonC%2B%2BJava
'''
class Solution(object):
    def maxProduct(self, nums):
        smun = nums[::-1]
        for i in range(1, len(nums)):
            nums[i] *= nums[i-1] or 1   # multiplied by 1 in case nums[i-1] = 0
            smun[i] *= smun[i-1] or 1
        return max(nums + smun)
'''
iterative brute force solution, note that mininum prod can become maximum once multiplied by a negative number
Reference: https://leetcode.com/problems/maximum-product-subarray/discuss/48276/Python-solution-with-detailed-explanation
'''
class Solution(object):
    def maxProduct(self, nums):
        maxProd, minProd, res = nums[0], nums[0], nums[0]
        for i in range(1, len(nums)):
            x = max(nums[i], maxProd*nums[i], minProd*nums[i])
            y = min(nums[i], maxProd*nums[i], minProd*nums[i])
            maxProd, minProd = x, y
            res = max(res, maxProd)
        return res