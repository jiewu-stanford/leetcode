'''
Title     : 42. Trapping Rain Water
Problem   : https://leetcode.com/problems/trapping-rain-water/description/
'''
'''
localized version of the 11. solution, trapped water can be accumulated column wise as we move the pointer from local leftMax to local rightMax or
from local rightMax to local leftMax by adding the local depth = min(leftMax, rightMax) - pointer height (width = 1, ref. the sketch in wfei'26 comment)
Reference: https://leetcode.com/problems/trapping-rain-water/discuss/17391/Share-my-short-solution
'''
class Solution:
    def trap(self, height: List[int]) -> int:
        res, l, r = 0, 0, len(height)-1
        leftMax, rightMax = 0, 0
        while l <= r:
            leftMax = max(leftMax, height[l])
            rightMax = max(rightMax, height[r])
            if leftMax <= rightMax:
                res += leftMax - height[l]
                l += 1
            else:
                res += rightMax - height[r]
                r -= 1
        return res
'''
iterative solution using stack to store indices with decreasing bar height, trapped water is accumulated row wise (width = i - stack[-1] -1) instead of column wise (width = 1 as above)
Reference: https://leetcode.com/problems/trapping-rain-water/discuss/17414/A-stack-based-solution-for-reference-inspired-by-Histogram
'''
class Solution:
    def trap(self, height: List[int]) -> int:
        res, stack, i = 0, [], 0
        while i < len(height):
            if not stack or height[i] <= height[stack[-1]]:
                stack.append(i)
                i += 1
            else:
                l = stack.pop()   # pop out all the left bars with height < height[i]
                if stack:
                    res += (min(height[stack[-1]], height[i])-height[l]) * (i-stack[-1]-1)   # add trapped water row wise with width = i-stack[-1]-1
        return res