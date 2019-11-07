'''
Title     : 457. Circular Array Loop
Problem   : https://leetcode.com/problems/circular-array-loop/
'''
class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        n = len(nums)
        for i, num in enumerate(nums):
            length = 0
            j = i
            forward = nums[j] > 0
            while True:
                if forward != (nums[j] > 0):
                    break
                nj = (j + nums[j] + n) % n
                if nj == j:
                    break
                j = nj
                length += 1
                if length > n:
                    return True
        return False