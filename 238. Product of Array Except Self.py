'''
Title     : 238. Product of Array Except Self
Problem   : https://leetcode.com/problems/product-of-array-except-self/
'''
'''
brute force double pass, use the following commands to see incrementing subsets of indices and 
how one is displaced and combined with the other to produce subsets with exactly one missing index
for i in range(0, n): leftacc.append(i); print(leftacc)
for i in range(n-1, -1, -1): rightacc.append(i); print(rightacc)
Reference: https://leetcode.com/problems/product-of-array-except-self/discuss/65625/Python-solution-(Accepted)-O(n)-time-O(1)-space
'''
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod, n = 1, len(nums)
        res = []
        for i in range(0, n):
            res.append(prod)
            prod = prod * nums[i]
        prod = 1
        for i in range(n-1, -1, -1):
            res[i] = res[i] * prod
            prod = prod * nums[i]
        return res
'''
one pass using two variables to store left product and right product
Reference: https://leetcode.com/problems/product-of-array-except-self/discuss/65797/Consice-answer-in-Python
'''
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        leftprod, rightprod, n = 1, 1, len(nums)
        res = [1] * n
        for i in range(n):
            res[i] *= leftprod
            res[n-i-1] *= rightprod
            leftprod *= nums[i]
            rightprod *= nums[n-i-1]
        return res