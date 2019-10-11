'''
Title     : 6. ZigZag Conversion
Problem   : https://leetcode.com/problems/zigzag-conversion/
'''
'''
just trace out a zigzag pattern by reversing the direction when hitting top row/bottom row
Reference: https://leetcode.com/problems/zigzag-conversion/discuss/3404/Python-O(n)-Solution-in-96ms-(99.43)
'''
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s): return s
        rows, indx = ['']*numRows, 0
        for c in s:
            rows[indx] += c
            if indx == 0: step = 1   # reach the top row, head down
            elif indx == numRows-1: step = -1   # reach the bottom row, head up
            indx += step
        return ''.join(rows)
'''
using mod operation to realize the same direction reversal
Reference: https://leetcode.com/problems/zigzag-conversion/discuss/3736/My-easy-read-python-solution
'''
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s): return s
        rows = ['']*numRows
        period = (numRows - 1) * 2   # for zigzag pattern the period is 2*numRows (one up + one down) similar to sine wave
        for i, c in enumerate(s):
            if i % period >= numRows:
                rows[(period - i % period)] += c
            else:
                rows[i % period] += c
        return ''.join(rows)