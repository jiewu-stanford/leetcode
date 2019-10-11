'''
Title     : 119. Pascal's Triangle II
Problem   : https://leetcode.com/problems/pascals-triangle-ii/
'''
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        row = [1]
        for i in range(1, rowIndex+1):
            row = [1] + [row[i]+row[i+1] for i in range(len(row)-1)] + [1]
        return row