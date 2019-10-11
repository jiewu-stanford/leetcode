'''
Title     : 229. Majority Element II
Problem   : https://leetcode.com/problems/majority-element-ii/
'''
'''
since the problem requires linear time, we can no longer use sorted(nums)[len(nums)//3] which takes squared time
instead we use Boyer-Moore algorithm, which sacrifices the actual count (relative count instead) for speed
Reference: https://leetcode.com/problems/majority-element-ii/discuss/63520/Boyer-Moore-Majority-Vote-algorithm-and-my-elaboration
'''
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        if not nums: return []
        count1, count2, candidate1, candidate2 = 0, 0, 0, 1
        for n in nums:
            if n == candidate1:
                count1 += 1
            elif n == candidate2:
                count2 += 1
            elif count1 == 0:
                candidate1, count1 = n, 1
            elif count2 == 0:
                candidate2, count2 = n, 1
            else:
                count1, count2 = count1-1, count2-1   # key step of Boyer-Moore, absolute count -> relative count
        return [n for n in (candidate1, candidate2) if nums.count(n)>len(nums)//3]