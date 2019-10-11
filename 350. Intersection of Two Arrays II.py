'''
Title     : 350. Intersection of Two Arrays II
Problem   : https://leetcode.com/problems/intersection-of-two-arrays-ii/description/
'''
'''
use counter() and &, note that intersection is applicable to not only set but also counter data structure
Reference: https://leetcode.com/problems/intersection-of-two-arrays-ii/discuss/82240/2-lines-in-Python
'''
import collections
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        c1 = collections.Counter(nums1)
        c2 = collections.Counter(nums2)
        return list((c1 & c2).elements())
'''
brute force search using list.remove() function instead of comparing number of occurrence using dict() etc., readily adapted from the 349. solution
Reference: https://leetcode.com/problems/intersection-of-two-arrays-ii/discuss/82254/SImple-Python-solution
'''
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        for i in nums1:
            if i in nums2:
                nums2.remove(i)
                res.append(i)
        return res