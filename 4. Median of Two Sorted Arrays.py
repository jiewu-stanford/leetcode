'''
Title     : 4. Median of Two Sorted Arrays
Problem   : https://leetcode.com/problems/median-of-two-sorted-arrays/
'''
'''
idea: (1) translate median into half-length smallest
      (2) recursive + balanced tree like search
Reference : https://leetcode.com/problems/median-of-two-sorted-arrays/discuss/2802/Python-O(lg(m%2Bn))-recursive-solution
'''
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        L = len(nums1) + len(nums2)
        if L % 2:
            return self.findKthSmallest(nums1, nums2, L//2+1)
        else:
            return (self.findKthSmallest(nums1, nums2, L//2) +
                    self.findKthSmallest(nums1, nums2, L//2+1))/2
        
    def findKthSmallest(self, nums1, nums2, k):
        if len(nums1) > len(nums2):
            return self.findKthSmallest(nums2, nums1, k)
        if not nums1:
            return nums2[k-1]
        if k == 1:
            return min(nums1[0], nums2[0])            
        sub1 = min(k//2, len(nums1))
        sub2 = k - sub1
        if nums1[sub1-1] <= nums2[sub2-1]:
            return self.findKthSmallest(nums1[sub1:], nums2, k-sub1)   # ignore first sub1 elements of nums1 since they are guaranteed <= the kth smallest
        else:
            return self.findKthSmallest(nums1, nums2[sub2:], k-sub2)