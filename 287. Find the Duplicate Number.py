'''
Title     : 287. Find the Duplicate Number
Problem   : https://leetcode.com/problems/find-the-duplicate-number/description/
'''
'''
adapt the 142. solution by treating repetition as closure of cycle in a linked list, use array equivalence of fast-slow two pointer strategy
Reference: https://leetcode.com/problems/find-the-duplicate-number/discuss/72852/Python-same-solution-as-142-Linked-List-Cycle-II
'''
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = fast = found = 0
        while True:
            slow = nums[slow]   # nums[a] = b can be interpreted as a.next = b
            fast = nums[nums[fast]]
            if slow == fast:
                while found != slow:
                    found = nums[found]   # found traverses at the same speed of slow from the beginning of the list
                    slow = nums[slow]     # slow traverses another cycle to return to the closure of the cycle (ref. the 142. solution)
                return found
'''
use binary search on indices (in ascending order) rather than numbers
Reference: https://leetcode.com/problems/find-the-duplicate-number/discuss/72912/Python-solution-with-detailed-explanation
'''
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        if not nums: return 0
        l, r = 1, len(nums)
        while l < r:
            mid = (l + r)//2
            count = 0
            for num in nums:
                if num <= mid: count = count + 1
            if count > mid:   # more numbers than the mid index, there must be repetition in the left half
                r = mid
            else:
                l = mid + 1
        return l