'''
Title     : 321. Create Maximum Number
Problem   : https://leetcode.com/problems/create-maximum-number/
'''
'''
divide-and-conquer: (1) select a sublist consisting of the n largest numbers from nums (2) merge and compare to find the max
Reference: https://leetcode.com/problems/create-maximum-number/discuss/77286/Short-Python-Ruby-C%2B%2B
         : https://leetcode.com/problems/create-maximum-number/discuss/77291/Share-my-Python-solution-with-explanation
'''
class Solution:
    def maxNumber(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        def selection(nums, n):
            rem = len(nums) - n
            out = []
            for num in nums:
                while rem and out and out[-1] < num:
                    out.pop()
                    rem -= 1
                out.append(num)
            return out[:n]

        def merge(nums1, nums2):
            res = []
            while nums1 or nums2:
                if nums1 > nums2:   # when comparing two lists of numbers the leading digit matters, hence [9, 7] > [6, 0, 4]
                    res += nums1[0],   # , converts int to tuple so that it becomes iterable
                    nums1 = nums1[1:]
                else:
                    res += nums2[0],
                    nums2 = nums2[1:]
            return res
            # return [max(nums1, nums2).pop(0) for _ in nums1 + nums2]   this one-liner is much faster than the while loop

        combs = [merge(selection(nums1, i), selection(nums2, k-i))
                    for i in range(k+1)
                    if i <= len(nums1) and k-i <= len(nums2)]
        return max(combs)