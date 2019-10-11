'''
Title     : 27. Remove Element
Problem   : https://leetcode.com/problems/remove-element/
'''
''' built-in .remove() function '''
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if not nums: return 0
        while val in nums:
            nums.remove(val)
        return len(nums)

''' iterative use of .append(.pop()), and faster '''
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if not nums: return 0
        ii, length = 0, len(nums)
        while ii < length:
            if nums[ii] == val:
                nums.append(nums.pop(ii))
                ii -= 1
                length -= 1
            ii += 1
        return length

''' iterative search and assign, and faster '''
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if not nums: return 0
        count = 0
        for ii in range(len(nums)):
            if nums[ii] != val:
                nums[count] = nums[ii]
                count += 1
        return count