'''
Title     : 85. Maximal Rectangle
Problem   : https://leetcode.com/problems/maximal-rectangle/description/
'''
'''
the first instinct is to try adapting the 221. solution since it is 'merely' generalization from square to rectangle, however it turns out that
allowing width and height to be independent variables causes enormous difficulty in determining the max rectangle out of three overlapping rectangles
which is much easier if all are required to be square, below is one attempt to solve the problem in this manner which is rather complicated
Reference: https://leetcode.com/problems/maximal-rectangle/discuss/132978/python-DP-solution-motivated-by-221-maximal-square
instead we adapt the 84. solution by viewing every row as a ground with histogram on top of it, the height = the count of CONSECUTIVE '1's from that row to above
Reference: https://leetcode.com/problems/maximal-rectangle/discuss/29065/AC-Python-DP-solutioin-120ms-based-on-largest-rectangle-in-histogram
'''
class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix: return 0
        r, c = len(matrix), len(matrix[0])
        res, heights = 0, [0]*(c+1)
        for row in matrix:
            for i in range(c):
                heights[i] = heights[i] + 1 if row[i] == '1' else 0   # height reset to 0 if it is '0' in the above row i.e. consecutive '1's terminated
            # the following is copied from the 84. solution
            stack = [-1]
            for i in range(c+1):
                while heights[i] < heights[stack[-1]]:
                    h = heights[stack.pop()]
                    w = (i-1) - stack[-1]
                    res = max(res, h * w)
                stack.append(i)
        return res