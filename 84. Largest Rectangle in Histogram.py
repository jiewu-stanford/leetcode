'''
Title     : 84. Largest Rectangle in Histogram
Problem   : https://leetcode.com/problems/largest-rectangle-in-histogram/
'''
'''
one-pass solution, add bar one by one, do not compare area while the bars are ascending because so is the area, the bar beginning to
descend signals the possible existence of max area, examine the ascending bars from right to left to find the (local) max area
Reference: https://leetcode.com/problems/largest-rectangle-in-histogram/discuss/28917/AC-Python-clean-solution-using-stack-76ms
'''
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        if not heights: return 0
        heights.append(0)   # to trigger the last comparison with the area ended by the rightmost bar
        res, stack = 0, [-1]
        for i in range(len(heights)):
            while heights[i] < heights[stack[-1]]:
                h = heights[stack.pop()]
                w = (i-1) - stack[-1]
                res = max(res, h * w)
            stack.append(i)
        heights.pop()   # cleanup for heights.append(0)
        return res
'''
two-pass solution, find for each bar the max area of the rectangle whose height is determined by it, scan from left to right to find
the extent of stretching such a rectangle to left and scan from right to left to find the extent of stretching such a rectangle to right
Reference: https://leetcode.com/problems/largest-rectangle-in-histogram/discuss/28963/Python-solution-without-using-stack.-(with-explanation)
'''
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        if not heights: return 0
        n = len(heights)
        left, right = [1]*n, [1]*n   # extent of stretching the rectangle to the left and the right
        
        for i in range(1, n):
            j = i - 1
            while j >= 0 and heights[j] >= heights[i]:
                j -= left[j]
            left[i] = i - j
            
        for i in range(n-2, -1, -1):
            j = i + 1
            while j < len(heights) and heights[j] >= heights[i]:
                j += right[j]
            right[i] = j - i
            
        res = 0
        for i in range(n):
            res = max(res, heights[i]*(left[i]+right[i]-1))   # -1 since bar i is counted twice
        return res